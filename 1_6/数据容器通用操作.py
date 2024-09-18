my_list = [1,2,3,4,5]
my_tuple = (1,2,3,4,5)
my_str = "abcdfg"
my_set = {1,2,3,4,5}
my_dict = {"key1":1,"key2":2,"key3":3,"key4":4,"key5":5}

# len()元素个数
print(f"列表元素有：{len(my_list)}")
print(f"元组元素有：{len(my_tuple)}")
print(f"字符串元素有：{len(my_str)}")
print(f"集合元素有：{len(my_set)}")
print(f"字典元素有：{len(my_dict)}")
print("-----------------------------------------------")
# max最大元素
print(f"列表最大元素有：{max(my_list)}")
print(f"元组最大元素有：{max(my_tuple)}")
print(f"字符串最大元素有：{max(my_str)}")
print(f"集合最大元素有：{max(my_set)}")
print(f"字典最大元素有：{max(my_dict)}")
print("-----------------------------------------------")

# min最小元素
print(f"列表最小元素有：{min(my_list)}")
print(f"元组最小元素有：{min(my_tuple)}")
print(f"字符串最小元素有：{min(my_str)}")
print(f"集合最小元素有：{min(my_set)}")
print(f"字典最小元素有：{min(my_dict)}")
print("-----------------------------------------------")

# 类型转换：数据容器转列表
print(f"列表转列表的结果：{list(my_list)}")
print(f"元组转列表的结果：{list(my_tuple)}")
print(f"字符串转列表结果：{list(my_str)}")
print(f"集合转列表的结果：{list(my_set)}")
print(f"字典转列表的结果：{list(my_dict)}")
print("-----------------------------------------------")

# 类型转换：数据容器转元组
print(f"列表转元组的结果：{tuple(my_list)}")
print(f"元组转元组的结果：{tuple(my_tuple)}")
print(f"字符串转元组结果：{tuple(my_str)}")
print(f"集合转元组的结果：{tuple(my_set)}")
print(f"字典转元组的结果：{tuple(my_dict)}")
print("-----------------------------------------------")

# 类型转换：数据容器转字符串
print(f"列表转字符串的结果：{str(my_list)}")
print(f"元组转字符串的结果：{str(my_tuple)}")
print(f"字符串转字符串结果：{str(my_str)}")
print(f"集合转字符串的结果：{str(my_set)}")
print(f"字典转字符串的结果：{str(my_dict)}")
print("-----------------------------------------------")

# 类型转换：数据容器转集合
print(f"列表转集合的结果：{set(my_list)}")
print(f"元组转集合的结果：{set(my_tuple)}")
print(f"字符串转集合结果：{set(my_str)}")
print(f"集合转集合的结果：{set(my_set)}")
print(f"字典转集合的结果：{set(my_dict)}")
print("-----------------------------------------------")

# 进行容器的排序
my_list = [3,1,2,5,4]
my_tuple = (3,1,2,5,4)
my_str = "bdcefga"
my_dict = {"key3":1,"key1":2,"key2":3,"key5":4,"key4":5}

print(f"列表对象的排序结果：{sorted(my_list)}")
print(f"元组对象的排序结果：{sorted(my_tuple)}")
print(f"字符串对象的排序结果：{sorted(my_str)}")
print(f"集合对象的排序结果：{sorted(my_set)}")
print(f"字典对象的排序结果：{sorted(my_dict)}")

print(f"列表对象的方向排序结果：{sorted(my_list,reversed = True)}")
print(f"元组对象的方向排序结果：{sorted(my_tuple,reversed = True)}")
print(f"字符串对象的方向排序结果：{sorted(my_str,reversed = True)}")
print(f"集合对象的方向排序结果：{sorted(my_set,reversed = True)}")
print(f"字典对象的方向排序结果：{sorted(my_dict,reversed = True)}")

