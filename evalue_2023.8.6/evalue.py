from decimal import *
from multiprocessing import Process, Queue

getcontext().prec = 10000000 # 指定计算精度为一千万位

def fact(n):
    if n == 0: return 1
    return n * fact(n - 1)

def compute_chunk(start, end, queue):
    chunk_sum = Decimal(0)
    for n in range(start, end):
        term = Decimal(1) / Decimal(fact(n))
        if term < Decimal(10) ** -500:
            break
        chunk_sum += term
    queue.put(chunk_sum)

if __name__ == '__main__':
    num_processes = 8
    chunk_size = 100 # 将计算分成大小为100的部分
    queue = Queue()

    # 启动进程计算各个部分的结果
    processes = []
    for i in range(num_processes):
        start = i * chunk_size
        end = start + chunk_size
        proc = Process(target=compute_chunk, args=(start, end, queue))
        proc.start()
        processes.append(proc)

    # 获取各个部分的结果并相加
    e = Decimal(0)
    for i in range(num_processes):
        e += queue.get()

    # 关闭进程
    for proc in processes:
        proc.join()

    print(e)