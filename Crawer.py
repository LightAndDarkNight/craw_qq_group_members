from selenium import webdriver
from bs4 import BeautifulSoup
import time
import os


def craw(number):

    # 打开浏览器
    driver = webdriver.Firefox()
    # 地址
    url = "https://qun.qq.com/member.html#gid="+number
    driver.get(url)
    check=False
    while(not check):
        try:
            driver.current_url
            # 获取源码
            res = driver.page_source
            time.sleep(1)
        except:
            check=True

    # 保存源码
    with open('html.txt', 'w', encoding='utf-8') as f:
        f.write(res)
    f.close()

    # 读取
    with open('html.txt', 'r', encoding='utf-8') as f:
        res = f.read()
    f.close()
    soup = BeautifulSoup(res, "lxml")
    #找到成员元素列表
    menber_list_tag=soup.find_all("tr",{"class":"mb"})
    menber_list={}
    count=0
    for menber in menber_list_tag:
        #获取序号
        no=menber.find("td",{"class":"td-no"}).contents[0]
        name=menber.span.contents[0].strip()
        if menber.find("td",{"class":"td-card"}).span.span:
            group_name = menber.find("td", {"class": "td-card"}).span.span.contents[0].strip()
        else:
            group_name=menber.find("td", {"class": "td-card"}).span.contents[0].strip()
        if group_name=="":
            group_name="未设置"

        qq=menber.attrs['class'][1].replace("mb","")
        gender=menber.find_all("td")[5].contents[0].strip()
        menber_list[no]={
            "qq昵称":name,
            "群昵称":group_name,
            "qq号":qq,
            "性别":gender
        }
    os.remove('html.txt')
    return menber_list


if __name__=='__main__':
    men_list=craw("263445621")
    print(men_list)
    print(len(men_list))