# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:53:32 2018

@author: shenliang-006
"""

#decision tree

from math import log
import operator

def calcShannonEnt(dataSet):  # 计算数据的熵(entropy)
    numEntries=len(dataSet)  # 数据条数
    labelCounts={}
    for featVec in dataSet:
        currentLabel=featVec[-1] # 每行数据的最后一个字（类别）
        if currentLabel not in labelCounts.keys():
            labelCounts[currentLabel]=0
        labelCounts[currentLabel]+=1  # 统计有多少个类以及每个类的数量
    shannonEnt=0
    for key in labelCounts:
        prob=float(labelCounts[key])/numEntries # 计算单个类的熵值
        shannonEnt-=prob*log(prob,2) # 累加每个类的熵值
    return shannonEnt

def createDataSet1():    # 创造示例数据
    dataSet = [['高','长', '粗', '男'],
               ['高','短', '粗', '男'],
               ['矮','短', '粗', '男'],
               ['矮','长', '细', '女'],
               ['矮','短', '细', '女'],
               ['高','短', '粗', '女'],
               ['矮','长', '粗', '女'],
               ['矮','长', '粗', '女']]
    labels = ['身高','头发','声音']  #两个特征
    return dataSet,labels

def splitDataSet3(dataSet,axis,value): # 按某个特征分类后的数据
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            print(featVec[axis])
            print(featVec)
            reducedFeatVec =featVec[:axis]
            print(reducedFeatVec)
            reducedFeatVec.extend(featVec[axis+1:])
            print(reducedFeatVec)
            retDataSet.append(reducedFeatVec)
    return retDataSet

def splitDataSet(dataSet,axis,value): # 按某个特征分类后的数据
    retDataSet=[]
    for featVec in dataSet:
        if featVec[axis]==value:
            reducedFeatVec =featVec[:axis]    #
            reducedFeatVec.extend(featVec[axis+1:])
            retDataSet.append(reducedFeatVec)
    return retDataSet

def splitDataSet2(trainData,index,value):
    subData = []
    for trainLine in trainData:
        if trainLine[index]==value:
            reducedFeatVec = []
            for i in range(0,len(trainLine),1):
                if i==index:
                    continue
                reducedFeatVec.append(trainLine[i])
            subData.append(reducedFeatVec)
    return subData

def chooseBestFeatureToSplit(dataSet):  # 选择最优的分类特征
    numFeatures = len(dataSet[0])-1
    baseEntropy = calcShannonEnt(dataSet)  # 原始的熵
    bestInfoGain = 0
    bestFeature = -1
    for i in range(numFeatures):
        featList = [example[i] for example in dataSet]
        uniqueVals = set(featList)
        newEntropy = 0
        for value in uniqueVals:
            subDataSet = splitDataSet(dataSet,i,value)
            prob =len(subDataSet)/float(len(dataSet))
            newEntropy +=prob*calcShannonEnt(subDataSet)  # 按特征分类后的熵
        infoGain = baseEntropy - newEntropy  # 原始熵与按特征分类后的熵的差值
        if (infoGain>bestInfoGain):   # 若按某特征划分后，熵值减少的最大，则次特征为最优分类特征
            bestInfoGain=infoGain
            bestFeature = i
    return bestFeature

def majorityCnt(classList):    #按分类后类别数量排序，比如：最后分类为2男1女，则判定为男；
    classCount={}
    for vote in classList:
        if vote not in classCount.keys():
            classCount[vote]=0
        classCount[vote]+=1
    sortedClassCount = sorted(classCount.items(),key=operator.itemgetter(1),reverse=True)
    return sortedClassCount[0][0]

def createTree1(dataSet,labels):
    classList=[example[-1] for example in dataSet]  # 类别：男或女
    if classList.count(classList[0])==len(classList):
        return classList[0]
    if len(dataSet[0])==1:
        return majorityCnt(classList)
    bestFeat=chooseBestFeatureToSplit(dataSet) #选择最优特征
    bestFeatLabel=labels[bestFeat]
    myTree={bestFeatLabel:{}} #分类结果以字典形式保存
    del(labels[bestFeat])
    featValues=[example[bestFeat] for example in dataSet]
    uniqueVals=set(featValues)
    for value in uniqueVals:
        subLabels=labels[:]
        myTree[bestFeatLabel][value]=createTree(splitDataSet(dataSet,bestFeat,value),subLabels)
    return myTree

def createTree(dataSet,labels):
    labellist=[example[-1] for example in dataSet]
    
    if labellist.count(labellist[0])==len(labellist): #set(labellist)==labellist[0]:
        return labellist[0]
    if len(dataSet[0])==1:  #   #<2
        return count(labellist)
    
    best=chooseBestFeatureToSplit(dataSet)
    bestfeature=labels[best]
    del(labels[best])
    newlabels=labels[:]
    
    Tree={bestfeature:{}}
    
    feature=[example[best] for example in dataSet]
    setfeature=set(feature)
    
    for fe in setfeature:
                
        Tree[bestfeature][fe]=createTree(splitDataSet(dataSet,best,fe),newlabels)

if __name__=='__main__':
    dataSet, labels=createDataSet1()  # 创造示列数据
    print(createTree(dataSet, labels))  # 输出决策树模型结果
