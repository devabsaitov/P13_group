text = "(123)(tuu)kill(remove)power(off)"

# 1 version
# s = text.split("(")
# result = s[0]
# for i in s[1:]:
#     ind = i.find(")")
#     result += i[ : ind][::-1] + i[ind+1 : ]
# print(result)

# 2 version
print("".join([text.split('(')[0]] + list(map(lambda x :  x[:x.find(')')][::-1]+x[x.find(')')+1:], text.split('(')[1:]))))