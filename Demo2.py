##循环与判断
#逻辑判断
#逻辑判断是编程语言中最有趣的地方

#布尔类型
#0.前置知识
#Logic  Decision bascic method —— if-else structure
#Logic Decision basic principle ——Boolean Type
#' == ' 在python 里是判断两个量是否相等的
#' = ' 在python里是赋值
'''
Demo 0 Python Console&Python Terminal
Python Console 与 Python Terminal的区别：
1.Python Console:Python交互式控制台，可以运行程序运算
2.Python Terminal:Pyhon终端，可以进行安装包下载
'''

###1.布尔(Boolean)和比较运算(Comparsion)
'''
##布尔类型（Boolean Type）——Ture&Flase
    #1.布尔类型的数据只有两种：True&Flase,现实对应：真&伪 计算机对应：1&0
    #2.逻辑是一种进行判断的方法
##布尔表达式(Boolean Expressions)——返回值是布尔值的表达式
    #返回值是True&False
    #产生布尔表达式的表达方式有很多种
'''

'''
#Demo 1:在Python Console里面运行以下语句 (Boolean Expressions)
    1 > 2 #False
    1 < 2 < 3 #True
    42 != '42' #True
    'Name' == 'name' #False
    'M' in 'Magic' #True
    number = 12   #  <input> : 1 :  SyntaxWarning: "is" with a literal. Did you mean "=="?
    number is 12 #True 
'''



'''
#2.比较运算符（Comparison Operatprs）
-----------------------------------
#(1)| a < b  | less than
Returns True if a is less than b,False otherwise
-----------------------------------
(2)| a > b  |greater than
#Retrns True if a is greater than b ,False otherwise
-----------------------------------
(3)| a <= b  | less than or equal to
Returns True if a is less than or equal to b,False otherwise 
-----------------------------------
(4)|a >= b  |greater than oe equal to
Returns True if a is greater than oe equal to b,False otherwise 
-----------------------------------
(5)|a != b  | not equal to
Returns True if a is not equal to b,False otherwise
-----------------------------------
(6)|a == b  | equal to
Returns True if a is  equal to b,False otherwise
-----------------------------------
成立时返回True,不成立时返回False
查找快捷键：Ctrl+F 
替换快捷键：Ctrl+R
'''

'''
#Demo 2 比较的其他类型

#多条件的比较（先给变量赋值，然后在多条件下比较大小）
middle = 5
1 < middle < 10 #True

#变量的比较（将运算结果储存在不同的变量中，然后比较两个变量的大小）
two = 1 + 1
three = 1 + 3
two < three #True

#字符串的比较（对比左右字符串是否一样）
# Python能够区分大小写，大小写是不同的变量
'Eddie Van Helen' == 'eddie van helen' #False

#函数结果的比较（先调用函数进行计算后再进行比较）
#abs()是一个计算绝对值的变量
abs(-10) > len('length of this word') #False
'''

'''
##比较类型中的其他问题

#不同类型的对象比较：
    1.不同类型数据进行比较，只能使用'=='&'!='
    2.不同类型数据使用'<、>、 <=、 >='都会报错
    *不同类型间的数据只有 "等于""不等于"两种关系
    3.浮点型和整数型的数据可以进行比较（可以使用所有的比较运算符号）
    
#布尔类型的对象互相进行比较
1.True = 1 & False = 0
# !=的其他写法是<> ,这两种写法都是相同的

#Demo 3 不同类型的数据进行比较
42 > 'the answer' #TypeError: '>' not supported between instances of 'int' and 'str'
42 == 'the answer'#False
42 != 'the answer'#True

5.0 == 5 #True
3.0 > 1 #True

#Demo 4 布尔类型的数据进行比较
True > False #True
True + False > False +False #True

#Demo 5 != 的另一种写法<>
a = 1
b = 2
a <> b #(X)SyntaxError: invalid syntax
a != b #(√)
'''

'''
###成员运算符&身份运算符（Membership Operators & Identify Operators）
#in & is
#in:把in放在两个对象中间的含义是：测试前者是否在后者的集合中

#集合类型：列表(List) 列表是非常好用的一种数据结构

#Demo 1 创建一个列表
 #Album = [] #空列表
 Album = [' Black Star','Davide Bowie',25,True] #列表赋值
 Album.append('New Song') #使用append方法给列表附加新的值
 A = Album[0] #列表的索引，类似字符串索引
 B = Album[-1] #列表的索引，类似字符串索引
 'Black Star' in Album #in测试某个值是否在某个集合中（只要有从一堆中找到一个的性质就可以用）
'''


'''
#is & is not 表示身份鉴别（Identify Operator）
#in & not in 表示归属关系（Membership Operator）
#Python 中任何一个对象都要满足身份(Identify')\类型（Type）\值(Value)三个特点

Demo 2 使用is 操作符进行身份比对
the_Eddie = 'Eddie'
name = 'Eddie'
the_Eddie = name
the_Eddie is name  # (True)
'''

'''
Demo 3 其他对象判断布尔值
#除了0、None、空的数列与集合 布尔值为False,其他都为True
bool(0) #False
bool([]) #False
bool('') #False
bool(False) #False
bool(None) #False

#可以给某个变量设定值为None
Nothing = None
'''

###布尔运算符（Boolean Operators）
#and,or 用于处理复合条件下的判断 （同时满足多个条件）
'''
运算符（Comparison Operatprs）
-----------------------------------
(1) Not X
如果X是True，则返回False，否则返回True
-----------------------------------
(2)X and Y 
and 表示“并且”,如果x和y都是True,则返回True；
如果x和y有一个是False，则返回False。
-----------------------------------
(3) X or Y
or 表示“或者”，如果 X 和 Y 其中有一个是True，则返回 True；
如果X和Y都是False，则返回False
-----------------------------------
'''

'''
Demo 4 
1 <3 and 2<5 #True
1 <3 and 2>5 #False
1<3 or 2>5 #True
1>3 or r2>5 #False
'''

