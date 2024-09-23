class Phone:
    IMEI = None
    producer = "ITCAST"

    def call_by_5g(self):
        print("使用5g网络进行通话")

# 定义子类，复写父类成员
class MyPhone(Phone):
    producer = "ITHEIMA"

    def call_by_5g(self):
        print("开启CPU单核模式，确保通话的时候省电")
        #方法1
        # print(f"父类的厂商是：{Phone.producer}")
        # Phone.call_by_5g(self)
        #方法2
        print(f"父类的厂商是：{Phone.producer}")
        super().call_by_5g()
        print("关闭CUP单核模式，确保性能")

phone = MyPhone()
phone.call_by_5g()
print(phone.producer)