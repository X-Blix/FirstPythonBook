###循环与判断
# 逻辑控制
# 条件控制与循环

# 条件控制：
# 条件控制实际上就是 if...else... 的运用
'''
              #if else 后面都有一个逗号
if condition: #condition 是返回条件为true的表达式
    do something

else:
    do something
#如果..条件成立，就做...；如果...条件不成立，就做...
'''
'''
#Demo 1 if-else 举例说明
#定义部分
def account_login(): #用户登录器
    password  = input('Please input your Password:')
    if password == "12345": #使用if-else设置条件
        password_correct = password =='12345'
        print('Login Success!') #布尔表达式：12345
    else:
        print('Login fall!')
        account_login() #运行函数
#调用部分
account_login() #调用函数
'''

# 在编写函数的时候，考虑到逻辑上的完整性，会进行多条件的判断
# 使用多条件判断的方法：在 if...else...语句中加入elif
# elif使用方法和if类似，会执行符合条件布尔值后的语句
# 若都不符合，则会跳到最后执行else语句
'''
if condition:
    do something
elif condition:
    do something
else:
    do something
'''

'''Demo 2 使用elif语句做一个重置密码的功能

pwd_list = ['123456','654321']
def password_change(pwd_list=pwd_list):
    pwd = input('input pwd:')
    if pwd in pwd_list:
        print('login success!')
        return pwd_list #需要返回，不然还会接下来连着运行
    elif pwd not in pwd_list:
        new_password = input('AS a new password：')
        append = pwd_list.append(new_password)
        print(pwd_list.append(append))
        print('new password add successfully!')
        #return append #返回值是None，append方法只是修改列表不是返回列表
        print(pwd_list) #输出数据应该用print
    else:
        print('Wrong password or invalid input!')
        return pwd_list #需要返回

password_change()
'''
'''
代码块（Code Block）
代码块的产生是由于缩进，具有相同缩进量的代码是在一个层面上完成事情
'''

###循环

##for循环 :在可迭代的序列被穷尽时而终止
# 语法：
'''
#item 是可容纳“每一个元素”的变量名称，不能和关键字重名
#in 后面的元素是“可迭代的(uterable)”,比如列表
for item in iterable: #于...其中的每一个元素，做...事情
    do something
'''
'''
Demo 1:循环输出
for every_letter in 'Hello World':
    print(every_letter)

Demo2 循环输出

for i in range(0,11):
    print(str(i)+ '+ 1 =',i+1) #需要进行类型转换，且需要逗号进行分割
'''

'''
Demo 3 将循环与选择结合进行应用：

song_list = ['Holy Driver','Thunderstruck','Rebel Rebel']
for song in song_list:
    if song == song_list[0]:
        print(song,'-DIO')
    elif song == song_list[1]:
        print(song,'-AC/DC')
    else:
        print(song,'- David Bowie')
#将所需要的元素从列表中取出来，并输出相应的对应值
'''

'''
#嵌套循环(Nested Loop)
#举例：99乘法表
Demo 4
for i in range (1,10):
    for j in range(1,10):
        res =('{} X {} = {}').format(i,j,i*j)
        print(res)
'''

# while循环  #在条件成立时，会一直执行下去（只要...条件成立，就一直做...）

# 语法：
# while condition:
#    do something

# while(True): #这种条件永远成立的循环，称为死循环(infinite Loop)

'''
Demo 5 在while循环中制造某种可以让循环停下来的条件

count = 0 #目的：计数器
while True:
    print('Repeat this line')
    count = count + 1 #重新赋值，每次在新的基础上+1
    if count == 5:
        break #上面条件成立，则停下来，跳出循环
'''

'''
Demo 6: 改变使循环成立的条件
若输入密码3次则禁止输入密码

pwd_list = ['123456','654321']
def password_change(pwd_list=pwd_list):
    total = 3  # 计数器
    while total > 0: #增加while循环
        pwd = input('input pwd:')
        if pwd in pwd_list:
            print('login success!')
            return pwd_list #需要返回，不然还会接下来连着运行
        elif pwd not in pwd_list:
            print('password is wrong,plrase input again(you have only {} chances):'.format(total-1))
            total = total - 1 #密码输入错误，次数减少1，直至为0
        else:
            print('Your account has been suspended')
            return pwd_list
#在while代码块中又存在着第二层逻辑判断，是一个while-else嵌套逻辑
password_change()
'''

