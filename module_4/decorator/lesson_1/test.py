# matrix = [
#              [9, 2, 3, 5],  # 19
#              [5, 8, 2, 1],  # 16
#              [1, 6, 8, 2],  # 17
# ]
#
#
# print(sorted(matrix , key=sum))
# print(sorted(matrix , key=lambda x : sum(x)))

# =================================================================

# nums = [1, 1, 0, 1, 1 ,1, 1, 1, 1, 0 ,1 , 1, 1, 0, 1]
#
# print(len(max(''.join(map(str , nums)).split('0'))))

# =============================================================

# from math import ceil, sqrt
#
# n = c = int(input())
#
# if not n % 2:
#     print(2 , end=' ')
#
#
# l = set()
# for i in range(3 , ceil(sqrt(c)) , 2):
#     while not c % i:
#         l.add(str(i))
#         c //= i
#
# print(' '.join(sorted(list(l))))





