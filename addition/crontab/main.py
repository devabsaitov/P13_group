
"""
crontab -> time ni boshqarish
minut -> 0-59
hour -> 0-23
day -> 1-31
month -> 1-12

*/30 8-10 * * 5 -> 8 dan boshlab "menu yaratildi"
har kuni soat 8 dan boshlab 10 gacha har yarim soatda ishlasin
"""

# * * * * *

if __name__ == '__main__':
    import os
    code = """

with open("/home/dilshod/PycharmProjects/P13_group/addition/crontab/test/test.txt", "a") as f:
    for i in range(10):
        if i % 2 == 0:
            f.write(f"{i} ")
        """
    if not os.path.exists("test"):
        os.mkdir("test")
    with open("test/test.py" , 'w') as f:
        f.write(code)

    import addition.crontab.test.test
