from bs4 import BeautifulSoup
import requests
import os
import re
#获取网页信息
def getHTMLText(url):
    '''
    此处写headers等参数，模拟用户登录
    如知乎、淘宝等需要用户登录才能访问页面信息
    kv={},在r=requests.get()中添加参数headers=kv
    '''
    try:
        r=requests.get(url,timeout=30)
        r.raise_for_status()#如果不是200，产生异常 requests.HTTPError
        r.encoding=r.apparent_encoding
        return r.text
    except:
        return "产生异常"
#获取图片信息
def getImgUrl(ulist,html):
    soup = BeautifulSoup(html, features='lxml')
    #匹配到图片时写法不唯一，具体网页具体分析。这里用的是正则表达式
    img_links = soup.find_all("img", {"src": re.compile('.*?\.jpg')})
    for link in img_links:
        ulist.append(link['src'])
#下载图片至本地
def loadImg(ulist,local):
    for img in ulist:
        path=local+img.split('/')[-1]
        try:
            if not os.path.exists(path):
                r=requests.get(img)
                with open(path,'wb') as f:
                    #HTTP响应内容的二进制形式，图片一般都是以二进制存储的
                    f.write(r.content)
                    f.close()
                    print('Saved %s' %img.split('/')[-1])
            else:
                print("文件已存在")
        except:
            print("爬取失败")

if __name__=="__main__":
    local='./image/'#存储的本机地址
    #如果本机地址不存在，则创建该路径
    if not os.path.exists(local):
        os.mkdir(local)
    url="http://www.ngchina.com.cn/photography/picture_story/4830.html"
    ulist=[]#暂存图片网址
    html = getHTMLText(url)
    getImgUrl(ulist,html)
    loadImg(ulist,local)