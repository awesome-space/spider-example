import w52bqg
from mutil_ import MultiProcess


def test(x, y):
    print(x, y)


if __name__ == '__main__':
    # book_1004 一代天骄
    # book_127664
    mp = MultiProcess()
    mp.add(w52bqg.spider_book, ("book_1004",))
    mp.run()
