import my_utils.str_util
from my_utils import file_util

print(my_utils.str_util.str_reverse("黑马程序员"))
print(my_utils.str_util.substr("itheima",0,4))

file_util.append_to_file("D:/abcd.txt","qwerty")
file_util.print_file_info("D:/abcd.txt")
