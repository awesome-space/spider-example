def write(book_name, title, content_text):
    # 将结果写入文件
    with open(f'{book_name}.txt', 'a', encoding='utf-8') as f:
        f.write(title + "\n")
        f.write(content_text)
    print("%s 抓取成功" % title)
