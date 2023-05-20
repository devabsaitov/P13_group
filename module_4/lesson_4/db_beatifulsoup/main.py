import os

from bs4 import BeautifulSoup
import time
import httpx

def get_data():
    html_code = httpx.get("https://kun.uz/").text
    soup = BeautifulSoup(html_code, "html.parser")
    data_list = soup.find_all("div", {"class": "small-news"})

    for i in data_list:
        img_url = i.img.get('src')
        img_response = httpx.get(img_url)
        created_at = i.span.text
        title = i.find('a', {'class':"small-news__title"}).text
        img_name = f"images/{img_url.rsplit('/', 1)[1]}"
        with open( img_name, "wb") as f:
            f.write(img_response.content)
            # f.write(img_response.content)


get_data()

