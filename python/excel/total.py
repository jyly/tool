import  xdrlib ,sys
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
	
def excel_table_byindex_d(file,colnameindex=0,by_index=0): 
#标题列数、表位数
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #行数
	ncols = table.ncols #列数
	dic={}
	for rownum in range(nrows):
		row = table.row_values(rownum)
		if row[0] in dic:
			for i in range(1,ncols):
				if row[i]:
					dic[row[0]].append(row[i])
		else:
			dic[row[0]]=[]
			for i in range(1,ncols):
				if row[i]:
					dic[row[0]].append(row[i])
	return dic
	
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
		content='%s, %s' % (content_i*5,content_t) 
		tags = jieba.analyse.extract_tags(content,topK=5)
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
		tags = jieba.analyse.extract_tags(content,topK=3)
		for i in tags:
			app.append(i)
		userlist[key]=app
	
	excel_write('new.xls',newlist)
	excel_write('user.xls',userlist)
	
	table_r = excel_table_byindex_d('read.xlsx')#阅读记录
	table_f = excel_table_byindex_d('find.xlsx')#查询表
	recommend={}
	for row_f in table_f:    #检索测试表用户
		if row_f in userlist  :
			for i in userlist  [row_f]: #检索兴趣
				for j in newlist [i]:	#检索新闻
					if j not in table_r[row_f]:
						print j
						if 	row_f not in recommend:
							recommend[row_f]=[]
							recommend[row_f].append(j)
						else:
							recommend[row_f].append(j)
		
	excel_write('recommend.xls',recommend)
	
	
	hit=0
	L=0
	for row_f in table_f:    #检索测试表用户
		if row_f in recommend:
			for j in table_f[row_f]:
				for i in recommend[row_f]: #检索推荐表
					L=L+1
					
					if i ==j:
						hit=hit+1
	float(hit)
	hit=float(hit)	
	L=float(L)
	precision=float(hit/L)
	print ("hit=%f,L=%f,precision=%f"%(hit, L,precision))
	recall=hit/10000
	print recall
	F=2/(1/precision+1/recall)
	print F
	print "finish"

		
if __name__=="__main__":
	main()	