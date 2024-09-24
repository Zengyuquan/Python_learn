# 对list进行切片，从1开始，4结束，步长为1
my_list = [0,1,2,3,4,5,6]
result1 = my_list[1:4]      #步长为1 ，所以可以省略不写
print(f"结果1：{result1}")

# 对tuple进行切片，从头开始，到最后结束。步长为1
my_tuple = (0,1,2,3,4,5,6)  # 起始和结束不写表示从头到尾，步长为1可以省略
result2 = my_tuple[:]
print(f"结果2：{result2}")

# 对str行进切片，从头开始，到尾结束，步长为2
my_str = "01234567"
result3 = my_str[::2]
print(f"结果3：{result3}")

# 对str进行切片，从头开始，到尾结束，步长为-1
my_str = "01234567"
result4 = my_str[::-1]
print(f"结果4：{result4}")

# 对list进行切片，从3开始，到1结束，步长为-1
my_list = [0,1,2,3,4,5,6]
result5 = my_list[3:1:-1]
print(f"结果5：{result5}")

# 对tuple进行切片，从头开始，到尾结束，步长为2
my_tuple = (0,1,2,3,4,5,6)
result6 = my_tuple[::-2]
print(f"结果6：{result6}")