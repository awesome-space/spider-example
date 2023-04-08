import requests

import file
from bs4 import BeautifulSoup


def getArticleInfo(url):
    response = requests.get(url)
    response.encoding = "zh-CN"
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.find("div", id="neirong")
    pList = content.find_all("p")
    return "\n".join([e.text for e in pList])


if __name__ == '__main__':
    res = requests.get(f"https://www.51shucheng.net/guanchang/zhujingbanzhuren")
    res.encoding = "zh-CN"
    soup = BeautifulSoup(res.text, 'html.parser')
    articleTitle = soup.find("h1").text
    subTitles = soup.findAll("div", class_="mulu-title")
    subCategories = soup.findAll("div", class_="quanji")

    for index, item in enumerate(subCategories):
        subTitle = subTitles[index].find("h2").text
        file.write(articleTitle, f"{subTitle}", "")
        aList = item.findAll("a")
        for a in aList:
            content = getArticleInfo(a["href"])
            file.write(articleTitle, a.text, content)
