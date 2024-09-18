# 定义一个函数，完成2数相加功能
def add(a,b):
    # 通过返回值，将相加的结果返回调用者
    result = a + b
    return result
    # 返回结果后，还想输出一句话
    print("并不会被打印输出，函数遇到return后结束")

# 函数的返回值，可以通过变量取接收
r = add(5,6)
print(r)