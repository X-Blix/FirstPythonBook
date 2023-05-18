##变量与字符串部分
'''
Demo 1 可以使用file函数，打开D盘，往相关的文件里写入数据
file = open('D:Py_Project', 'w')
file.write("flie = open('D:\Py_project','w')")

'''
'''
demo 2 字符串可以进行相加，字符串是被引号包裹起来的一串
person_name = input('Please input  his name:')
person_instrument = input('Please input what is his instrument:')
person_position = input('Please input where he is:')

person_sum = person_name + ' is playing '+person_instrument + ' in the '+person_position
print(person_sum)
'''
'''
###Demo 3 不同数据类型无法相加，可以使用type判断数据类型

a = 1
b = 'hello'
###print(a+b)
print(type(a))
print(type(b))
'''
'''
#Demo4 可以使用类似int()函数的函数，将数据类型化为一类进行相加
a = 1
b = '2'
c = int(b)
#print(type(c))
sum_a_b = a+c
print(sum_a_b)
'''
'''
#Demo 5 字符串可以进行相×的操作
Word = '123456'
Words = Word * 3
print(Words) 
'''
'''
#Demo 6 字符串可以进行复杂计算
word = 'a long word'
#print(len(word))
sum = 5
word_all = (len(word)-sum)*2
print(word_all)'''
'''
#Demo 7 字符串可以进行索引等操作
String = 'MA-QWERT-UY-ZANY'
a = String[0] #字符串截取正数从0开始
b = String[-1] # 字符串倒数是从-1开始
c = String[0:-1] #字符串的全部内容
d = String[1:6] #字符串正数位置1到位置6，但不包括位置6上的数字
e = String[:5] #等价于String[0:5] ,位置5之前的所有内容，但是不包括位置5上面的数字
f = String[5:] #等价于String[5:-1],位置5之后的所有内容，但是不包括位置5上面的数字
print(d,e,f)
#字符串从左向右数是0 start，从右向左数是-1 start'''
'''
# Demo 8 字符串练习1
Word = 'Friends'
evil = Word[0]+Word[2:6]
print(evil) ###字符串不可以减，可以加 ==》同理，不能除可以乘
'''
'''
#Demo 9 字符串练习2
url1 = 'http://ww1.site.cn/14d2e8ejw1exjogbxdxhj20ci0kuwex.jpg'
url2 = 'http://ww1.site.cn/85cc87jw1ex23yhwws5j20jg0szmzk.png'
url3 = 'http://ww3.site.cn/185cc87jw1ex23yyvq29j20jg0t6gp4.gif'
photo1 = url1[-12:] #[-12:-1](X) [-12: ](√)
photo2 = url2[-12:]
photo3 = url3[-12:]
print(photo1)
print(photo2)
print(photo3)
'''
'''
#Demo 10 字符串练习--隐藏手机号码
number = '185-5326-5715'
hide_number_first = number.replace(number[0:9],'*' * 8)
print(hide_number_first)
#练习字符串的replace功能
'''
'''
#Demo 11 字符串练习--模拟手机通讯录
search = '168'
num_a = '168-2223-3342'
num_b='321-2345-1683'
print(search+' is at '+str(num_a.find(search)+1)+' to '+str(num_a.find(search)+len(search))+' of num_a ') #因为数组从0开始，所以要+1变为1
print(search+' is at '+str(num_b.find(search)+1)+' to '+str(num_b.find(search)+len(search))+ 'of num_b ') #同理可得
'''

'''
#Demo 12 字符串练习--填空题的几种形式
#_(with)_ a word she can get what she _(came)_ for
print('{} a word she can get what she {} for'.format('with','came'))
print('{prep} a word she can get what she {verb} for'.format(prep='with',verb='came'))
print('{0} a word she can get what she {1} for'.format('with','came'))
#使用format特性，需要填写的空用大括号对表示
'''

''' 
一个输入城市获取天气的API输入框，不过好像是坏的
city = input("Write down the name of city:")
url = "https://jisuweather.api.bdymkt.com/weather/{}".format(city)
print(url)
'''

'''
#函数是编程中最基本的魔法，但同时一切的复杂又被隐含其中。
#Define a function named 'function' which has two arguments:arg1 and arg2,returns the result——something

def function(arg1,arg2):  #关键字 函数名(参数1，参数2) :
    return 'Something'    #缩进! 关键字 结果 

#缩进后面是一个语句块(block)，主要用来表示逻辑和代码的从属关系
'''