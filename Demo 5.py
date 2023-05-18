#数据结构（Data Structure）
#存储大量数据的容器---->内置数据结构（Bulit-in Structure）
#概念基于现实生活中的原型
'''
1.列表
list = [val1,val2,val3,val4]
#2.字典
dict = {key1:val1, key2:val2} #均带有’:‘的key与value的对应关系组
#3.元组
tuple = (val1,val2,val3,val4)
#4.集合
set = {val1,val2,val3,val4}
元素均需要加逗号分开
'''

'''
##1.列表（List）
最显著的特征
A.每一个元素都是可变的
B.列表中的元素是有序的，咱就是说 每一个元素都有一个自己的位置
C.列表可以容纳Python中的任何对象
'''
'''
#Demo1 通过输入位置查询该位置所对应的值
Weekday = ['Monday','Tuesday','Wednesday','Thursday','Friday']
print(Weekday[0])

#Demo2 列表可以输入Python中所有对象
all_in_list = [
    1,                   #整数
    1.0,                 #浮点数
    'a word',            #字符串
    print(1),            #函数
    True,                #布尔值
    [1,2],                #列表
    (1,2),               #元组
    {'Key':'value'}      #字典
]
'''
'''
#Demo3 列表的增删改查
#a.增加：insert方法
fruit = ['Pineapple','Pear']
fruit.insert(1,'Grape') #insert方法，插入位置在指定位置之前
fruit.insert(3,'Orange') #insert方法，插入位置不存在则放在最后
fruit[0:0] = ['Orange']  #另一种插入方法
print(fruit)

#b.删除：remove方法
fruit = ['Pineapple','Pear','Orange']
fruit.remove('Orange')
print(fruit)
del fruit[0:2] #除remove外另一种方法
print(fruit) 

#c.改变：
fruit = ['Pineapple','Pear','Orange']
fruit[0] = 'Strawberry' #指定列表位置和新的元素
print(fruit)


#d.查找：列表的索引
#输入对应的位置就会返回在这个位置上的值
periodic_table = ['H','He','Li','Be','B','C','N','O','F','Ne']
print(periodic_table[0])
print(periodic_table[-2])
print(periodic_table[0:3])
print(periodic_table[-10:-7])
print(periodic_table[-10:])# 等价于[-10:0]
print(periodic_table[:9]) #等价于[0:9]

print(periodic_table['H']) #报错（X） 列表仅能接受数字索引
##列表也是一种数据结构
'''

'''
##2.字典（Dictionary）
#使用 名称-内容 进行数据构建----> 键(Key)——值(Value)（键值对）
#映射关系(mapping)
 
最显著的特征
A.字典中的数据以键值对[（Key）-（value）]的形式出现
B.逻辑上：键不能重复，值可以重复
C.键不可改变，无法修改；值可以改变，可以修改，可以是任何对象
'''
'''
#Demo 4 字典的特点
NASDAQ_code = {
    'BIDU':'BaiDu',
    'SINA':'Sina',
    'YOKU':'YouKu',
           
    'BIDU': #一个字典中的键与值不能脱离对方存在
    []:'a Test' #可变元素做键是不可以的
}
a = {'key':123,'key':123}
print(a)
#Key 和 value是一一对应的，Key是不可变的
#键值对不能有重复，重复后相同的键值只能出现一次。


#Demo5 字典的增删改查

NASDAQ_code = {'BIDU':'Baidu','SINA':'Sina'}
#a.增加:使用update方法
NASDAQ_code['YOKU'] = 'YouKu'  #增加单个元素
print(NASDAQ_code)
NASDAQ_code.update({'FB':'Facebook','TSLA':'Tesla'})#增加多个元素 update
print(NASDAQ_code)

#b.删除：使用del方法
del  NASDAQ_code['FB'] #删除使用del

#c.查找--->索引（index）
NASDAQ_code['TSLA']#字典和列表在索引的时候是一样的，都是使用的方括号

#d.其他
NASDAQ_code[1:4] #（X错误写法）字典不能够切片
'''
'''
##3.元组（Tuple）
#元组可视为一个不可修改的列表
#元组使用小括号
Letters = ('a','b','c','d','e','f','g','g')
#元组属性：索引
print(Letters[1:8])
'''
'''

##4.集合（Set）---->参考数学上的概念
#元素：无序、不重复、任意
#集合属性：添加、删除
'''
a_set = {1,2,3,4}
add = a_set.add(5)
print(a_set)
delete = a_set.discard(5)
print(a_set)
