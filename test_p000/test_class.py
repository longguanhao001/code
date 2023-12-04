
class Student(object):
    def __init__(self,name,city):
        self.name=name
        self.city=city
    def talk(self):
        print("Hello,my name is %s I com from %s" %(self.name,self.city))
# 生成实例对象
stu1=Student('Jack','Beijing')
stu1.talk()
stu2=Student('Harry','Shanghai')
stu2.talk()