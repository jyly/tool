import xdrlib ,sys
import xlrd
import xlwt
import jieba
import jieba.analyse

def open_excel(file):
    try:
        data = xlrd.open_workbook(file)
        return data
    except Exception,e:
        print str(e)
	

def excel_table_byindex(file,colnameindex=0,by_index=0): 
#标题列数、表位数
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #行数
	ncols = table.ncols #列数
	colnames =  table.row_values(colnameindex) #某一行数据
	list =[]
	for rownum in range(1,nrows):
		row = table.row_values(rownum)
		if row:
			app = {}
			for i in range(len(colnames)):
				app[i] = row[i]
			list.append(app)
	return list

def excel_write(file,dic):
	wb = xlwt.Workbook()
	ws = wb.add_sheet('sheet1')
	i=0
	for key in dic:
		ws.write(i,0,key)
		j=1
		for cod in dic[key]:
			if j==254:
				i=i+1
				j=1
				ws.write(i,0,key)
				ws.write(i,j,cod)
				j=j+1
			else:
				ws.write(i,j,cod)			
				j=j+1
		i=i+1
	wb.save(file)

	
def main():
	tables = excel_table_byindex('train.xlsx')
	newlist ={}
	userlist={}
	for row in tables:
		content_i=row[2]
		content_t=row[3]
		if content_i=='404' or content_t=='NULL'or type(content_i)=='float' or type(content_t)=='float':
			continue
		content='%s, %s' % (content_i*3,content_t) 
		tags = jieba.analyse.extract_tags(content,topK=3)
		print(",".join(tags))	
		for i in range(len(tags)):	
			if tags[i] not in newlist:
				newlist[tags[i]]=[]
				newlist[tags[i]].append(row[1])
			else:
				newlist[tags[i]].append(row[1])
			if row[0] not in userlist:
				userlist[row[0]]=[]
				userlist[row[0]].append(tags[i])
			else:
				userlist[row[0]].append(tags[i])
			
			
	for key in newlist:
		app=[]
		for i in newlist[key]:
			if i not in app:
				app.append(i)
		newlist[key]=app

	for key in userlist:
		app=[]
		content=(",".join(userlist[key]))
		tags = jieba.analyse.extract_tags(content,topK=5)
		for i in tags:
			app.append(i)
		userlist[key]=app
	
	excel_write('new.xls',newlist)
	excel_write('user.xls',userlist)
	print "finish"

		
if __name__=="__main__":
	main()	