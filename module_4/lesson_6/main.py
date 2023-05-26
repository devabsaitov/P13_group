nums1 = [1,3]
nums2 = [2]

l = sorted(nums1 + nums2)

len_m = len(l)
if len_m % 2 == 1:
    print(float(f"{l[len_m//2]: .5f}"))

else:
    result = float(f"{(l[len_m // 2] + l[len_m // 2 - 1]) / 2 : .5f}")
    print(result)
