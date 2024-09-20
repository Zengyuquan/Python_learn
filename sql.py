from pymysql import Connection

# 构建MySQL数据库的连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456"
)

# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("test")
# 执行sql
# cursor.execute("create table test_pymysql1(id int);")

# 查询
cursor.execute("select * from user;")

result = cursor.fetchall()
print(f"{type(result)}")
for r in result:
    print(r)

print(f"{type(r)}")

# 关闭连接
conn.close()