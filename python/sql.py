import MySQLdb
 
try:
    conn=MySQLdb.connect(host='localhost',user='root',passwd='root',db='test',port=3306)
    cur=conn.cursor()
    i=cur.execute('select * from user')
print i
result=cur.fetchone()
print result[0],result[1]
results=cur.fetchmany(5)
for r in results:
	print r
sql_insert = "insert user values ('name','pwd')"
sql_update = "update user set password='666' where password='pwd'"
sql_delete = "delete from user where passwor='612'"	
conn.commit()
conn.rollback()
cur.close()
conn.close()
except MySQLdb.Error,e:
	print "Mysql Error %d: %s" % (e.args[0], e.args[1])


sql='select * from user'
curs.execute(sql)
print curs.rowcount
rs=curs.fetchall()

    # fetchone(): 该方法获取下一个查询结果集。结果集是一个对象
    # fetchall():接收全部的返回结果行.
    # rowcount: 这是一个只读属性，并返回执行execute()方法后影响的行数。
try:
   # 执行SQL语句
	cursor.execute(sql)
   # 向数据库提交
	db.commit()
except:
   # 发生错误时回滚
	db.rollback()

for row in rs:
	print 'user=%s,pwd=%s'%(row)
# rs=curs.fetchone()
print rs

