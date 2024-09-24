# 定义一个有异常的函数
def fun1():
    print("func 1 开始执行")
    num = 1 / 0
    print("fun1 执行结束")

# 定义一个无异常的函数，调用上面的函数
def fun2():
    print("func 2 开始执行")
    fun1()
    print("fun2 执行结束")

# 定义一个函数，继续调用上面的函数
def main():
    try:
        fun2()
    except:
        print("出现异常")

main()