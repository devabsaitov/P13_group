import json
data = [
    {
        "v": 1
    },
    {
        "v": 2
    }
]

with open('my_json.json', 'r') as f:
    try:
        d = json.load(f)
    except:
        d = []

with open('my_json.json', 'w') as f:
    d.extend(data)
    json.dump(d , f , indent=3)

# ======================================================================

# httpx
import httpx

response = httpx.get("https://jsonplaceholder.typicode.com/posts").text
response= json.loads(response)
response.append('1')
print(response)



# ======================================================================

# Decoratorni oldin tushunishimiz kerak bo'lgan terminlar

# step 1  -> O'zgaruvchilarga funksiyalarni belgilash


def plus_one(number):
    return number + 1

add_one = plus_one
add_one(5)

# step 2   -> Tashqi funksiyalar ichida funksiyalarni ishlatish

def plus_one(number):

    # -------------------------
    def add_one(number):
        return number + 1
    # ------------------------

    result = add_one(number)
    return result

plus_one(4)

# step 3

def plus_one(number):
    return number + 1

def function_call(function):
    number_to_add = 5
    return function(number_to_add)

function_call(plus_one)


# step 4

def hello_function():
    def say_hi():
        return "Hi"
    return say_hi

hello = hello_function()
hello()

# ============================================================================

# Dekoratorlarni yaratish

def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


def say_hi():
    """Salom beruvchi function"""
    return 'hello there'

decorate = uppercase_decorator(say_hi)


# 2 version
def uppercase_decorator(function):
    def wrapper():
        func = function()
        make_uppercase = func.upper()
        return make_uppercase

    return wrapper


@uppercase_decorator
def say_hi():
    """Salom beruvchi function"""
    return 'hello there'

print(say_hi())


# task : har qanday funksiyani qancha vaqtda ishini tugashini hisoblovchi decorator yarating






