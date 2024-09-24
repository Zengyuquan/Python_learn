# 1.设计一个类(类比生活中：设计一张表)
class Student:
    name = None
    gender = None
    nationality = None
    native_place = None
    age = None

# 2.创建一个对象(类比生活中：打印一张表)
stu1 = Student()
# stu2 = Student()

# 3.对象属性进行赋值(类比生活中：填写表单)
stu1.name = '林俊节'
stu1.gender = '男'
stu1.nationality = '中国'
stu1.native_place = '广东'
stu1.age = 18

# 4.获取对象中记录的信息
print(stu1.name)
print(stu1.gender)
print(stu1.nationality)
print(stu1.native_place)
print(stu1.age)