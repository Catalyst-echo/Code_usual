
import random
import string

def generate_random_password(length=12):
    """
    生成一个随机密码。

    参数:
    length (int): 密码的长度。默认为12。

    返回:
    str: 生成的随机密码。
    """
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

num_of_passwords = 500  # 指定要生成的密码数量

random_passwords = []
for _ in range(num_of_passwords):
    random_password = generate_random_password()
    random_passwords.append(random_password)

# 打印生成的多个随机密码
for i, password in enumerate(random_passwords):
    print(f"随机生成的密码 {i+1}:", password)
