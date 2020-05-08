# -*- coding: utf-8 -*-
import numpy as np
import jieba
import jieba.analyse
import sys
import random
import time
reload(sys)
sys.setdefaultencoding( "utf-8" )

#一些全局参数
    #用户向量维数/关键字数量
n_v = 400
#f为阀值
f = 0.84



#得到测试集{user:[newsid]}
def get_testset():
    ts = r'C:\Users\zhx\Desktop\xwtj\test_set.csv'
    t = open(ts,'r')
    #所有用户的id集
    t_set = dict()
    #随机生成的用户id集
    r_set = dict()
    
    for line in t.readlines():
    
        a = line.strip().split(',')
        t_set[a[0]]=a[1]
   
    return t_set
    
#得到关键字列表[keywords]
def get_keywords():
    news = r'C:\Users\zhx\Desktop\xwtj\news.csv'
    content = open(news)
    fl=open('tn.txt','w')
    txt = ''
    keywords = []
    for line in content.readlines():
    # txt=txt+line.strip()+','
        txt = '%s, %s'%(txt,line.strip().split(',')[1])
    t = jieba.analyse.extract_tags(txt,n_v,allowPOS = ['n','vn','nr'])
    #t = jieba.analyse.textrank(txt,n_v,allowPOS = ['n','vn','nr'])
    for i in t:
        fl.write(i+',')
        keywords.append(i)
    return keywords

#输入参数：[关键词集],model=1(2),默认为1
#model=1时得到用户兴趣向量{user:voctor}
#model=2时得到用户浏览新闻id集{user:[newsid]}
def get_set(test_set,Keywords,model = 1):
    m = 3
    if model ==2:
        m = 1
    #userid = r'C:\Users\zhx\Desktop\xwtj\user_id.csv'
    usernews = r'C:\Users\zhx\Desktop\xwtj\test_data.csv'
    #关键词集
    keywords = Keywords
    #将用户id放进一个数组s_id        
    s_id = test_set.keys()
    #print s_id[:15]
    #构造字典存放用户{id：数据}，方便计算
    user_d = dict([(k,[])for k in s_id]) 
    nf = open(usernews,'r')
    #将用户看过的新闻标题存进字典user_d
    for line in nf.readlines():
        #t[0]是用户id，t[3]为新闻标题集,t[1]为新闻id集
        t= line.strip().split(',')
        #print t[0]
        if t[0] in s_id:
            #print 2
            #break
            user_d[t[0]].append(t[m])
        # else:
            # print 1
            # #break
    #当model = 2时，返回用户浏览新闻集{user:[news]}     
    if model ==2:
        return user_d
    #{用户：关键词集}
    for user in user_d.keys():
        #对标题集抽取关键词
        t = jieba.analyse.extract_tags(','.join(user_d[user]),allowPOS = ['n','vn','nr'])
        #t = jieba.analyse.textrank(','.join(user_d[user]),allowPOS = ['n','vn','nr'])
        
        #用户兴趣向量
        V_u = [0]*n_v
        #为向量赋值
        for i in t:
            if i in keywords:
                V_u[keywords.index(i)] = 1
            # else:
                # print 0
        #得到user:voctor
        user_d[user] = V_u
    return user_d

#计算用户间相似度
def similar(v1,v2):
    v1 = np.array(v1)
    v2 = np.array(v2)
    cos1 = np.sum(v1*v2)
    cos12 = np.sqrt(sum(v1*v1))
    cos22 = np.sqrt(sum(v2*v2))
    return cos1/(float(cos12*cos22))
    
#输入参数：｛user：兴趣向量｝得到用户的推荐候选集{user:[相似用户]}
def similar_users(userdict):

    ud = userdict 
    #惯例，用户id集[]
    uk = ud.keys()
    r_set = dict([(k,[])for k in uk])
    #一次对比，双方录入，减少循环量
    for i in range(len(uk)):
        if i == len(uk)-1:
            break
        for j in range(i+1,len(uk)):
            if j==len(uk)-1:
                break
            if(uk[i]!=uk[j]) and (sum(np.array(ud[uk[i]])*np.array(ud[uk[j]]))!=0):
                s = similar(ud[uk[i]],ud[uk[j]])
                #若满足条件则互相录入推荐列表
                if s > f:
                    r_set[uk[i]].append(uk[j])
                    r_set[uk[j]].append(uk[i])
            
    return r_set

#输入参数：｛user:[相似用户]｝得到推荐集｛user:[推荐新闻id集]｝
def get_result(userdict):
    #用户浏览新闻id集{user:[newsid]}
    Keywords = get_keywords()
    nset = get_set(test_set,Keywords,model = 2)
    tj_set = dict()
    for user in userdict.keys():
        t =[]
        for suser in userdict[user]:
            for new in nset[suser]:
                if (new not in nset[user]) and (new not in t):
                    t.append(new)
        tj_set[user] = t
    return tj_set

#输入推荐集{user:[推荐新闻id]}，测试集｛user：新闻id｝，计算并返回召回率
def rate_call(tj_set,test_set):
    #推荐新闻数
    n_tj=0
    for user in tj_set.keys():
        n_tj+=len(tj_set[user])
    #print n_tj
    #有效推荐数
    n_cr =0
    for user in test_set.keys():
        if test_set[user] in tj_set[user]:
            n_cr+=1
    #return n_cr/n_tj 
    #print n_cr
    p = float(n_cr)/n_tj
    c = float(n_cr)/10000
    f1 = 1/(1/p+1/c)
    return (n_tj,n_cr,p,c,f1)
    

#mark  = open(r'C:\Users\zhx\Desktop\xwtj\mark4.txt','w')
#mark.writelines( 'n_v:\tn_id:\tf:\tn_tj:\tn_cr:\tp:\tc:\tf1:\n')
print u'..............开始..............'
s_kw = get_keywords()  
test_set = get_testset()   
#初始时间
start_time = time.time()
data = rate_call(get_result(similar_users(get_set(test_set,s_kw))),test_set)
print data
#mark.writelines(txt)
#结束时间，顺便输出算法用时
end_time = time.time()
print end_time-start_time
#mark.close()
print u'...............结束................'
#end
#2.1版
#优化比较次数，不再重复生成关键字集
#加入计时功能
#推荐新闻去重复
#调整关键字提取，限定名称，动名词和人名
#正式运行版