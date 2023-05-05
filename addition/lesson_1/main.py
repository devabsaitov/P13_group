# 1)iterator va generator

# ------------------- '''iterators''' ----------------------------
# iterable and iterator are different.
# iterable -> () , [] , {} , dict()                         --joriy joyni saqlamaydi
# iterator -> iter() shu function yordamida object olinsa   --joriy joy saqlanib qolinadi

"""
        tup = ('a', 'b', 'c', 'd', 'e')

        tup_iter = iter(tup)

        print("Inside loop:")
        for index, item in enumerate(tup_iter):
            print(item)
            if index == 2:
                break

        print("Outside loop:")
        print(next(tup_iter))
        print(next(tup_iter))
"""


# ----------------------------- '''generator''' ----------------------------------
from time import sleep


def test(size):
    x = 0
    while size > x:
        x +=1
        yield x



for i in test(10):
    print(i)


# ---------------------------------------------------------
import sys
'''etibor bering ikkala holat bir xil kurinishi mumkin '''
nums_squared_lc = [num**2 for num in range(6)] # -> ro'yhat tuzish
nums_squared_gc = (num**2 for num in range(6)) # -> generator yaratish uchun
print(nums_squared_lc)
print(nums_squared_gc)

'''generator ni yaratishdan maqsad kam joy egalashi

sinab kuramiz :'''
def clone_range(start , stop = None):
    if not stop:
        stop , start = start , 0
    while start < stop:
        yield start
        start += 1

l = [10,11,12,13,14,15,16,17,18,19,20,21,22]
print(sys.getsizeof(l))
print(sys.getsizeof(clone_range(10 , 1000)))

# b = [1,2,3,4,5,6,7,8,9,10,11,12]
# print(sys.getsizeof(b))
# print(sys.getsizeof(r))


numbers = [100, 200, 300]
iterator1 = iter(numbers)
iterator2 = iter(iterator1)
iterator3 = iter(iterator2)

# Check if they are the same object
print(iterator1 == iterator2)


def test():
    return list(range(50))
def test1():
    for i in range(50):
        yield i


l = [test() , test1()]
l1 = []
print(test())        # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
print(list(test1())) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49]
print(sys.getsizeof(test())) # size - 80056
print(sys.getsizeof(test1())) # size - 16








