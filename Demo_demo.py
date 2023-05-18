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
数据是按照条来进行存储的，以”，“为一行的结束分隔
将列表变成元组，目的是为了节省内存
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