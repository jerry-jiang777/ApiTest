import pymysql


class DBUtil:
    def __init__(self, host, user, password, port=3306):
        self.connect = pymysql.connect(
            host=host,
            user=user,
            password=password,
            port=port,
            charset='utf8mb4',
            cursorclass=pymysql.cursors.DictCursor
        )

    def select(self, sql):
        cursor = self.connect.cursor()
        cursor.execute(sql)
        data = cursor.fetchall()
        self.connect.commit()
        cursor.close()
        return data

    def updata(self, sql):
        """
        insert
        delete
        update
        :param sql:
        :return:
        """
        cursor = self.connect.cursor()
        cursor.execute(sql)
        self.connect.commit()
        cursor.close()

    def close(self):
        if self.connect is not None:
            self.connect.close()


if __name__ == "__main__":
    db_util = DBUtil(
        host="59.36.173.55",
        user="mtxshop_test",
        password="mtxshamo",
        port=3306
                     )

    res = db_util.select("select * from mtxshop_trade.es_order ORDER BY order_id DESC LIMIT 2")
    print(res[0]["order_status"])
    db_util.close()
