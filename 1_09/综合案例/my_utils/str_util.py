def str_reverse(s):
    return s[::-1]

def substr(s,x,y):
    return s[x:y]

if __name__ == "__main__" :
    print(str_reverse("黑马程序员"))
    print(substr("黑马程序员",1,3))