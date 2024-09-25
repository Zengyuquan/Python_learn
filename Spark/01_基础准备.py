# 导包
from pyspark import SparkConf, SparkContext
# 创建SparConf类对象
conf = SparkConf().setMaster("local[*]").setAppName("test_spark_app")
# 基于SparkConf类对象创建SparkContext
sc = SparkContext(conf=conf)
# 打印pyspark的运行版本
print(sc.version)
# 停止SparkContext对象的运行（停止运行pyspark程序）
sc.stop()