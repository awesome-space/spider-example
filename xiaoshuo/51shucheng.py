import requests

if __name__ == '__main__':
    res = requests.get(f"https://www.51shucheng.net/guanchang/zhujingbanzhuren")
    res.encoding = "zh-CN"

    from bs4 import BeautifulSoup

    soup = BeautifulSoup(res.text, 'html.parser')
    articleTitle = soup.find("h1")
    print(articleTitle.text)
    subTitles = soup.findAll("div", class_="mulu-title")
    subCategories = soup.findAll("div", class_="quanji")
    print(subCategories)