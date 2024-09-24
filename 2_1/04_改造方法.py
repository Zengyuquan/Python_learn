class Student:

    def __init__(self,  name, age, tel):
        self.name = name
        self.age = age
        self.tel = tel
        print("Student类创建了一个类对象")

stu1 = Student(name="zyq", age="male", tel=15218802838)
print(stu1.name)
print(stu1.age)
print(stu1.tel)