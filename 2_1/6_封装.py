# 定一个类，内含私有成员变量和私有成员方法
class Phone:

    __current_voltage = 0.5

    def __keep_sing_core(self):
        print("让cup以单核运行")

    def call_by_5G(self):
       if self.__current_voltage >= 1:
           print("5G通话，启动！")
       else:
           self.__keep_sing_core()
           print("电量不足，无法开启5G通话，并已设置为单核运行进行省电")

phone = Phone()
phone.call_by_5G()