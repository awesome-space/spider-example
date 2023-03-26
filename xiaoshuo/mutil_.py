"""
实现并发爬取文章功能
"""

import multiprocessing


class MultiProcess:
    def __int__(self):
        self.workerQueue = []

    def add(self, worker, args):
        """
        追加任务
        :param args:
        :param worker:
        :return:
        """
        self.workerQueue.append(multiprocessing.Process(target=worker, args=(args,)))

    def run(self):
        """
        执行
        :return:
        """
        for worker in self.workerQueue:
            worker.start()

        for worker in self.workerQueue:
            worker.join()

    def success(self):
        """
        执行成功的回调函数
        :return:
        """
        pass

    def failure(self):
        """
        失败执行回调函数
        :return:
        """
        pass


if __name__ == "__main__":
    pass
