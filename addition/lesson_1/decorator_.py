# decorator


# def multiple_to_two(func):
#     def inner(a , b):
#         returned_value = func(a , b)
#         return returned_value * 2
#     return inner

# def multiple(num):
#     def wrapper(func):
#         def inner(a , b):
#             if a > 10:
#                 returned_val = func(a,b)
#                 return returned_val * num
#         return inner
#     return wrapper
#
#




# def test1(func):
#     def inner(*args, **kwargs):
#         print("test1")
#         return func(*args, **kwargs)
#     return inner
#
#
# def test2(func):
#     def inner(*args, **kwargs):
#         print("test2")
#         return func(*args, **kwargs)
#     return inner

# @test1
# @test2
# def add(a, b):
#     print('add')
#     return a + b
#
# print(add(4, 6))
#
#
# @check_admin
# def add_admin():
#     pass
#
# add_admin({"id" : 1 , "role": 'ADMIN'})


