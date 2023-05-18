##类与可口可乐

'''
#1.类的拓展理解

Demo 1.1 类的拓展理解
#Python中任何种类的对象都是类的实例
以下的几种类型都是内建模型，不需要实例化

obj1 = 1
obj2 = 'String'
obj3 = []
obj4 ={}
print(type(obj1))#<class 'int'>
print(type(obj2))#<class 'str'>
print(type(obj3))#<class 'list'>
print(type(obj4))#<class 'dict'>
'''

'''
#Demo1.2 类的拓展理解（2）

from bs4 import BeautifulSoup
soup = BeautifulSoup
print(type(soup)) #<class 'type'>
#在 BS后点Ctrl可以查看到该类型的完整定义
'''
#2.类的实践
#类背后承载的理念是OOP（面向对象）的编程理念和方式，
#目的是为了在大型项目中易于管理和维护代码质量。

#Demo2 手动生成版
'''
使用类的概念来编写一个日常的工具库导入到python的库中
在使用python处理数据或者是开发网站的时候，有时候会使用一些毫无意义的假数据，
现在制作一个填充用户假数据的工具
'''
'''
设计思路：
---------------------------------------------
父类：FakeUser
功能：
1.随机姓名
    a.单字名
    b.双字名
    c.无所谓，有名字即可
2.随机性别
-------------------------------------------
子类：SnsUser
功能：
1.随机数量的跟随者
    a.few
    b.lot
'''
'''
#part 1 词库整理
fn_path = 'first_name.txt'
ln_path = 'last_name.txt'
fn = []
ln1 = [] #单字名
ln2 = [] #双字名
with open(fn_path,'r',encoding='UTF-8')as f: #姓氏
    for line in f.readlines():
        fn.append(line.split(',')[0])#避免列表里有列表
#print(fn)


with open(ln_path,'r',encoding='UTF-8') as f: #姓名
    for line in f.readlines():
        if len(line.split(',')[0])==1:
            ln1.append(line.split(',')[0])
        else:
            ln2.append(line.split(',')[0])
print('=' * 70) #分割线

fn = tuple(fn)
ln1 = tuple(ln1)
ln2 = tuple(ln2)

'''
#数据是按照条来进行存储的，以”，“为一行的结束分隔
#将列表变成元组，目的是为了节省内存
'''
#part 2 定义父类FakeUser
import random
class FakeUser:
    def fake_name(self,one_word = False,two_words = False):
        if one_word:
            full_name = random.choice(fn) + random.choice(ln1)
        elif two_words:
            full_name = random.choice(fn) +random.choice(ln2)
        else:
            full_name = random.choice(fn)+random.choice(ln1+ln2)
        print(full_name)
    def fake_gender(self):
        gender = random.choice(['男','女','未知'])
        yield gender
        print(gender)
#part 3 定义子类
class SnsUser(FakeUser):
    def get_followers(self,few = True,a_lot = False):
        n = 0
        if few:
            followers = random.randrange(1,50)
            print(followers)
        elif a_lot:
            followers = random.randrange(200,10000)
            print(followers)
user_a = FakeUser()
user_b = SnsUser()
user_a.fake_name()
user_b.get_followers(few=True)


#Demo 3 使用生成器进行批量输出
#数据批量填充，涉及概念：生成器（generator）
#1.把print变成yield
#2.在每个定义前面加一层循环

#part 1 词库整理
fn_path = 'first_name.txt'
ln_path = 'last_name.txt'
fn = []
ln1 = [] #单字名
ln2 = [] #双字名
with open(fn_path,'r',encoding='UTF-8')as f: #姓氏
    for line in f.readlines():
        fn.append(line.split(',')[0])#避免列表里有列表
#print(fn)


with open(ln_path,'r',encoding='UTF-8') as f: #姓名
    for line in f.readlines():
        if len(line.split(',')[0])==1:
            ln1.append(line.split(',')[0])
        else:
            ln2.append(line.split(',')[0])
print('=' * 70) #分割线

fn = tuple(fn)
ln1 = tuple(ln1)
ln2 = tuple(ln2)

'''

'''
数据是按照条来进行存储的，以”，“为一行的结束分隔
将列表变成元组，目的是为了节省内存
'''
'''
#part 2 定义父类FakeUser
import random
class FakeUser:
    def fake_name(self,amount=1,one_word = False,two_words = False):
        n = 0
        while n <=amount:
            if one_word:
                full_name = random.choice(fn) + random.choice(ln1)
            elif two_words:
                full_name = random.choice(fn) +random.choice(ln2)
            else:
                full_name = random.choice(fn)+random.choice(ln1+ln2)
            yield (full_name)
            n +=1
    def fake_gender(self,amount =1):
        n = 0
        while n<=amount:
            gender = random.choice(['男','女','未知'])
            yield gender
            n +=1
#part 3 定义子类
class SnsUser(FakeUser):
    def get_followers(self,amount =1,few = True,a_lot = False):
        n = 0
        while n<=amount:
            if few:
                followers = random.randrange(1,50)
                print(followers)
            elif a_lot:
                followers = random.randrange(200,10000)
            yield followers
            n +=1
user_a = FakeUser()
user_b = SnsUser()
for name,gender in zip(user_a.fake_name(30),user_a.fake_gender(30)):
    print(name)
    print(gender)
    '''
'''
#3.安装自己的库
1>找到python安装目录，然后找到下面的site-packaes文件夹，然后将写的.py文件放进去（site-packages）
2>这个文件夹含有所有装的第三方库（√）
3>不清楚安装路径可以使用先导入再打印，具体是列表中的第四个（X只能显示C盘所在位置）
'''
#1.安装目录当初安装时如果未指定则在C盘，指定的话在指定的位置（venv\Lib\site-packages）
