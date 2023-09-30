#可以修改 characters = string.ascii_letters + string.digits + string.punctuation 来更改密码所包含的类型
#也可以使用字符加法功能来生成
#修改 length 改变密码长度，characters 改变密码类型
#
#常见密码类型
#以下是常见密码类型在 Python 的 string 模块中对应的常量：
#字母（随机大小写）：string.ascii_letters
#特殊字符：string.punctuation
#大写字母：string.ascii_uppercase
#小写字母：string.ascii_lowercase
#数字：string.digits
#空格字符：string.whitespace（包括空格、制表符、换行等空白字符）
#Unicode 字符：string.printable（包括可打印字符的所有 ASCII 字符）


#注意：只有两处值得修改！！！！


import random
import string

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits+string.punctuation
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

num_of_passwords = 10  # 指定要生成的密码数量

random_passwords = []
for _ in range(num_of_passwords):
    random_password = generate_random_password()
    random_passwords.append(random_password)

# 打印生成的多个随机密码
for i, password in enumerate(random_passwords):
    print(f"随机生成的密码 {i+1}:", password)

input()