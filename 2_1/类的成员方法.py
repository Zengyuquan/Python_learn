# 定义一个带有成员方法的类
class Student:
    name = None;

    def say_hi(self):
        print(f"大家好呀，我是{self.name},欢迎大家多多关照")

    def say_hi2(self, msg):
        print(f"大家好，我是：{self.name},{msg}")

stu = Student()
stu.name = "周杰轮"
stu.say_hi2("哎呦不错哟")

stu2 = Student()
stu2.name = "林俊节"
stu2.say_hi2("小伙子，我看好你")