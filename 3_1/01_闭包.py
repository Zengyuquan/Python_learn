# def outer(loge):
#
#     def inner(msg):
#         print(f"<{loge}>{msg}<{loge}>");
#
#     return inner
#
# fn1 = outer("黑马程序员")
# fn1("大家好")
#
# fn2 = outer("传智教育")
# fn2("大家好")

# def outer(num1):
#
#     def inner(num2):
#         nonlocal num1
#         num1 += num2
#         print(num1)
#
#     return inner
#
# fn = outer(10)
# fn(10)          # 20
# fn(10)          # 30
# fn(20)          # 50

def account_create(initial_amount=0):

    def atm(num, deposit = True):
        nonlocal initial_amount
        if deposit:
            initial_amount += num
            print(f"存款：+{num}, 账户余额：{initial_amount}")
        else:
            initial_amount -= num
            print(f"存款：-{num}, 账户余额：{initial_amount}")

    return atm

atm = account_create()
print(type(atm))

atm(100)
atm(200)
atm(100, deposit=False)