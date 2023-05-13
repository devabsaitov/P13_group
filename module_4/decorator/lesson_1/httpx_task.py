# httpx

# REQUEST METHODS : post , get , delete , put , putch
import httpx
import json



def write_response(url):
    response = httpx.get(url)
    data = json.loads(response.text)
    file_name = url.rsplit('/', 1)[1]
    with open(f"{file_name}.json" , 'w') as f:
        json.dump(data ,f , indent=3 )

write_response("https://jsonplaceholder.typicode.com/photos")

