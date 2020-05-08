#coding:utf-8
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
	table_r = excel_table_byindex('recommend.xls')#新闻表
	table_f = excel_table_byindex('find.xlsx')#查询表
	hit=0
	L=0
	temp=0
	for row_f in table_f:    #检索测试表用户
		if row_f in table_r:
			j=table_f[row_f][0]
			for i in table_r[row_f]: #检索推荐表
				L=L+1
				if i ==j:
					hit=hit+1
	float(hit)
	hit=float(hit)	
	L=float(L)
	precision=float(hit/L)
	print ("新闻推荐成功条数：%f    新闻中总推荐数：%f"%(hit,L))
	recall=hit/10000
	print ("精确度：%f   召回率：%f"%(precision,recall))
	F=2/(1/precision+1/recall)
	print ("工作效率：%f"%(F))
	print "finish"
		
		
		
if __name__=="__main__":
	main()	