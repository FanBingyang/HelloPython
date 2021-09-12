from bs4 import BeautifulSoup
import requests

# 伪造headers
headers = {
    'User-Agent':'Mozilla/5.0 (iPhone; CPU iPhone OS 11_0 like Mac OS X) AppleWebKit/604.1.38 (KHTML, like Gecko) Version/11.0 Mobile/15A372 Safari/604.1'
}

url ='https://www.tripadvisor.cn/Attractions-g60763-Activities-oa60-New_York_City_New_York.html'

wb_data = requests.get(url,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')

titles = soup.select('div.location')
imgs = soup.select('div.thumb.thumbLLR.soThumb > img')
for title,img in zip(titles,imgs):
    data = {
        'title':title.get_text(),
        'img':img.get('src')
    }
    print(data)

