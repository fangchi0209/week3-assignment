


import urllib.request as request
import json
import ssl #為避免erro
ssl._create_default_https_context = ssl._create_unverified_context
src="https://padax.github.io/taipei-day-trip-resources/taipei-attractions.json"
with request.urlopen(src) as response:
    data=json.load(response) #利用json模組處理json資料格式

#景點名稱, 經度, 緯度, 第一張圖檔網址

plist=data["result"]["results"]
with open("data.txt", "w", encoding="utf-8") as file:
    for attractions in plist:
        s = attractions["stitle"]+","+attractions["longitude"]+","+attractions["latitude"]+","+ "http" + attractions["file"].split("http")[1]+"\n"
        file.writelines(s)

file.close()
# pic=data["result"]["results"]["attractions"]["file"]
# print(pic.split('http://'))


