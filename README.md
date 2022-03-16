![yande.reImg](https://assets.yande.re/assets/logo_small-418e8d5ec0229f274edebe4af43b01aa29ed83b715991ba14bb41ba06b5b57b5.png)
![pythonImg](https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/160px-Python-logo-notext.svg.png)    
# **yande.re-imgDownloader**
此程式是對於yande.re內的圖片進行搜索並下載的python爬蟲  
**yande.re主頁：[yande.re](https://yande.re/post)**
***
接下來的示範會以知名人物 &nbsp;**初音未來 (Hatsune Miku)** &nbsp;為主。   
進入主頁後 可以看到網頁左邊有一個 **Search** 跟 **Tags**  

![Search](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/yandeSearch.png)   
![Tags](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/yandeTags.png)  
&emsp;     
&emsp;   
**Search** 可以搜尋你想要的 **Tags**，通搜尋你想要的人物名字，再從推薦搜索下方可以找到更精確的 tags  

![miku_recommSearch](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/mikurecommSearch.png)
![miku_highlight](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/mikuhighlight.png)   
*** 
本程式中會先用到 Tags 來進行人物的搜索，再進行下載圖片的動作，但 Tags 的取得需要用到該人物的網址  
Search Tags 為 hatsune_miku，這是初音未來的第一頁 `https://yande.re/post?page=1&tags=hatsune_miku`   
可以看到該網址後是 `tags=hatsune_miku`   

程式中第一個動作就是會要求你們輸入的 tags，而該tags就是要從網址中來判斷要輸入什麼tags  
&emsp;    
執行程式時，如果要搜尋初音未來就要輸入 tags:`hatsune_miku`  
![tags_hatsune_miku](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/tags_hatsune_miku.png)   
&emsp;  
&emsp;    
有一些tags會有包含括號，像是這些 tags   
![tagsS](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/tagsS.png)

點進 hibiki_(kancolle) 作為示範   
第一頁網址為 `https://yande.re/post?page=1&tags=hibiki_%28kancolle%29`  
會發現網址後是 `tags=hibiki_%28kancolle%29`  
括號轉換成 %28 , %29，搜尋時一樣使用 tags:`hibiki_%28kancolle%29`  
但在命名資料夾名稱時，會使用 str.replace   
變成 `hibiki_kancolle` ，這樣資料夾名稱就不會有 %28 , %29 等符號    
![tags_hibiki](https://raw.githubusercontent.com/SnowFey/yande.re-imgDownloader/main/md_img/tags_hibiki.png)   