'''
#练习题
#Demo 7 :设置一个函数，创建10个文本，并以数字连续命名
for i in range(0,11):
    path = (str(i)+'.txt' )
    file = open(path,'w')
'''
'''
#Demo 8:计算复利

def invest(amount,rate,time):
    while int(time) > 0:
        amount = (amount*rate)+amount
        print('year '+ str(time)+':'+str(amount))
        time = time - 1

#input 应该放在函数调用部分
time = int(input("input year:"))
rate = int(input("input rate%:"))
rate = rate/100
amount = int(input("input peincipal amount:"))
invest(amount,rate,time) #一一对应
'''

'''
#Demo 9 打印1~100以内偶数
for i in range(1,101):
    if(i%2 == 0):
        print(i)
'''

##综合练习

# 前置知识
'''
a_list = [1,2,3]
print(sum(a_list))
'''

'''
import random #python内置的库，用于生成随机数

point1 = random.randrange(1,7)
point2 = random.randrange(1,7)
point3 = random.randrange(1,7)

print(point1,point2,point3)
'''

'''
Demo 10 写一个猜大小的游戏

import random

def shake_dce():
    print("<<<<<GAME STARTS>>>>>")
    number = input("Big or Small:")
    list = []
    for dce in range(1,4):
        dce = random.randrange(1,7)
        list.append(dce)
    list_all = list[0]+list[1]+list[2] #list下标从0开始
    if (11 <= list_all <= 18) and number=="Small":
        print("You Lose!")
    elif (11 <= list_all <= 18) and number=="Big":
        print("You Win!")
    elif (3<=list_all<=10) and number=="Small":
        print("You Win!")
    elif (3<=list_all<=10) and number=="Big":
        print("You Lose")
    else:
        print("Wrong Tings")
    print("<<<<<ROLE THE DICE>>>>>")
    print("The points are " +str(list))

shake_dce()
'''

'''
Demo 10 正确答案版
import random
def roll_dice(numbers = 3,points = None): #numbers:筛子数量 points:点数列表
    print("<<<ROLL THE DICE! >>>")#告知用户摇筛子
    if points is None: #参数中未指定points.为points创建一个空列表
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1  #摇动三次筛子，每摇动一次数量-1.直到小于等于0
    return points #返回结果列表

def roll_result(total): #创建参数，必要的参数是筛子的总点数
    isBig = 11 <= total <= 18 #定义‘大’的标准
    isSmall = 3 <= total <=10 #定义‘小’的标准
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small' #在不同的条件下返回不同的结果

def start_game():   #创建函数
    print('<<<<< GAME STARTS !>>>>>') #告知用户游戏开始
    choices = ['Big','Small'] #规定正确的输入
    your_choice = input("Big or Small :") #用户输入的字符串放在 your_choice中
    if your_choice in choices: #如果符合规定继续向下执行
        points = roll_dice() ###调用roll_Dice函数，返回的列命名为points
        total = sum(points) #点数求和
        youWin = your_choice = roll_result(total)#所选结果和计算机生成结果相同
        if youWin: #成立告知胜利
            print('The points are',points,'You win !')
        else:#不成立告知失败
            print('The points are',points,'You lose !')
    else: #不符合规定则提示不符合规定
        print('Invalid Words')
        start_game()
start_game()

'''
'''
# Demo 11 加上功能：下注金额和赔率
#初始金额 1000元
#金额为 0 时游戏结束
#押对了会获得相应的金额，押错了会输掉相应的金额
import random
def roll_dice(numbers = 3,points = None): #numbers:筛子数量 points:点数列表
    print("<<<ROLL THE DICE! >>>")#告知用户摇筛子
    if points is None: #参数中未指定points.为points创建一个空列表
        points = []
    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1  #摇动三次筛子，每摇动一次数量-1.直到小于等于0
    return points #返回结果列表


def roll_result(total): #创建参数，必要的参数是筛子的总点数
    isBig = 11 <= total <= 18 #定义‘大’的标准
    isSmall = 3 <= total <=10 #定义‘小’的标准
    if isBig:
        return 'Big'
    elif isSmall:
        return 'Small' #在不同的条件下返回不同的结果

def start_game():   #创建函数
    your_money = 1000 #本金1000元
    while your_money > 0:
        print('<<<<< GAME STARTS !>>>>>') #告知用户游戏开始
        choices = ['Big','Small'] #规定正确的输入
        your_choice = input("Big or Small :") #用户输入的字符串放在 your_choice中
        your_bet_money = int(input('How money you wanna bet? -')) #输入想要进行打赌的金额
        if your_bet_money <= 1000: #参与打赌的钱要小于本金
            if your_choice in choices: #如果符合规定继续向下执行
                points = roll_dice() ###调用roll_Dice函数，返回的列命名为points
                total = sum(points) #点数求和
                youWin = your_choice = roll_result(total)#所选结果和计算机生成结果相同
                if youWin: #成立告知胜利
                    print('The points are',points,'You win !')
                    money_now = (your_bet_money*2)+(your_money-your_bet_money)
                    print(' you gained ' + str(your_bet_money)+','+' you have '+ str(money_now) +' know ' )#获得打赌赢得的钱
                    your_money = money_now
                else:#不成立告知失败
                    print('The points are',points,'You lose !')
                    money_now = ((-1)*your_bet_money)+ (your_money - your_bet_money)
                    print(' you lost ' + str(your_bet_money) + ',' + ' you have ' +str(money_now) +' know ')  # 失去打赌输得的钱
                    your_money = money_now

            else: #不符合规定则提示不符合规定
                print('Invalid Words')
                #start_game()
        else:#大于本金会提示钱不够
            print('Invalid Money')
    else:#退出游戏
        print("GAME OVER")
start_game()
'''

'''
#Demo 11
#用户名校验
#1.长度不少于11位
#2.移动、联通、电信号段中的一个
#3.忽略输入除号码以外其他字符的可能性
#4.号段列表：
CN_mobile  = [134,135,136,137,138,139,150,151,152,157,158,159,182,183,184,187,188,147,178,1705]
CN_union = [130,131,132,155,156,185,186,145,176,1709]
CN_telecom = [133,153,180,181,189,177,1700]


CN_mobile = [134, 135, 136, 137, 138, 139, 150, 151, 152, 157, 158, 159, 182, 183, 184, 187, 188, 147, 178, 1705]
CN_union = [130, 131, 132, 155, 156, 185, 186, 145, 176, 1709]
CN_telecom = [133, 153, 180, 181, 189, 177, 1700]
CN_aLL = CN_mobile + CN_union + CN_telecom
#print(CN_aLL)
for i in CN_aLL:
    string = str(input("Enter Your Number :"))  # 告知用户输入数字
    first_three =  int(string[0:3]) #字符串前3位,要转换成int类型
    first_four = int(string[0:4])  #字符串前4位，要转换成int类型
    if(len(string) == 11): #print("valid length")
        if first_three in CN_mobile or first_four in CN_mobile: #或者条件 用 or连接
                print("China Moile")
                print("We're sending verification code via test to your phone:"+ string)
                break #找到后用break跳出，不然会循环多次
        elif first_three in CN_union or first_four in CN_mobile: #同上
                print("China Telecom")
                print("We're sending verification code via test to your phone:" + string)
                break
        elif first_three in CN_telecom or first_four in CN_telecom: #同上上
                print("China Telecom")
                print("We're sending verification code via test to your phone:" + string)
                break
        else:
            print("Not such operator")
    else:
        print("Invalid length,your number should be in 11 digits")
'''