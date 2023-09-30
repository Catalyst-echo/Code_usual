>`.sh` is a file can run in HPC

## Project Introduction:

This project is a password generator implemented in Python, utilizing multi-processing techniques to generate multiple random passwords. Below is an overview of the main components and functionalities of the project:

1. **Password Generation Function** `generate_random_password(length=12)`:
   - This function takes an optional parameter `length` to specify the length of the generated password, with a default of 12 characters.
   - It defines the character set that passwords can include using `string.ascii_letters` and `string.digits`, encompassing uppercase letters, lowercase letters, and digits.
   - Random characters are chosen to construct a password of the specified length, which is then returned as a password string.

2. **`generate_passwords(num_of_passwords)` Function**:
   - This function accepts a parameter `num_of_passwords` to determine the number of passwords to generate.
   - It iteratively generates the specified number of random passwords, stores them in a list, and returns the list.

3. **Main Program (`if __name__ == "__main__":` Section)**:
   - Defines the total number of passwords to generate, set to 50,000 passwords in this instance.
   - Utilizes `multiprocessing.cpu_count()` to retrieve the number of CPU cores on the computer to distribute work among multiple processes.
   - Creates a process pool (`multiprocessing.Pool`) and distributes the password generation task evenly among multiple processes, employing the `pool.map` method to execute the `generate_passwords` function.
   - Merges the generated passwords and stores them in a list named `random_passwords`.
   - Prints the multiple random passwords generated for user reference.

The primary objective of this project is to efficiently generate a large number of random passwords. By employing multi-processing techniques, it leverages the multi-core processing capabilities of the computer to enhance password generation speed. Users can control the number of passwords generated by modifying the `num_of_passwords` variable and adjust the password length as needed. The generated passwords can be used for various applications such as secure logins, testing, and simulation scenarios. This project demonstrates how to execute parallel tasks using Python and the multiprocessing library to improve performance.

***
# 中文
这个项目是一个密码生成器，它使用Python编程语言和多进程技术生成多个随机密码。以下是项目的主要组成部分和功能介绍：

1. 密码生成函数 `generate_random_password(length=12)`：
   - 该函数接受一个可选参数 `length`，用于指定生成的密码长度，默认为12个字符。
   - 使用 `string.ascii_letters` 和 `string.digits` 定义了密码可能包含的字符集，即大写字母、小写字母和数字。
   - 随机选择字符并构建指定长度的密码，然后返回密码字符串。

2. `generate_passwords(num_of_passwords)` 函数：
   - 这个函数接受一个参数 `num_of_passwords`，用于指定要生成的密码数量。
   - 它迭代生成指定数量的随机密码，将它们存储在一个列表中，然后返回该列表。

3. 主程序（`if __name__ == "__main__":` 部分）：
   - 定义了要生成的密码总数 `num_of_passwords`，在这里设置为50000个密码。
   - 使用 `multiprocessing.cpu_count()` 来获取计算机的CPU核心数量，以便将工作分配给多个进程。
   - 创建了一个进程池（`multiprocessing.Pool`），并根据CPU核心数量分配工作。
   - 将密码生成任务均匀分配给多个进程，并使用 `pool.map` 方法执行密码生成函数 `generate_passwords`。
   - 合并生成的密码，将它们存储在一个名为 `random_passwords` 的列表中。
   - 打印生成的多个随机密码，以便用户查看。

这个项目的主要目的是以高效的方式生成大量随机密码。通过使用多进程技术，它可以利用计算机的多核处理能力，提高密码生成速度。用户可以通过修改 `num_of_passwords` 变量来控制生成的密码数量，并可以根据需要修改密码长度。生成的密码可以用于各种应用，如安全登录、测试和模拟等场景。这个项目展示了如何使用Python和多进程库来执行并行任务，以提高性