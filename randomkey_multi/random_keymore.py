import random
import string
import multiprocessing

def generate_random_password(length=12):
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    return password

def generate_passwords(num_of_passwords):
    random_passwords = []
    for _ in range(num_of_passwords):
        random_password = generate_random_password()
        random_passwords.append(random_password)
    return random_passwords

if __name__ == "__main__":
    num_of_passwords = 50000

    # 分配工作给多个进程
    num_processes = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(processes=num_processes)
    passwords_per_process = num_of_passwords // num_processes
    results = pool.map(generate_passwords, [passwords_per_process] * num_processes)

    # 合并生成的密码
    random_passwords = [password for sublist in results for password in sublist]

    # 打印生成的多个随机密码
    for i, password in enumerate(random_passwords):
        print(f"随机生成的密码 {i + 1}:", password)