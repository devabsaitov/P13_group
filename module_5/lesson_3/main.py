

num = 687
p = sorted(map(int , list(str(num))))
print(int(''.join(map(str , p[::2]))) + int(''.join(map(str,p[1::2]))))