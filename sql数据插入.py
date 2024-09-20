from pymysql import Connection

# 构建MySQL数据库的连接
conn = Connection(
    host="localhost",
    port=3306,
    user="root",
    password="123456",
    autocommit=True
)

# print(conn.get_server_info())

# 执行非查询性质SQL
cursor = conn.cursor()      # 获取到游标对象
# 选择数据库
conn.select_db("test")
# 执行sql，插入数据
cursor.execute("insert into user values(id=101,name='zqs')")
# 通过commit确定
# conn.commit()

# 关闭连接
conn.close()