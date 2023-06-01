# pip install redis
from datetime import timedelta

import redis
from PIL.Image import msg

con = redis.Redis(host = 'localhost', port = 6379 , decode_responses=True)

con.hset("user_id" , mapping={"first_name":msg.from_user.first_name , "last_name":msg.from_user.last_name})
con.hgetall("user_id")

dict_ = {
    "1" : 10
}

dict_["1"] = 11

print(len(dict_))











