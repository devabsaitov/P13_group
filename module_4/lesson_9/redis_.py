# pip install redis
from datetime import timedelta

import redis

con = redis.Redis(host = 'localhost', port = '6381')

con.hset("user_id" , mapping={"first_name":"Botirjon" , "last_name":"Doe"})
con.hgetall("user_id")

dict_ = {
    "1" : 10
}

dict_["1"] = 11

print(len(dict_))











