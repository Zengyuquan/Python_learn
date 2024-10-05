import re

# s = "itheima @@ !# !python _+_+()#^R*&( 125221561a  itcast"
#
# result = re.findall(r'\d', s)
# print(result)
#
# result = re.findall(r'\W', s)
# print(result)
#
# result = re.findall(r'[a-zA-Z]', s)
# print(result)

# 匹配账号 只能由字母和数字组成，长度限制6到10位
# r = '^[0-9a-zA-Z]{6,10}&'
# s = '123456abcs'
# print(re.findall(r, s))

# 匹配QQ账号，要求纯数字，长度5-11，第一位不为0
# r = '^[1-9][0-9]{4,10}$'
# s = '12345678'
# print(re.findall(r, s))

# 匹配邮箱地址    只允许qq, 163, gmail这三种邮箱地址
r = r'(^[\w-]+(\.[\w-]+)*@(qq|163|gamil)(\.[\w-]+)+$)'
s = 'a.b.c.d.e.fg@qq.com.a.z.c.d.e'
print(re.match(r, s))