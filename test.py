s = input("请输入字符")

if len(s) > 20 :
    print(s)
else:
    print("{0:->20}".format(s))