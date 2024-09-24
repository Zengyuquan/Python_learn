#while循环遍历
def list_while_func():

    my_list = ["itheima", "itcast", "python"]

    index = 0
    while  index < len(my_list):
        element = my_list[index]
        print(f"列表的元素，第{index + 1}个：{element}")

        index += 1



def list_for_func():
    my_list = ["itheima", "itcast", "python", "itcast", "python"]

    for element in my_list:
        print(f"列表的元素：{element}")


list_while_func()
print("-----------------")
list_for_func()