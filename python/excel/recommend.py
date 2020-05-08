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
	table_n = excel_table_byindex('new.xls')#新闻表
	table_u = excel_table_byindex('user.xls')#用户表
	table_r = excel_table_byindex('read.xlsx')#阅读记录
	table_f = excel_table_byindex('find.xlsx')#查询表
	recommend={}
	for row_f in table_f:    #检索测试表用户
		if row_f in table_u:
			for i in table_u[row_f]: #检索兴趣
				for j in table_n[i]:	#检索新闻
					if j not in table_r[row_f]:
						print j
						if 	row_f not in recommend:
							recommend[row_f]=[]
							recommend[row_f].append(j)
						else:
							recommend[row_f].append(j)
		
	excel_write('recommend.xls',recommend)
	print "finish"
		
		
		
if __name__=="__main__":
	main()	