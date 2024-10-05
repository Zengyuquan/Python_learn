import re

s1 = "python itheima python python"
# match从头匹配
result = re.match("python", s1)
print(result)
print(result.span())
print(result.group())


s2 = "11python itheima python python"
# search搜索全部
result = re.search("python", s2)
print(result.span())
print(result.group())

s3 = "11python itheima python python itheima python"
# findall搜索全部匹配
result = re.findall("python", s3)
print(result)
