my_str = "itheima and itcast"
# 通过下标索引取值
value = my_str[2]
value2 = my_str[-16]
print(f"从字符串{my_str}取下标为2的元素，值是{value}，取下标为16的元素为：{value2}")

# index方法
value = my_str.index("and")
print(f"在字符串{my_str}中查找and，其下标是：{value}")

# replace方法
new_my_str = my_str.replace("it","程序")
print(f"将字符串{my_str}进行替换后得到：{new_my_str}")

# split方法
my_str = "hello python itheima itcast"
my_str_list = my_str.split(" ")
print(f"将字符串{my_str}进行split切分后得到：{my_str_list}，类型是：{type(my_str_list)}")

# strip方法
my_str = "        itheima and itcast          "
new_my_str = my_str.strip()     #不传参数，去除首位空格
print(f"字符串{my_str}被strip后，结果是{new_my_str}")

my_str = "21itheima and itcast12"
new_my_str = my_str.strip("12")     #把‘1’，‘2’分为两个小字符串
print(f"字符串{my_str}被strip('12')后，结果是{new_my_str}")

# 统计字符串的长度，count
my_str = "itheima and itcast"
count = my_str.count("it")
print(f"字符串{my_str}中it出现的次数是：{count}")

# 统计字符串长度，len()
num = len(my_str)
print(f"字符串{my_str}的长度是：{num}")