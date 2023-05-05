# a = ("id" , "name" , "nimadir")
#
# # "id , name , nimadir"
# print(','.join(a))

def f1(*args, **kwargs):
    print(kwargs)

f1(1 , 2,3,4,5 , num1 = 1)