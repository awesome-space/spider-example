"""
实现并发爬取文章功能
"""

import multiprocessing


def worker(q):
    """子进程的任务"""
    while True:
        data = q.get()
        print(f"Processing {data}")
        # 执行任务的代码


if __name__ == "__main__":
    # 创建一个队列用于进程间通信
    q = multiprocessing.Queue()

    # 创建子进程并启动
    p1 = multiprocessing.Process(target=worker, args=(q,))
    p2 = multiprocessing.Process(target=worker, args=(q,))

    p1.start()
    p2.start()

    # 往队列中添加任务
    for i in range(10):
        q.put(i)

    # 等待子进程执行完成
    p1.join()
    p2.join()
