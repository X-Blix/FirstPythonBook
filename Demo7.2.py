#类与可口可乐

#1.魔术方法
'''
def __init__():
在类里定义，在创建实例时能帮助你自动的处理很多事情，比如新增实例属性
__init__()是initialize(初始化)的缩写
'''

'''
#Demo 1.1
class Cocacola():
    formula = ['caffine','sugar','water','soda']
    def __init__(self):
        self.local_logo = '可口可乐'

    def drink(self):
        print('Energy!')
coke = Cocacola()
print(coke.local_logo)
#>>>可口可乐
'''

'''
#Demo 1.2
class Cocacola:
    formula = ['caffine','sugar','water','soda']
    def __init__(self):
        for element in self.formula:
            print('Coke has {}!'.format(element))

    def drink(coke):
        print('Energy!')
coke = Cocacola()
'''
'''

#Demo 1.3
#__init__()的说明：
#1.__init__可以拥有自己的参数
#2.__init__可以自动执行，不需要使用obj.__init__()的方式来执行

class Cocacola:
    formula = ['caffine','sugar','water','soda']
    def __init__(self,logo_name):
        self.local_logo = logo_name
        #左边是变量作为类的属性，右边是传入这个参数作为变量
        #变量的复制所存储的结果取决于初始化的时候所传进来的参数logo_name
        #传进来什么就将是什么

    def drink(self):
        print('Energy!')
coke = Cocacola('可口可乐')
print(coke.local_logo)
'''
'''
#2.类的继承(inheritance)

#Demo 2.1 配方的重定义
#所有子品类都会继承可口可乐的品牌--->类的继承（inheritance）
class Cocacola:
    calories = 140
    sodium = 45
    total_carb = 39
    caffine = 34
    ingredients = [
        'High Fructose Corn Syrup'
        'Carbonated Water'
        'Phosphoric Acid'
        'Natural Flavors'
        'Caramel Color'
        'Caffine'
    ]
    def __init__(self,logo_name):
        self.local_logo = logo_name
    def drink(self):
        print('You got {} cal energy!'.format(self.calories))
        self = self

class CaffineFree(Cocacola):
    #在新的类CaffineFree后的括号里放入Cocacola，表示这个欸继承于父类CocaCola
    #父类中的变量完全被子类继承。有改动可以进行覆盖（Override）
    caffine = 0
    ingredients = [
        'High Fructose Corn Syrup'
        'Carbonatd Water'
        'Phosphoric Acid'
        'Natural Flavors'
        'Caramel Color'
    ]
coke_a = CaffineFree('Cocacola-FREE')
coke_a.drink()
'''

'''
#3.类属性与实体属性
#Q1 ：类属性如果被重新赋值，是否影响到类属性的引用？ YES
class TestA:
    attr = 1
obj_a = TestA()
TestA.attr = 42
print(obj_a.attr)
'''

'''
Python的引用机制是自外而内的。创建实例后引用属性，
1.编译器会先搜索实例是否拥有这个属性。若有则引用。
2.若没有，搜索实例所属的类是否有这个属性。若有则引用
3.若都没有，则报错
'''


#print 42
'''


'''
#Q2 :实例属性如果被重新赋值，是否影响到类属性引用 NO
class TestA:
    attr = 1
obj_a = TestA()
obj_b = TestA()

obj_a.attr = 42
print(obj_b.attr)
#print 1
'''

#Q3 类属性实例属性具有相同的名称，那么.后面引用的将会是什么？ 实例属性
class TestA:
    attr = 1  # 类属性

    def __init__(self):
        self.attr = 42  # 实例属性


obj = TestA()
print(obj.attr)
print 42

#__dict__是一个类的特殊属性，是一个字典，存储类或实例的属性
print(TestA.__dict__)

#{'__module__': '__main__', 'attr': 1, '__init__': <function TestA.__init__ at 0x0000020B6BD91900>, '__dict__': <attribute '__dict__' of 'TestA' objects>, '__weakref__': <attribute '__weakref__' of 'TestA' objects>, '__doc__': None}


print(obj.__dict__)
'''
{'attr': 42}
'''

#类TestA和类的实例obj_a各自拥有各自的attr属性，互相完全独立

'''