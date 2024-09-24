#定义一个列表list
my_list = ["itheima","itcast","python"]

#1.查找某元素在列表内的下标索引
index = my_list.index("itheima")
print(f"itheima在列表中的下标索引值是:{index}")

#2.修改特定下标索引的值
my_list[0] = "python"
print(f"列表被修改元素值后，结果是：{my_list}")

#3.在指定下标位置插入新的元素
my_list.insert(1,"best")
print(f"列表插入元素后，结果是：{my_list}")

#4.在列表尾部追加“单个”新元素
my_list.append("黑马程序员")
print(f"列表在追加了元素后，结果是：{my_list}")

#5.在列表的尾部追加“一批”新元素
my_list2 = [1,2,3]
my_list.extend(my_list2)
print(f"列表在追加了一个新的列表后，结果是：{my_list}")

#6.删除指定下标索引的元素（2种方式）
my_list = ["itheima","itcast","python"]

#6.1 方式1： del 列表[下标]
del my_list[2]
print(f"列表删除元素后结果是：{my_list}")

#6.2 方式2： pop.(下标)
my_list = ["itheima","itcast","python"]
element = my_list.pop(2)
print(f"通过pop方式取出元素列表内容为：{my_list},取出是元素是{element}")

#7.删除某元素在列表中的第一个匹配项
my_list = ["itheima","itcast","python","itcast","python"]
my_list.remove("itcast")
print(f"通过remove方法移除元素后，列表结果是：{my_list}")

#8.清空列表
my_list.clear()
print(f"列表被清空了，结果是：{my_list}")

#9.统计列表内某内容元素的数量
my_list = ["itheima","itcast","python","itcast","python","python","itcast","python","python","itcast","python"]
count = my_list.count("python")
print(f"列表中python的数量是：{count}")

#10.统计列表中全部的元素数量
count = len(my_list)
print(f"列表的元素数量总共有：{count}个")