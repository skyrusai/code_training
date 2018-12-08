# -*- coding: utf-8 -*-
"""
Created on Wed Nov 14 10:53:32 2018
https://blog.csdn.net/csqazwsxedc/article/details/65697652
@author: shenliang-006
"""
from math import log
import operator

def createDataSet1():    # 创造示例数据
    dataSet = [['长', '粗', '男'],
               ['短', '粗', '男'],
               ['短', '粗', '男'],
               ['长', '细', '女'],
               ['短', '细', '女'],
               ['短', '粗', '女'],
               ['长', '粗', '女'],
               ['长', '粗', '女']]
    labels = ['头发','声音']  #两个特征
    return dataSet,labels

def createDataSet2():    # 创造示例数据
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

def calcShannonEnt(dataSet):
#    len(dataSet)
#    len(dataSet[0])
    labelcounts={}
    
    for data in dataSet:
        fealabel=data[-1]
        if fealabel not in labelcounts.keys():
            labelcounts[fealabel]=0
        labelcounts[fealabel]+=1
    shannonEnt=0
    for key in labelcounts:
        ent=float(labelcounts[key])/len(dataSet)
        shannonEnt -=ent*log(ent,2)
    return shannonEnt


    
def splitDataSet(dataSet,axis,value):
    subdata=[]
    for data in dataSet:
        if data[axis]==value:
            
            sub =data[:axis]#### axis 这列不加入
            sub.extend(data[axis+1:])
            subdata.append(sub)
    #print(subdata)
    
    return subdata

def chooseBestFeatureToSplit(dataSet):  # 选择最优的分类特征
    best=-1
    bestminus=-1
    num=calcShannonEnt(dataSet)
    for i in range(len(dataSet[0])-1):
        featureList=[m[i] for m in dataSet]
        uniquefeature=set(featureList)
        ent=0
        for feature in uniquefeature:
            
            subDataSet=splitDataSet(dataSet,i,feature)
            prob=len(subDataSet)/float(len(dataSet))
            ent +=prob*calcShannonEnt(subDataSet)
        
        minus=num-ent
        
        if bestminus<minus:
            bestminus=minus
            best=i
            
        
    return best
    
def count(labellist):
    list={}
    for label in labellist:
        if label not in list:
            list[label]=0
        list[label]+=1
    Max=sorted(list.items(),key=operator.itemgetter(1),reverse=True)
    return Max[0][0]#  返回key


def createTree(dataSet,labels):
    labellist=[example[-1] for example in dataSet]
    
    if  labellist.count(labellist[0])==len(labellist): #   set(labellist)==labellist[0]:#
        return labellist[0]
    if len(dataSet[0])<2:  #   #==1
        return count(labellist)
    
    best=chooseBestFeatureToSplit(dataSet)
    bestfeature=labels[best]
    
    Tree={bestfeature: { }}
    
    feature=[example[best] for example in dataSet]
    setfeature=set(feature)
    
    del(labels[best])
    
    for fe in setfeature:
        newlabels=labels[:]           
        Tree[bestfeature][fe]=createTree(splitDataSet(dataSet,best,fe),newlabels)

    return Tree


if __name__=='__main__':
    dataSet, labels=createDataSet1()  # 创造示列数据
    print(createTree(dataSet, labels))  # 输出决策树模型结果

    dataSet, labels=createDataSet2()  # 创造示列数据
    print(createTree(dataSet, labels)) 

    dataSet, labels=createDataSet2()
    tree=createTree(dataSet, labels)
    import json
    print(json.dumps(tree,indent=5,ensure_ascii=False,sort_keys=True))