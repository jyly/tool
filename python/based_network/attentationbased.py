#-*-coding:utf-8-*-
"""
@author:taoshouzheng
@time:2019/2/14 8:05
@email:tsz1216@sina.com
"""

import numpy as np
from keras.layers import Input, Dense
from keras.layers import multiply
from keras.models import Model
import matplotlib.pyplot as plt
# 参数定义
BATCH_SIZE = 12800		# 批次大小
TIME_STEP = 6		# 样本特征数量
DEMESION = 10		# 每个特征的维度
OUTPUT_LEN = 3		# 标签的维度
SAMPLE_NUM = 300000		# 样本数量
ONE_HOT = False		# 是否独热编码
np.random.seed(1)		# 结果重复性设置
# 创建样本数据
def create_data(n):
	"""
	:param n: 样本数量
	:return: 样本的特征及标签以及对应的one-hot编码
	"""
	# 预定义特征
	X = np.zeros((n, TIME_STEP), dtype='int32')		# np.zeros返回一个给定形状和类型的用0填充的数组
	# 预定义标签
	Y = np.zeros((n, ), dtype='int32')
	# one_hot编码部分
	for i in range(n):		# 遍历所有样本
		# 特征
		feature = np.random.randint(0, 10, size=TIME_STEP)		# numpy.random.randint(low, high size=n)返回一个长度为n的每个元素位于low和high之间的整数数组
		x1 = feature[0] * 100 + feature[1] * 10 + feature[2]		# 第一个三位数
		x2 = feature[3] * 100 + feature[4] * 10 + feature[5]		# 第二个三位数
		# 标签
		label = abs(x1 - x2)		# 两个三位数的差的绝对值
		label_zfill = [int(s) for s in str(label).zfill(OUTPUT_LEN)]		# zfill()返回指定长度的字符串，原字符串右端对齐，左端填充0
		X[i] = feature
		Y[i] = label
	return {
		'X': X / 10,
		'Y': Y / 1000,
	}

# 定义带有注意力的多层感知机模型
def build_model():
	inputs = Input(shape=(TIME_STEP, ))
	# 注意力层，计算输入中每个元素的注意力分布
	attention_prob = Dense(TIME_STEP, activation='relu')(inputs)
	# 根据计算的注意力分布对每个输入元素进行加权
	attention_encoding = multiply([inputs, attention_prob])		# 对应位置元素相乘
	print(attention_encoding)
	encoding_a = Dense(TIME_STEP, activation='relu')(attention_encoding)
	encoding_b = Dense(int(TIME_STEP / 2), activation='relu')(encoding_a)
	output = Dense(1)(encoding_b)		# 回归问题，不需要将预测结果进行分类转换，所以输出层不需要设置激活函数，直接输出数值
	# 函数式模型
	model = Model(inputs=[inputs], output=output)
	att_model = Model(inputs=inputs, output=attention_prob)
	print(attention_prob)
	return model, att_model, inputs, output, attention_prob
model, att_model, inputs, outputs, attention_prob = build_model()		# 调用函数，返回模型、输出值以及注意力分布
data = create_data(SAMPLE_NUM)		# 调用函数生成样本

print(data['X'][0])
print(data['Y'][0])
# 编译模型
model.compile(loss='MSE', optimizer='Adam', metrics=['mse'])
# 训练模型
model.fit([data['X']], data['Y'], batch_size=2048,epochs=10)
# 可视化注意力分布
model.save_weights('./model.h5')
# model.load_weights('./model.h5')

att_dis = att_model.predict(data['X'])
avg_attention = np.mean(att_dis, axis=0)
avg_attention = avg_attention / np.sum(avg_attention, axis=0)
# 以柱状图的形式进行可视化
plt.bar(range(1, 7), avg_attention)
plt.show()
print(avg_attention)