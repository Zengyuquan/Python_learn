# # 基本捕获
# try:
#     f = open("D:/abc.txt","r",encoding="UTF-8")
# except:
#     print("出现异常了，因为文件不存在，将open的模式，改为w模式去打开")
#     f = open("D:/abc.txt","w",encoding="UTF-8")
#
# f.close()
# # 捕获指定异常
# try:
#     print(name)
# except NameError as e:
#     print("出现了变量未定义的异常")
#     print(e)
#
# # 捕获多个异常
# try:
#     1/0
#     print(name)
# except (NameError,ZeroDivisionError) as e:
#     print("出现了变量未定义 或 除以0的异常错误")
#     print(e)

# 捕获全部异常
try:
    # print("hello")
    # a = 1 / 0
    # print(name)
    f = open("D:/abcde.txt", "r", encoding="UTF-8")

except Exception as e:
    print("出现异常了")
    f = open("D:/abcde.txt", "w", encoding="UTF-8")
else:
    print("没有出现异常")
finally:
    print("finally无论有没有异常都执行")
    f.close()