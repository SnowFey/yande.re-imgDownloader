import os, asyncio

import requests, aiohttp

from bs4 import BeautifulSoup
from lxml import html

async def download(link:str, imgID:list, tags, session):
    async with session.get(link) as response:
        with open(f"./{tags}/{tags}{imgID}.jpg", mode="wb") as file:
            file.write(await response.read())

async def main():
    tags = input("tags: ")
    last_page = int(input(f"Starts from page 1, \nEnter last page: "))

    print("Strat fetching")

    CharacterName = tags.replace("%28","").replace("%29","")

    if not os.path.exists(CharacterName):
        os.mkdir(CharacterName)  # 建立資料夾

    for i in range(1, last_page+1):
        url = f"https://yande.re/post?page={i}tags={tags}"
        print(f"requesting to: {url}")


        # I will find a solution to replace this garbage down here
        response = await loop.run_in_executor(None, requests.get, url)


        soup = BeautifulSoup(response.text, "lxml")
        results = soup.find_all("a", {"class": ["directlink largeimg","directlink smallimg"]}) 
        thumbs = soup.find_all("a", {"class": "thumb"}) 
        image_links = [result.get("href") for result in results]  # 取得圖片來源連結
        imgID_hrefs = [thumb.get("href") for thumb in thumbs] #/post/show/ID

        tasks = []
        async with aiohttp.ClientSession() as session:
            session = session
            for _, link in enumerate(image_links):
                for imgID in imgID_hrefs:
                    imgID = imgID[11:]
                    tasks.append(loop.create_task(await download(link, imgID ,tags, session)))
        await asyncio.gather(*tasks)
    session.close()
    print("Downloaded Finished")

if __name__ == "__main__":
    loop = asyncio.new_event_loop()
    asyncio.set_event_loop(loop)
    loop.run_until_complete(main())
