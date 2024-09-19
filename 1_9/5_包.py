# 创建一个包
# 导入自定义的包中的模块，并使用
import my_package.my_model1
# import my_package.my_model2
#
# my_package.my_model1.info_print1()
# my_package.my_model2.info_print2()

# from my_package import my_model1
# from my_package import my_model2
# my_model1.info_print1()
# my_model2.info_print2()

# from my_package.my_model1 import info_print1
# from my_package.my_model2 import info_print2
# info_print1()
# info_print2()

# 通过__all__变量，控制import *
from my_package import *
my_model1.info_print1()
# my_model2.info_print2()