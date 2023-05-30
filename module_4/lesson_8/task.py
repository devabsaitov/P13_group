import json
import time

import httpx
from multiprocessing import Pool

def get_data_and_save(req_name):
    response = httpx.get(f"https://jsonplaceholder.typicode.com/{req_name}")
    with open(f"{req_name}.json", "w") as f:
        json.dump(json.loads(response.content),f, indent=3)


if __name__ == '__main__':
    req_name_list = ["posts" , "albums" , "comments" , "todos" , "users"]

    start = time.time()
    with Pool(5) as p:
        p.map(get_data_and_save , req_name_list)
    print(time.time() - start)



