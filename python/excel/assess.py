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
#������������λ��
	data = open_excel(file)
	table = data.sheets()[by_index]
	nrows = table.nrows #����
	ncols = table.ncols #����
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
	table_r = excel_table_byindex('recommend.xls')#���ű�
	table_f = excel_table_byindex('find.xlsx')#��ѯ��
	hit=0
	L=0
	temp=0
	for row_f in table_f:    #�������Ա��û�
		if row_f in table_r:
			j=table_f[row_f][0]
			for i in table_r[row_f]: #�����Ƽ���
				L=L+1
				if i ==j:
					hit=hit+1
	float(hit)
	hit=float(hit)	
	L=float(L)
	precision=float(hit/L)
	print ("�����Ƽ��ɹ�������%f    ���������Ƽ�����%f"%(hit,L))
	recall=hit/10000
	print ("��ȷ�ȣ�%f   �ٻ��ʣ�%f"%(precision,recall))
	F=2/(1/precision+1/recall)
	print ("����Ч�ʣ�%f"%(F))
	print "finish"
		
		
		
if __name__=="__main__":
	main()	