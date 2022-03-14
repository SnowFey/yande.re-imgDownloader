from asyncio import tasks
from bs4 import BeautifulSoup
from lxml import html
import pip._vendor.requests 
import requests
import os
import asyncio


headers = {
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9", 
    "Accept-Encoding": "gzip, deflate, br", 
    "Accept-Language": "zh-TW,zh;q=0.9", 
    "Host": "example.com",  #目標網站 
    "Sec-Fetch-Dest": "document", 
    "Sec-Fetch-Mode": "navigate", 
    "Sec-Fetch-Site": "none", 
    "Upgrade-Insecure-Requests": "1", 
    "User-Agent": "Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36" #使用者代理
}
session_requests = requests.session()

CharacterName = input("CharacterName:") #uruha_rushia
print("first page:1")
last1 = input("last page:")
print("Going")


async def directlink_largeimg(url):
    response = await loop.run_in_executor(None, requests.get, url)
    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("a", {"class": ["directlink largeimg","directlink smallimg"]})  #directlink largeimg "directlink medicineimg",
    thumbs = soup.find_all("a", {"class": "thumb"})

    image_links = [result.get("href") for result in results]  # 取得圖片來源連結
    imgID_hrefs = [thumb.get("href") for thumb in thumbs] #https://yande.re/post/show/ID
    #str(imgID_hrefs).replace("/post/show/","uruha_rushia_") 
    await download(image_links, imgID_hrefs)


async def download(image_links, imgID_hrefs):
    x = 0
    for index, link in enumerate(image_links):

        if not os.path.exists(str(CharacterName)):
            os.mkdir(str(CharacterName))  # 建立資料夾
 
        img = requests.get(link)  # 下載圖片 

        with open("./%s\\"%CharacterName + imgID_hrefs[x].replace("/post/show/","%s_"%CharacterName)  + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼

            print(imgID_hrefs[x].replace("/post/show/",""))
            x += 1


def main():
    tasks = []
    for i in range(1, int(last1) + 1):
        url = "https://yande.re/post?page=" + str(i) + "&tags=" + str(CharacterName)   #url=https://yande.re/post?page=1&tags=uruha_rushia
        tasks.append(loop.create_task(directlink_largeimg(url)))
    loop.run_until_complete(asyncio.wait(tasks))
    print("Downloaded Finish")


if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    main()
    