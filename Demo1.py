

'''
##函数部分 系统内带
Built-in Functions
A
abs() #一个会返回输入输入参数的绝对值的函数
aiter()
all()
any()
anext()
ascii()

B
bin()
bool()
breakpoint()
bytearray()
bytes()

C
callable()
chr()
classmethod()
compile()
complex()

D
delattr()
dict()
dir()
divmod()

E
enumerate()
eval()
exec()

F
filter()
float()
format()
frozenset()

G
getattr()
globals()

H
hasattr()
hash()
help()
hex()

I
id()
input() #可以接受用户输入的信息
int() #可以把其他类型转换成整数类型
isinstance()
issubclass()
iter()
L
len() #测量对象的长度 ？？？
list()
locals()

M
map()
max()
memoryview()
min()

N
next()

O
object()
oct()
open() #运行起来需要2个参数：文件路径名称+打开的方式
        #以write=方法文件写入内容
        #以close方法关闭文件
ord()

P
pow() #pow(X,Y) ==> X的Y次方 Y>1 --[开方] Y<1--[开根]
print()  #可以把输入的（对象）东西打印出来
        #没有，终端运行函数时可能输出空白（无数据）
        #sep是print函数的一个可选参数，默认是’ ‘
property()


R
range()
repr()
reversed()
round()

S
set()
setattr()
slice()
sorted()
staticmethod()
str()   #可进行类型转换,将其他数据类型类型转换为字符串类型
sum()   #对内容进行求和
super()

T
tuple()
type()

V
vars()

Z
zip()

_
__import__()
'''

##函数的定义和使用
'''
Demo 1 函数母版
#函数是编程中最基本的魔法，但同时一切的复杂又被隐含其中。
#Define a function named 'function' which has two arguments:arg1 and arg2,returns the result——something

def function(arg1,arg2):  #关键字 函数名(参数1，参数2) :
    return 'Something'    #缩进! 关键字 结果
##define(定义) == declaration(声明) ，表达相同的意思，缩写都可以表示 def 的意思
#缩进后面是一个语句块(block)，主要用来表示逻辑和代码的从属关系
'''

'''
#Demo2 编写一个函数，计算摄氏度转换成华氏度的值
#函数定义部分
def fahrenheit_converter(C): #摄氏度转换器
    fahrenheit = C * 9/5 +32 #将计算结果转为str类型才能与F相加
    return str(fahrenheit) + 'F' #return 作为一个关键字起到了控制函数返回值的作用
#函数调用部分(call)
C2F = fahrenheit_converter(35)  #使用摄氏度转换器将35摄氏度转换成华氏度，并且存放在一个叫C2F的变量里
print(C2F)
----------------------------------------
RESULT:
95F
---------------------------------------
'''

"""
#Demo3 在Demo2的基础上进行了改变，将‘return’改为了‘print’
#函数定义部分
def fahrenheit_converter(C):
    fahrenheit = C*9/5 +32
    print(str(fahrenheit)+'F') #print是一个函数，只是展示打印输出的结果
#？？？ 所有的函数都要有返回值(return)吗？ ==> 没有也没关系，return 是（optical）可选择的，在没有的时候函数也可以正常运行，只是返回值是None
#函数调用部分(call)
C2F = fahrenheit_converter(35) #
print(C2F)
----------------------------------------
RESULT:
 95F    #调用函数后返回的数值
 None  #此时C2F中所被返回的数值，为None的原因是没有关键字return
        #把根本不存在的“返回值”储存在一个变量中，实际上变量的赋值结果是None
 --------------------------------------
̶For Example:
 这就好比你对一个人喊了一声他的名字(call)，
 他只是“哎”的回了你一声，
 这是因为你并没有告诉他该做什么(return)
 """

'''
#Demo 4  课后练习题1：将g转换成kg的一个重量转换器
#函数定义部分
def weight_converter(G):
    KG = G * 0.001
    return str(KG)+'KG'
#函数调用(call)部分
input = input('Please input the weight in g:')
g = weight_converter(int(input)) # 需要进行类型转化
print(g)
'''
''' 
#Demo 5 课后练习题2：直角三角形已知两边，求斜边
#函数定义部分
def triangle_converter(A,B):#已知的两直角边，设为A，B
    C = pow(A,2)+pow(B,2) #A^2 + B^2 =C^2
    C = pow(C,0.5) # 对C开根
    return C
#函数调用(call)部分
a = int(input('Please input the first side :')) #将输入的值转换为int形
b = int(input('Please input the second side:')) #将输入的值转换为int形
c = triangle_converter(a,b)
print("The right triangle third side's length is {}".format(c))
'''

##传递函数的参数的方式

'''
#Demo 1 位置参数（positional argument）
#函数定义部分
def trapezoid_area(base_up,base_down,height): #构造函数的命名方法：名词+动词+器 
    return (base_up + base_down) * height * 1/2
#函数调用部分(call)
area=trapezoid_area(4,6,10) #调用函数时传递的参数和定义部分内容的值对应（数量一样？）
print(area) #要有打印输出，不然控制台输出空白（连None都没有）
'''
'''
#Demo 2 关键字参数（KeyWord argument）
#函数定义部分
def trapezoid_area(base_up,base_down,height): #参数好像都是名词？
    return((base_up+base_down)*height*1/2)
#函数调用(call)部分
area = trapezoid_area(base_up=4,base_down=6,height=10) #在每个参数后面附一个传入的值
#参数名称和参数值一一对应的这种传参方式称为关键字参数（argument）
print(area)
'''

'''
#Demo 3 :位置参数和关键字参数举例说明（举一个栗子）
-----------------------------------------------------------------
**有关位置参数和关键字参数的区别，用一个例子说明：（摘抄书里面的）：
*去餐厅预约与就餐流程
1.找到预约的座位：[人]按照（姓名）的方式传入预定的座位-->关键词参数
2.上菜就餐：[食物]按照（座位号）的方式传入桌子-->位置传递参数
(存疑：)姓名是关键字，座位号是位置传递吗？ ==>是的，类似先有菜单再把菜放上去这样的
--------------------------------------------------------------------
'''

'''
#Demo 4 根据Demo3的举例说明进行举例说明（举一个含树栗子）
#函数定义部分：
def restrurant_reservation(name):#位置预定器
     if name =='Xblix':
          return str('座位号是10')
#函数调用部分（call）
name = input('Please input your name:')
position = restrurant_reservation(name)
print(position)

#函数定义部分
def up_desk(position): #上菜器
     meat = ' 肉类 '
     vegetable = ' 蔬菜类 '
     soup = ' 汤类 '
     if position == '10':
          return meat + soup + vegetable
desk = input('Please input your desk:')
foods = up_desk(desk)
print(foods)
#好像有一点问题，不过能运行出来
'''

'''
#Demo 5
#有关函数的位置参数和关键词参数调用的其他形式：
#函数定义部分
def trapezoid_area(base_up,base_down,height): #参数好像都是名词？
    return((base_up+base_down)*height*1/2)
#函数调用(call)部分
#area1 = trapezoid_area(height=3 ,base_down = 2,base_up = 1 ) #第一种
#调用函数时位置和参数里面定义的位置并不是一一对应的，这种叫做反序传入，但是因为是关键字函数，所以函数还是能正常运行的
#关键字函数指的是在调用的时候赋值的方式
#area2 = trapezoid_area(height=3,base_down=2,1)#第二种，这是错误的，会报错
#这种类比第一种，也是反序传入，但是第三个参数默认是height的位置却在之前被传入了其他值，这样会报错
#area3 = trapezoid_area(base_up=1, base_down = 2,3) #第三种，前两个是以关键词传入，第三个是位置参数传入
#书上说可以正常运行，但实际上运行不出来..
#area4 = trapezoid_area(1, 2,height=3) #第四种，前两个是位置参数，第三个是关键字函数，这种函数是可以正常运行的。
#print(area4)
'''

'''
#Demo 6 在上个函数的基础上，给一组变量复制后再调用，并观察出现的情况
#函数定义部分
def trapezoid_area(base_up,base_down,height):
    #参数名称在定义函数（名称）的时候同时被定义，指导我们传入参数，并提供与函数使用的相关上下文。
    return (base_up+base_down)*height*1/2
#函数调用部分
base_up = 1       #命名的一个变量
base_down=2       #命名的一个变量
height = 3        #命名的一个变量
area = trapezoid_area(height,base_down,base_up)#答案是2.5
#area = trapezoid_area(height=3,base_down=2,base_up=1) = #(3+2)*1*1/2
#--------------------------------------------------
说明：在函数调用部分重新赋值了3个变量，需要将变量的位置和定义时候的位置相对应。即变量的命名
#顶i是变量对应，变量与参数以位置对应
'''

'''
#Demo 7 举例说明变量和参数的关系？
def flashlight(battery1,battery2):
    return 'Light'
nanfu1 = 600#是变量，也是满足能够满足传入函数flashlight函数的参数
nanfu2 = 600 #传入后替代了原有的battery1，battery2，且传入方式是位置参数传入
flashlight(nanfu1,nanfu2)
print(flashlight(battery1=nanfu1,battery2=nanfu2))
----------------------------------------------------
好像明白一点了,就是要给参数传一个变量的值进行改变
'''
'''
Demo 8:参数定义和调用要一一对应
参数：一开始设定好的参数，在调用的时候缺一不可。==>不然可能会报错
举一个栗子：
trapezoid_area(1,2) ==>typeArea:trapezoid_area()missing 1 required positional argument:'height'
'''
'''
# Demo 9 默认参数（引入）
print('  *', ' * *', '* * *', '  |  ')  # 一行
print('  *', ' * *', '* * *', '  |  ', sep='\n')  # 多行
# sep是print函数的一个可选参数，默认值为’ ‘。'\n'是传入的新参数，意为’换行‘
'''
'''
#Demo 10 默认参数（举栗子）
def trapezoid_area(base_up,base_down,height = 3): #在定义参数的时候给参数赋值
    return (base_up+base_down)* 1/2 * height
area = trapezoid_area(1,2) #已经给height设立过默认参数的值，只需要赋值两个变量就可
area = trapezoid_area(1,2,height=15) # 默认赋值若需要更改，在参数调用里面进行更改就可以了
print(area)
----------------------------------------------------------
requsets.get(url, headers=header) #请求网站时header
img.savr(img_new,img_format,quality = 100 )#照片加水印默认质量100
#需要导入一些库
----------------------------------------------------------
'''


'''
#Demo 11 函数的综合运用--敏感词过滤器（书上的栗子）

#0.前置知识
file = open('D:/Py_Project/Py_Project1.txt','w') #使用open函数打开一个txt文件，使用的方法叫write
#方法是函数的一种，只是位置不同，使用方法非常的相似。
file.write('Hello World')
#--------------------------

#1.创立一个txt文件，在指定位置叫指定的名字
def text_create(name,msg): #定义函数器名称和参数名称
    path = "D:/Py_Project/"+name+'.txt'    #要用/不能用\ #定义完整name路径
    file = open(path,'w') #调用open函数打开文件
    file.write(msg) #以write方法向文件里写入内容
    file.close() #以close方法关闭文件
    print('All progress have been finished') #打印证明上面的语句已被执行
    return path #一个可有可无的返回值
title = input('Please input the txt titie:')
message = input('Please input the txt massage:')
total = text_create(title,message)
#print(total)
#--------------------------

#2.定义一个函数作为敏感词过滤器
def text_filter(string,censored_word,changed_word):
    return string.replace(censored_word,changed_word)
string = message
censored_word = string
changed_word = input('input the changed word:')   #加亿点点细节
result = text_filter(string,censored_word,changed_word)
print(result) #打印清洗后的数据
#--------------------------

#3.将新的数据放到原来的txt里
def censored_text_create(result=result,total = total):  #total里面是新的path路径，result里面是输入的新的结果
    file_new = open(total,'w')
    file_new.write(result)
    file_new.close()
    print('Refresh progress have been finished')
    return file_new
censored_text_create(result,total)   #Debug很好用，finish！
#----------------------
'''

'''
举例子，借助数学计算阐述函数的运作方式。（梯形面积计算器）
数学相关问题解决会用到的符号：
+  加：两个对象相加                   A + B output result : 30
-  减：得到附属或是一个数减去另一个数    A - B output result : -10  
*  乘：两个数相乘或是返回一个被重复若干次的字符串      A * B output result : 200
/  除：返回一个被重复小于一若干的字符串       B / A output result : 2
%  取模：返回除法的余数       B % A output result : 0
**  幂：返回x的y次幂       A**B output result :10^20
'''
print(10**20)