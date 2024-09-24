#定义一个列表list
my_list = ["itheima","itcast","python"]
print(my_list)
print(type(my_list))

my_list = ["itheima",666,True]
print(my_list)
print(type(my_list))

#定义一个嵌套的列表
my_list = [[1,2,3],[4,5,6]]
print(my_list)
print(type(my_list))

#通过下标索引取出对应位置的数据
my_list = ["Tom","Lily","Rose"]
#列表[下标索引]从前往后从0开始，每次+1.     从后往前从-1开始，每次-1
print(my_list[0])
print(my_list[1])
print(my_list[2])
#倒叙
print(my_list[-1])
print(my_list[-2])
print(my_list[-3])

#取出嵌套列表的元素
my_list = [[1,2,3],[4,5,6]]
print(my_list[1][1])