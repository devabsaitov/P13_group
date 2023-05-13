# json -> load , dump , loads , dumps
# import json

# list = [1,2,3,4]
#
# a = json.dumps(list)
# print(a , type(a))
# b = json.loads(a)
# print(b, type(b))


data = [
    {
        "v": 1
    },
    {
        "v": 2
    }
]
import json
with open("my_json.json" , "r") as f:
    try:
        l = json.load(f)
    except:
        l = []

l.extend(data)

with open("my_json.json" , "w") as f:
    json.dump(l, f , indent=3)
