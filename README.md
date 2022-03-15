![yande.reImg](https://assets.yande.re/assets/logo_small-418e8d5ec0229f274edebe4af43b01aa29ed83b715991ba14bb41ba06b5b57b5.png)  
# **yande.re-imgDownloader**
## 此程式是對於yande.re內的圖片進行搜索並下載的python爬蟲 &nbsp;**yande.re主頁：[yande.re](https://yande.re/post)**  
***
接下來的示範會以 &nbsp;**初音未來 (Hatsune Miku)** &nbsp;為主。  
&emsp;    
進入該網址後 可以看到網頁左邊有一個 **Search** 跟 **Tags**    
![Search](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/yandeSearch.png)   
![Tags](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/yandeTags.png)  
&emsp;     
**Search** 可以搜尋你想要的 **Tags**，通常可以先搜尋你想要的人物名字，再從推薦搜索下方可以找到更精確的 tags  
![mikurecommSearch](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/mikurecommSearch.png)  
&emsp;  
本程式中有用到 Tags 來進行人物的搜索，但 Tags 的取得需要用到該人物的網址

***
Tags 為 hatsune_miku，這是初音未來的第一頁 https://yande.re/post?page=1&tags=hatsune_miku&nbsp;，可以看到該網址後是 `tags=hatsune_miku`  
&emsp;   
程式中第一個動作就是會要求你們輸入的 tags，該tags就是要從網址中來判斷要輸入什麼tags   
***

