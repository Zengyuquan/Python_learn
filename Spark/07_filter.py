# 构建执行坏境入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([1,2,3,4,5])

# 对RDD的数据进行过滤
rdd2 = rdd.filter(lambda num: num % 2 == 0)

print(rdd2.collect())

sc.stop()