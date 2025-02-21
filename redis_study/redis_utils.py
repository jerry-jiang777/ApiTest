import javaobj
import redis


class RedisUtil:
    def __init__(self, host, pwd, port: 6379, decode_responses=False):
        self.pool = redis.ConnectionPool(
            host=host,
            port=port,
            password=pwd,
            decode_responses=decode_responses
        )
        self.r = redis.Redis(connection_pool=self.pool)  # redis操作对象
        # 提供统一的获取数据方法

    def get(self, key):
        # 判断要操作的数据类型, 决定调用什么方法处理数据
        type_ = self.r.type(key)
        if type_ == b'string' or type == 'string':
            return self.r.get(key)
        elif type_ == b'hash' or type == 'hash':
            return self.r.hgetall(key)
        elif type_ == b'list' or type == 'list':
            return self.r.lrange(key, 0, -1)
        elif type_ == b'set' or type == 'set':
            return self.r.smembers(key)
        elif type_ == b'zset' or type == 'zset':
            return self.r.zrange(key, 0, -1)
        else:
            raise BaseException(f"{key} 的数据类型不支持")


if __name__ == "__main__":
    # pool = redis.ConnectionPool(
    #     host="59.36.173.55",
    #     port=6379,
    #     password="mtx",
    #     decode_responses=False
    # )
    # r = redis.Redis(connection_pool=pool)  # redis操作对象
    # res = r.get("{BUY_NOW_ORIGIN_DATA_PREFIX}_7778611")  # 59
    # res 是java对象序列化后的数据,要把他转换成python对象
    r = RedisUtil(host="59.36.173.55", pwd="mtx", port=6379)
    # 我们要把其转化成python对象
    # pip install javaobj-py3
    # print(r.get("{BUY_NOW_ORIGIN_DATA_PREFIX}_59")) # 立即购买的操作
    res = r.get("{CHECKOUT_PARAM_ID_PREFIX}_7778611")  # 确认收获地址的操作
    for key, value in res.items():
        key = javaobj.loads(key)
        if value == b'':
            value = ''
        else:
            value = javaobj.loads(value)
            if key == 'paymentType':
                print(dir(value))
                value = value.constant
        print(f"{key}: {value}")








    # 立即购买数据解析
    # res = r.get("{BUY_NOW_ORIGIN_DATA_PREFIX}_7778611")
    # res_obj = javaobj.loads(res)
    # print(res_obj)
    # print(type(res_obj))
    # buy_now_object = res_obj[0]
    # buy_now_object对象都有哪些属性
    # python中可以用dir查看对象有哪些属性
    # print(dir(buy_now_object))
    # print(buy_now_object.__getattribute__("skuId"))
    # print(buy_now_object.__getattribute__("num"))
