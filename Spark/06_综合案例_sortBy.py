# 1.构建执行坏境入口对象
from pyspark import SparkConf, SparkContext
import os
os.environ['PYSPARK_PYTHON'] = "C:/Program Files/Python311/python.exe"
conf = SparkConf().setMaster("local[*]").setAppName("test_spark")
sc = SparkContext(conf=conf)

# 2.读取数据文件
rdd = sc.textFile("D:/hello.txt")

# 3.取出全部单词
word_rdd = rdd.flatMap(lambda x: x.split(" "))

# 4.将所有单词都转成二元数组，单词为key，value设置为1
word_with_one_rdd =  word_rdd.map(lambda word: (word,1))
# print(word_with_one_rdd.collect())

# 5.分组并求和
result_rdd = word_with_one_rdd.reduceByKey(lambda a, b : a + b)

# 6.对结果进行排序
final_rdd = result_rdd.sortBy(lambda x : x[1], ascending=False, numPartitions=1)
print(final_rdd.collect())

sc.stop()