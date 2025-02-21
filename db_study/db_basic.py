import pymysql


# 创建数据库连接对象 需要数据库几点信息： ip username pwd port
connect = pymysql.Connect(
    host="59.36.173.55",
    port=3306,
    user="mtxshop_test",
    password="mtxshamo",
    charset='utf8mb4',
    cursorclass=pymysql.cursors.DictCursor  # 这个参数的意思是得到的行数据以字典方式存储
)

# 要操作数据库，必须先得到一个游标对象
# 这个游标对象将会把当前数据库的结果集存储起来,后续的操作就是在这个结果集上面进行
cursors = connect.cursor()

# 查询订单数据倒叙排序，取前两条数据
cursors.execute("select * from mtxshop_trade.es_order ORDER BY order_id DESC LIMIT 2")
# 得到所有查询结果
res = cursors.fetchall()
print(res)
print(res[0]["order_status"])
cursors.close()
connect.close()
