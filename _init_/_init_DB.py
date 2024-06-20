import pymssql
# 初始化数据库
server = '192.168.1.106'
database = 'JobDB'
username = 'sa'
password = '123456789'
connection = pymssql.connect(server, username, password, database)
cursor = connection.cursor()

# 读取 SQL 文件内容
with open('D:\Code_study\python_study\pycharm\PY38_DB\sql\Init_db.sql', 'r',encoding='utf-8') as file:
    sql_script = file.read()

# 执行 SQL 脚本
cursor.execute(sql_script)

print("初始化数据库成功")
connection.commit()

# 关闭连接
cursor.close()
connection.close()
