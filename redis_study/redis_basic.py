import redis

pool = redis.ConnectionPool(
    host="127.0.0.1",
    port=6379,
    decode_responses=True
)
# decode_responses 表示是否针对结果做decode转码
r = redis.Redis(connection_pool=pool)  # redis操作对象
# 操作字段数据
r.set("name", "shamo2")
# print(r.get("name"))

# 操作hash（字典）数据
r.hset("userinfo2", "name", "shamo")
r.hset("userinfo2", "age", "18")
r.hset("userinfo2", "job", "tester")
# print(r.hgetall("userinfo2"))
# 操作list
r.lpush("list33", "data1", "data2", "data3")
# print(r.lrange("list33", 0, -1))


# 操作集合
r.sadd("jihe33", "da1", "da2", "da3")
print(r.smembers("jihe33"))

# 操作有序集合
r.zadd("zset33", {"data1": 80, "data2": 70, "data3": 90})
print(r.zrange("zset33", 0, -1))

print(r.type("zset33"))
print(r.type("jihe33"))
print(r.type("list33"))
print(r.type("name"))
print(r.type("userinfo2"))
