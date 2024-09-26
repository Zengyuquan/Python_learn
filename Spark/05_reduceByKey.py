from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"

conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 准备一个RDD
rdd = sc.parallelize([('男',99),('男',88),('女',99),('女',66)])
# 求男女生两个数组的成绩之和
rdd2 = rdd.reduceByKey(lambda a,b : a + b)
print(rdd2.collect())

sc.stop()