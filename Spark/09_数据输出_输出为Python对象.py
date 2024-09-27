from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备RDD
rdd = sc.parallelize([1,2,3,4,5])

# collect算子，输出RDD为list对象
rdd_list: list = rdd.collect()
print(rdd_list)
print(type(rdd_list))

# reduce算子，将rdd进行两两聚合
num = rdd.reduce(lambda a, b: a + b)
print(num)

# take算子，取出RDD为list对象
take_list = rdd.take(3)
print(take_list)

#  count,统计rdd内有多少数据，返回为数字
num_count = rdd.count()
print(f"rdd内有{num_count}个元素")

sc.stop()