# -*- coding: utf-8 -*-
from numpy import *
import operator
import matplotlib
import matplotlib.pyplot as plt
import matFont
import os

def create_data_set():
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
    sortedDistIndicies = distances.argsort()
    classCount = {}
    for i in range(k):
        # 计算k个数据的概率
        voteIlabel = labels[sortedDistIndicies[i]]
        classCount[voteIlabel] = classCount.get(voteIlabel, 0) + 1
    sortedClasscount = sorted(classCount.iteritems(),
                              key=operator.itemgetter(1), reverse=True)
    # 概率最高的一个
    return sortedClasscount[0][0]


def autoNorm(dataSet):
    minVals = dataSet.min(0)
    maxVals = dataSet.max(0)
    ranges = maxVals - minVals
    normDataSet = zeros(shape(dataSet))
    m = dataSet.shape[0]
    normDataSet = dataSet - tile(minVals, (m, 1))
    normDataSet = normDataSet / tile(ranges, (m, 1))
    return normDataSet, ranges, minVals


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
            returnMat[index, :] = listFromLine[0:3]
            classLabelVector.append(int(listFromLine[-1]))
            index += 1
        return returnMat, classLabelVector

def drawScatter(datingDataMat):
    matFont.set_matplot_zh_font()
    fig = plt.figure('datingDataMat')
    ax = fig.add_subplot(111)
    ax.set_title(u'散点图')
    ax.set_xlabel(u'玩视频游戏所耗时间百分比')
    ax.set_ylabel(u'每周消费的冰激凌公升数')
    ax.scatter(datingDataMat[:, 1], datingDataMat[:, 2],
           20.0 * array(datingLabels), 15.0 * array(datingLabels))
    plt.show()


def img2vector(filename):
    returnVector = zeros((1, 1024))
    with open(filename, 'r') as fr:
        for i in range(32):
            lineStr = fr.readline()
            for j in range(32):
                returnVector[0, 32 * i + j] = int(lineStr[j])
        return returnVector

def datingClassTest():
    hoRatio = 0.15
    datingDataMat, datingLabels = file2matrix('datingTestSet2.txt')
    normMat, ranges, minVals = autoNorm(datingDataMat)
    m = normMat.shape[0]
    numTestVecs = int(m * hoRatio)
    errorCount = 0.0
    print numTestVecs
    for i in range(numTestVecs):
        classifierResult = classify0(
            normMat[i, :], normMat[numTestVecs:m, :], datingLabels[numTestVecs:m], 3)
        print '%d the classifier came back with:%d, the real answer is:%d' % (i, classifierResult, datingLabels[i])
        if (classifierResult != datingLabels[i]):
            errorCount += 1.0
    print 'the total error rate is:%f' % (errorCount / float(numTestVecs))

def handwritingClassTest():
    # 加载训练数据
    hwLabels = []
    trainingFileList = os.listdir('trainingDigits')
    m = len(trainingFileList)
    trainingMat = zeros((m, 1024))
    for i in range(m):
        fileNameStr = trainingFileList[i]
        fileStr =  fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        hwLabels.append(classNumStr)
        trainingMat[i, :] = img2vector('trainingDigits/%s' % fileNameStr)
    # 加载测试数据
    testFileList = os.listdir('testDigits')
    errorCount = 0.0
    mTest = len(testFileList)
    for i in range(mTest):
        fileNameStr = testFileList[i]
        fileStr =  fileNameStr.split('.')[0]
        classNumStr = int(fileStr.split('_')[0])
        vectorUnderTest = img2vector('testDigits/%s' % fileNameStr)
        classifierResult = classify0(vectorUnderTest, trainingMat, hwLabels, 3)
        print '%d the classifier came back with:%d, the real answer is:%d' % (i, classifierResult, classNumStr)
        if (classifierResult != classNumStr):
            errorCount += 1.0
    print 'the total error rate is:%f' % (errorCount / float(mTest))

# 约会人群分类
# datingClassTest()

# 手写识别
handwritingClassTest()