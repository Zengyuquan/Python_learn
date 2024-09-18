# 打开文件
import time

f = open("D:\python.txt","r",encoding="UTF-8")
print(type(f))

# 读取文件- read()
# print(f"读取10个字节的结果：{f.read(10)}")
# print(f"读取全部内容的结果：\n{f.read()}")

# 读取文件 - readlines()
# lines = f.readlines()       # 读取文件的全部行，封装到列表中
# print(f"lines对象的类型：{type(lines)}")
# print(f"lines对象的内容是：{lines}")

# 读取文件 - readline()
# line1 = f.readline()
# line2 = f.readline()
# line3 = f.readline()
# line4 = f.readline()
# print(f"第一行数据是：{line1}")
# print(f"第二行数据是：{line2}")
# print(f"第三行数据是：{line3}")
# print(f"第四行数据是：{line4}")

# for循环读取文件行
for line in f:
    print(f"每一行数据是：{line}")


# 文件的关闭
# time.sleep(300)
#f.close()

# with open语法操作文件
with open("D:\python.txt","r",encoding="UTF-8") as f:
    for line in f:
        print(f"每一行数据：{line}")

time.sleep(10000)
