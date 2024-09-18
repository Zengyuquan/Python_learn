my_dict = {"周杰轮":99,"林俊节":88,"张学铀":77}

# 新增元素
my_dict["张信哲"] = 66
print(f"字典经过新增元素后，结果：{my_dict}")

# 更新元素
score = my_dict["周杰轮"] = 33
print(f"字典中被移除了一个元素，结果：{my_dict},周杰轮的考试分数是：{score}")

# 删除元素
score = my_dict("周杰轮")
print(f"字典中被移除了一个元素，结果：{my_dict}，周杰轮的考试分数是：{score}")

# 清空元素，clear
my_dict.clear()
print(f"字典被清空了，内容是：{my_dict}")

# 获取全部的key
my_dict = {"周杰轮":99,"林俊节":88,"张学铀":77}
keys = my_dict.keys()
print(f"字典的全部key是：{keys}")

# 遍历字典
# 方式1：通过获取到全部的key来完成遍历
for key in keys:
    print(f"字典的key是：{key}")
    print(f"字典的value是：{my_dict[key]}")

# 统计字典内的元素数量
