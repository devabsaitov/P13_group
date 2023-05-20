# http://10.10.1.118:8000/
# http://kun.uz


# IP -> 10.10.1.118
# domain -> kun.uz   DNS
# port -> 8000

#
# from bs4 import BeautifulSoup
#
#
# html_doc = """
# <html><head><title>The Dormouse's story</title></head>
# <body>
# <p class="title"><b>The Dormouse's story</b></p>
#
# <p class="story">Once upon a time there were three little sisters; and their names were
# <a href="http://example.com/elsie" class="sister" id="link1">Elsie</a>,
# <a href="http://example.com/lacie" class="sister" id="link2">Lacie</a> and
# <a href="http://example.com/tillie" class="sister" id="link3">Tillie</a>;
# and they lived at the bottom of a well.</p>
#
# <p class="story">...</p>
#
# </html>
# """
#
# soup = BeautifulSoup(html_doc , "html.parser")
#
# for i in soup.find_all("a"):
#     print(i.text)
# import time

# import httpx
# from bs4 import BeautifulSoup
#
# response = httpx.get("https://daryo.uz/")
# html_code = response.text
#
# soup = BeautifulSoup(html_code, "html.parser")
#
# url = soup.find_all("div", {"class": "article__pic"})[1].find("img").get('src')
#
#
#
#
# image_url = f"https://daryo.uz{url}"
# response = httpx.get(image_url)
# time = time.strftime("%Y-%m-%d %H:%M:%S")
#
# with open(f"{time}.png" , "wb") as f:
#     f.write(response.content)






