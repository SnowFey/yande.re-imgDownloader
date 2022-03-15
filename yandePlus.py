import os, asyncio

import aiohttp

from bs4 import BeautifulSoup
from lxml import html

#          https://yande.re/post?page=(i)&tags=(Tags)
# Example: https://yande.re/post?page=1&tags=Mochizuki_anna
tags = input("tags: ")

CharacterName = tags.replace("%28","").replace("%29","")
print(f"fileName:{CharacterName}")
print("first page: 1")

last1 = int(input("last page: "))

print("Going")

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

async def directlink_largeimg(url):
    soup = BeautifulSoup(response.text, "lxml")

    results = soup.find_all("a", {"class": ["directlink largeimg","directlink smallimg"]}) 
    thumbs = soup.find_all("a", {"class": "thumb"}) 

    image_links = [result.get("href") for result in results]  # 取得圖片來源連結
    imgID_hrefs = [thumb.get("href") for thumb in thumbs] #/post/show/ID
    await download(image_links, imgID_hrefs)

def main():
    tasks = []
    for i in range(1, (last1+1)):
        # url = https://yande.re/post?page=1&tags=uruha_rushia
        url = f"https://yande.re/post?page={i}tags={tags}"
        tasks.append(loop.create_task(directlink_largeimg(url)))
    print("Downloaded Finish")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    
