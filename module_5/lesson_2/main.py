strs = ["alic3","bob","3","4","00000"]

"""
[5 , 3 , 3 , 4 , 0]
"""

print(max(int(i) if i.isdigit() else len(i) for i in strs))
print(max({i: int(i) if i.isdigit() else len(i) for i in strs}.values()))
print(max(map(lambda x : len(x) if not x.isdigit() else int(x), strs)))