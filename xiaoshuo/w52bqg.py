import requests
import logging

import file


def __get_article_info(url, title, book_name):
    """
    :param url: 文章链接
    :param title: 文章标题
    :return:
    """
    response = requests.get(url)
    response.encoding = "GBK"

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find('div', id='content')
    content_text = str(content)

    content_text = content_text.replace('<br/><br/>', '\n')
    content_text = content_text.replace('<br/>', '\n')

    # 创建HTML解析器
    from html.parser import HTMLParser

    class MyHTMLParser(HTMLParser):
        def __init__(self):
            super().__init__()
            self.text = ""

        def handle_data(self, data):
            self.text += data

    # 解析HTML
    parser = MyHTMLParser()
    parser.feed(content_text)
    content_text = parser.text
    content_text = '\n'.join([line.lstrip() for line in content_text.split('\n')])
    content_text = '\n'.join([line.lstrip() for line in content_text.split('\n') if 'www.w52bqg.org' not in line])

    file.write(book_name, title, content_text)


def retry(callback, num=3):
    """
    重试函数
    :param callback:
    :param num:
    :return:
    """
    for index in range(num):
        try:
            callback()
            return
        except:
            print(f"重试第 {index}次")
            continue


def spider_book(book_id):
    """
    抓取指定 book_id 的书籍 \n
    书籍链接 https://www.52bqg.org/book_19589/
    :param book_id:  book_19589
    :return:
    """
    baseURL = f"https://www.52bqg.org/{book_id}/"
    response = requests.get(baseURL)
    from bs4 import BeautifulSoup

    soup = BeautifulSoup(response.text, 'html.parser')
    info = soup.find("div", id="info")
    book_name = info.h1.text

    dl_children = soup.find('dl').children

    flag = False
    continue_ = False
    for child in dl_children:
        if child.name == "center" or flag:
            flag = True
            a = child.a
            if a is not None and a.name == "a":
                if a.text == "第3010章 异变骤起" or continue_:
                    continue_ and retry((lambda: __get_article_info(baseURL + a["href"], a.text, book_name)))
                    continue_ = True
