# _*_ coding: utf-8 _*_
import numpy as np
import numpy 

#建立lda模型，生成文章-主题概率和主题-词汇概率


print "total reader start"		#读数据进内存
input_1=open('data.txt','ab+')
doc = []
for row in input_1:
    doc.append(row.strip())
input_1.close()
print "total reader over"


print "CountVectorizer reader start"	#转变成向量
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.feature_extraction.text import TfidfTransformer  

vectorizer = CountVectorizer()
x = vectorizer.fit_transform(doc)
# print(x)
analyze = vectorizer.build_analyzer()
weight = x.toarray()
word = vectorizer.get_feature_names()
output_1=open('wordset.csv','wb')		#词的向量输出到wordset中
output_1.write(str(word).replace('u',''))
output_1.close()
print "CountVectorizer reader over"

import lda
import lda.datasets

model = lda.LDA(n_topics=100, n_iter=1000,random_state=1)	#计算lda模型
model.fit(np.asarray(weight))     # model.fit_transform(X) is also available
topic_word = model.topic_word_    # model.components_ also works
#文档-主题（Document-Topic）分布
doc_topic = model.doc_topic_
a=doc_topic
topic_word = model.topic_word_
b=topic_word
numpy.savetxt('doc_topic.csv', a, delimiter = ',') #将得到的文档-主题分布保存
numpy.savetxt('topic_word.csv', b, delimiter = ',') #将得到的主题-词汇分布保存

