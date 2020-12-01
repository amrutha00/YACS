#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd
import json
import time
from datetime import datetime as d
import matplotlib.pylab as plt
import pprint


file_path=['worker1.log','worker2.log','worker3.log']


color=['b','g','r','c','m','y','k','w']

algos = dict()
algos['random'] = [dict(),dict(),dict()]
algos['round-robin'] = [dict(),dict(),dict()]
algos['least-loaded'] = [dict(),dict(),dict()]
countt = dict()
countt['random'] = [0,0,0]
countt['round-robin'] = [0,0,0]
countt['least-loaded'] = [0,0,0]


worker=[]
for path in file_path: 

    # data=open(path,'r')
    # logs={}

    # for line in data:
    #     col  = line.split(';')
    #     alg = col[-2]
    #     a=col[-1].strip()
    #     x=d.strptime(a,"%Y-%m-%d %H:%M:%S,%f")
    #     if(x not in logs.keys()):
    #         logs[x]=[]
    #     record = [col[1]] 
    #     logs[x].append(record)
    
    # final_list={}
    # curr=0
    # for i in logs.keys():
    #     x=logs[i]
    #     for j in x:
    #         col=j[0]
    #         col = col.split(' ')
    #         if(col[0]=='Started'):
    #             curr=curr+1
    #         else:
    #             curr= curr-1
    #     final_list[i]=curr
    # worker.append(final_list)
    # data.close()

    file = open(path, "r")
    for line in file.readlines():
        temp = line.split(";")
        alg = temp[-2]
        if (temp[1].split()[0] == 'Started'):
            if (temp[-1].split()[1] in algos[alg][int(path[-5]) - 1].keys()):
                # algos[alg][int(path[-5]) - 1][temp[-1].split()[1]] += 1
                countt[alg][int(path[-5]) - 1] += 1
                algos[alg][int(path[-5]) - 1][temp[-1].split()[1]] = countt[alg][int(path[-5]) - 1]
            else:
                # algos[alg][int(path[-5]) - 1][temp[-1].split()[1]] = 1
                countt[alg][int(path[-5]) - 1] = 1
                algos[alg][int(path[-5]) - 1][temp[-1].split()[1]] = 1
        else:
            if (temp[-1].split()[1] in algos[alg][int(path[-5]) - 1]):
                # algos[alg][int(path[-5]) - 1][temp[-1].split()[1]] -= 1
                countt[alg][int(path[-5]) - 1] -= 1
                algos[alg][int(path[-5]) - 1][temp[-1].split()[1]] = countt[alg][int(path[-5]) - 1]
    file.close()




for algo in algos:
    plt.figure(figsize=(8,8))
    for i in range(0,len(file_path)):
        x='worker' +str(i+1)
        plt.step(*zip(*sorted(algos[algo][i].items())),marker='o',color= color[i],label=x)
    plt.xlabel('Time')
    plt.ylabel('Running Tasks')
    plt.legend()
    plt.show() 
   

