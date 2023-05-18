##类与可口可乐
'''
class CocaCola:
    it_taste = 'So good!'

coke_for_bum = CocaCola()
coke_for_president = CocaCola()

print(coke_for_bum.it_taste)
print(coke_for_president.it_taste)
'''

'''
#1.定义一个类
#被称为一类的物体，都有相似的特征和行为方式
#类是一系列有共同特征和行为事物的抽象概念的总和

class CocaCola:     #使用class定义一个类
    formula = ['caffeine','sugar','water','soda'] #类的（变量）叫做类的属性

#类的实例化(instance)
#按照配方把可乐生产出来的过程就是实例化的过程
coke_for_me = CocaCola()
coke_for_you = CocaCola()
print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

#2.类属性的引用
#在类的后面输入”。“,IDE会联想出在定义类的时候写的属性。-->类属性的引用(attribute references)
#类的属性会被所有类的实例共享
print(CocaCola.formula)
print(coke_for_me.formula)
print(coke_for_you.formula)

#类的属性和正常的变量并无区别
for element in coke_for_me.formula:
    print(element)
'''

'''
#3.实例属性
class CocaCola:     #使用class定义一个类
    formula = ['caffeine','sugar','water','soda'] #类的（变量）叫做类的属性

coke_for_China = CocaCola
coke_for_China.local_logo = '可口可乐' #创建实例属性
#在创建了类之后，通过object.new_attr的形式进行一个赋值，得到一个新的实例的变量，也叫实例属性（instance attribute）
print(coke_for_China.local_logo)#打印实例属性引用结果

可乐的配方（formula）属于可口可乐（Class），
而”可口可乐“的中文标识（local_logo）属于中国区的每一瓶可乐（instance）
给中国区可口可乐贴上中文标签不会影响到美国地区的销售。
'''

'''
#4.实例方法
#类的实例可以引用属性，方法就是函数，但我们吧这个函数称为方法（Method）
#方法是供实例使用的。也可以叫做实例方法
'''
#喝掉一瓶可乐的时候，会从大量的糖分和咖啡因中获得能量
#使用类的方法来表示这个功能
'''
class Cocacola:
    formula = ['caffeine','sugar','water','soda']
    def dink(self):
    #等价于def dink(coke): -- >这个参数就是被创建的实例本身
        print('energy')

coke = Cocacola()
coke.dink()
#等价于CocaCola.drink(coke)-->一个类被实例花，可以使用与我们使用函数相似的方式
#被实例化的对象会被默默的传到后面方法中的括号中--->更多的写成前面那种形式

#BTW:英语中，”功能“和”函数“都由一个词表达 —— Function
'''

#5.更多参数
#类的方法也能有属于自己的参数
class CocaCola:
    formula = ['caffine','sugar','water','soda']
    def drink(self,how_much):

        if how_much == 'a sip':
            print('Cool~')
        elif how_much == 'whole bottle':
            print('Headache')

ice_coke = CocaCola()
ice_coke.drink('a sip')
