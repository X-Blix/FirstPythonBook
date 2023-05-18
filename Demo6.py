#数据结构（Data Structure）应用
'''
##1.多重循环
#按照字母和日期进行排序(Sort,Zip)

#单个列表
A_list = [6,2,4,1,7,5,3]
print(sorted(A_list))
print(sorted(A_list,reverse = True)) #reverse默认参数，表示逆序整理

1. sort函数按照长短、大小、英文字母木顺序进行排序
2. sort函数并不改变列表本身，将列表复制后进行排序


#同时需要两个列表：
A_list = [1,2,3,4,5,6]
B_list = sorted(A_list,reverse=True)
for a,b in zip(A_list,B_list): #a对应A_list,B对应B_list
    print(b,'is',a)
'''


'''


2.推导式（List comprehension）&列表的解析式

import time
#Python3.8 不再支持 time.clock，但在调用时依然包含该方法；
#用 time.perf_counter() 替换
a = []
t0 = time.perf_counter()
for i in range(1,1000):
    a.append(i)
print(time.perf_counter() - t0 ,"seconds process time")

t0= time.perf_counter()
b = [i '|' for i in range(1,1000)]
#想要放在列表中元素|for循环
#放在for循环中的元素是元素本身。
print(time.perf_counter() - t0,"seconds process time")

##推导式的其他例子
#列表
a = [i**2 for i in range(1,10)] #放进i里面的元素是i的平方
b = [j+1 for j in range(1,10)] #放进j里面的元素是j+1的平方
c = [n for n in range(1,10) if n%2 == 0] #在1,10种为偶数的数
d = [letter.lower() for letter in 'ABCDEFGHIGK'] #把letter中的大写转小写
print(d)
#字典 
#字典要满足键-值对两个条件
e = {i:i+1 for i in range(4)} #i和i+1进行匹配，i里面的内容是i+1
f = {i:j for i,j in zip(range(1,6),'abcde')} #i中1-6 与j中 a-e匹配
g = {i : j.upper() for i,j in zip(range(1,6),'abcde') }#i中1-6 与j中 A-E匹配,a-e转为大写 
print(g)


##3.循环列表时获取元素的索引(！！！)
#使用Python中函数enumerate
letters =['a','b','c','d','e','f','g']
for num,letters in enumerate(letters):
    print(letters,'is',num+1)
'''

##4.综合项目:瓦尔登湖词频统计
import string
print(string.punctuation)

'''
#1.前置知识

lyric = 'The night begin to shine,the night begin to shine'
words = lyric.split()
print(words)
#使用spilt方法将字符串中每个单词分开

#2.程序运行版
f = open('Walden.txt',encoding = "utf-8")#以 utf-8 的编码格式打开指定文件
#输出读取到的数据
str = f.read().split() #使用split方法切割
for str in str:
    print('{}--{} times'.format(str,str.count(str)))
#关闭文件
f.close()

问题
1.有些字母带符号
2.同个单词区分了大写和小写
3.有些单词不止一次出现
'''

'''
import string

#3.程序完整版

path = open('Walden.txt','r',encoding='UTF-8')
with path as text:
    words = [raw_word.strip(string.punctuation).lower() for raw_word in text.read().split()]
    words_index = set(words)
    counts_dict = {index:words.count(index) for index in words_index}

for words in sorted(counts_dict,key=lambda x:counts_dict[x],reverse=True):
    print('{}-{} times'.format(words,counts_dict[words]))


#String.punctuation :包含所有标点符号（!"#$%&'()*+,-./:;<=>?@[\]^_`{|}~）
#去掉所有标点符号且把 大写转换成小写（字母预处理）
#用列表转换成集合-->去除所有重复的元素
#创建一个 单词为键（Key），出现频率(Value)为值的字典
#使用lambda表达式整理输出
'''