# -*- coding: utf-8 -*-  
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
import matFont

def createDataSet():
	group = array([[1.0, 1.1], [1.0, 1.0], [0, 0], [0, 0.1]])
	labels = ['A', 'A', 'B', 'B']
	return group, labels

# print createDataSet()
def classify0(inX, dataSet, labels, k):
	dataSetSize = shape(dataSet)[0]
	diffMat = tile(inX, (dataSetSize, 1)) - dataSet
	sqDiffMat = diffMat**2
	sqDistances = sqDiffMat.sum(axis=1)
	distances = sqDistances**0.5
	# 每个元素的排序后的序号
	sortedDistIndicies =  distances.argsort()
	classCount = {}
	for i in range(k):
		# 计算k个数据的概率
		voteIlabel = labels[sortedDistIndicies[i]]
		classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
	sortedClasscount = sorted(classCount.iteritems(), key=operator.itemgetter(1), reverse=True)
	# 概率最高的一个
	return sortedClasscount[0][0]

def file2matrix(filename):
	with open(filename, 'r') as fr:
		arrayOLines = fr.readlines()
		numberOfLines = len(arrayOLines)
		returnMat = zeros((numberOfLines, 3))
		classLabelVector = []
		index = 0
		for line in arrayOLines:
			line = line.strip()
			listFromLine = line.split('\t')
			returnMat[index,:] = listFromLine[0:3]
			classLabelVector.append(int(listFromLine[-1]))
			index += 1
		return returnMat, classLabelVector

matFont.set_matplot_zh_font()
datingDataMat,datingLabels = file2matrix('datingTestSet2.txt')
fig = plt.figure('datingDataMat')
ax = fig.add_subplot(111)
ax.set_title(u'散点图')
ax.set_xlabel(u'玩视频游戏所耗时间百分比')
ax.set_ylabel(u'每周消费的冰激凌公升数')
ax.scatter(datingDataMat[:,1], datingDataMat[:,2], 20.0 * array(datingLabels), 15.0 * array(datingLabels))
plt.show()
