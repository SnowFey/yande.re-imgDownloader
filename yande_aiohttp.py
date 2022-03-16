from aiohttp import ClientSession
from bs4 import BeautifulSoup
from lxml import html
import asyncio, os, requests

#          https://yande.re/post?page=(i)&tags=(Tags)
# Example: https://yande.re/post?page=1&tags=Mochizuki_anna

tags = input("tags: ")

CharacterName = tags.replace("%28","").replace("%29","")
print(f"fileName:{CharacterName}")
print("first page: 1")

last1 = int(input("last page: "))

print("Going")

if not os.path.exists(str(CharacterName)):
    os.mkdir(str(CharacterName))  # 建立資料夾

async def main():
    weblinks = [] 
    for page in range(1, (last1+1)):
        weblinks.append(f"https://yande.re/post?page={page}&tags={tags}")

    async with ClientSession() as session:
        tasks = [asyncio.create_task(directlink_largeimg(weblink, session)) for weblink in weblinks]
        await asyncio.gather(*tasks)

async def directlink_largeimg(weblink, session):
    async with session.get(weblink) as response:  #非同步發送請求
        html_text = await response.text()
        soup = BeautifulSoup(html_text, "lxml")  # 解析HTML原始碼
 
        results = soup.find_all("a", {"class": ["directlink largeimg","directlink smallimg"]}) 
        thumbs = soup.find_all("a", {"class": "thumb"})

        image_links = [result.get("href") for result in results]  # 取得圖片來源連結
        imgID_hrefs = [thumb.get("href") for thumb in thumbs] #/post/show/ID
        
        await download(image_links, imgID_hrefs)

async def download(image_links, imgID_hrefs):
    x = 0
    for index, link in enumerate(image_links):

        img = requests.get(link)  # 下載圖片 

        with open("./%s\\"%CharacterName + imgID_hrefs[x].replace("/post/show/","%s_"%CharacterName)  + ".jpg", "wb") as file:  # 開啟資料夾及命名圖片檔
            file.write(img.content)  # 寫入圖片的二進位碼

            print(imgID_hrefs[x].replace("/post/show/",""))
            x += 1

if __name__ == "__main__":
    loop = asyncio.get_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
    print("Downloaded Finish")