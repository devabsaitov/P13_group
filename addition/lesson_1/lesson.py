# iterable , iterator , generator

# iterable - list , tuple , dict , set
# iterator - iter()
# generator -
# =====================================
# import sys
# a = [i for i in range(10000)]
# print(sys.getsizeof(a))
#
# iterator = iter(a)
# print(sys.getsizeof(iterator))


# ========================================
import json
import sys



# print(sys.getsizeof(b))
# print(sys.getsizeof(a))

# def test():
#     with open('db/product.json', 'r') as f:
#         b = json.load(f)
#     for i in b:
#         yield i
#
# print(sys.getsizeof(test()))




