from bs4 import BeautifulSoup
import requests
import time

url = 'https://www.tripadvisor.cn/Attractions-g60763-Activities-New_York_City_New_York.html'
# 连续爬多个网页，首先找出地址变化规律并构建
urls = ['https://www.tripadvisor.cn/Attractions-g60763-Activities-oa{}-New_York_City_New_York.html#FILTERED_LIST'.format(str(i)) for i in range(30,1230,30)]

def get_attractions(url,data=None):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text,'lxml')
    # titles = soup.select('#taplc_attraction_coverpage_attraction_0 > div > div:nth-of-type(1) > div > div > div.shelf_item_container > div:nth-of-type(1) > div.poi > div > div.item.name > a')
    # 拿到所有的标题
    titles = soup.select('div.detail > div > a.poiTitle') # 通过对元素的不同属性定位到唯一性
    # 拿到景区图片，在此图片不是一次性加载的真实地址，所以抓取到的是同一个连接
    imgs = soup.select('img[width="200"]') # 通过添加查询元素的属性来筛选想要的数据

    for title,img in zip(titles,imgs):
        data = {
            'title':title.get_text(),
            'img':img.get('src')
        }
        print(data)

def get_webs(url,data=None):
    wb_data = requests.get(url)
    time.sleep(2) # 每两秒请求一次,防止访问频繁，被网站反爬取拒绝
    soup = BeautifulSoup(wb_data.text,'lxml')
    # 拿到所有的标题
    titles = soup.select('div.listing_title  >  a') # 通过对元素的不同属性定位到唯一性
    # 拿到景区图片，在此图片不是一次性加载的真实地址，所以抓取到的是同一个连接
    imgs = soup.select('img.photo_image') # 通过添加查询元素的属性来筛选想要的数据

    for title,img in zip(titles,imgs):
        data = {
            'title':title.get_text(),
            'img':img.get('src')
        }
        print(data)

'''
# 提交假的cookie信息，骗过服务器的登录步骤，从而收藏该景点信息
# 构建需要用的headers，从网页检查里面复制过来的，自己先登录::>_<::
headers = {
    'Uesr-Argent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.67 Safari/537.36',
    'Cookie':'ServerPool=B; TART=%1%enc%3AecyOkT9T0NY92bn5BfVn6uGYSYwnOUk9hK1XliJ%2BoeDPFQ2UC2eS3QIdPC1T7KXqx4RT0S7Gmbs%3D; TAUnique=%1%enc%3A9qBPh2hdE%2BD%2Fw57j%2B9%2BSSwUMLLOQCHozuxQ76QzksenGTrNbZretrQ%3D%3D; TASSK=enc%3AAPNelFFAl7T9Wvd7vJGWSWsY5KegUSvyXF95TUTOok1iy5ldVw7ATDvDq%2FUjj3uK1qlJnp70s8rb4WsJLL93Gn4r7jIhDlt73Cc2KzUe3tYJEMAy0wRClwKVt8aRQCOSgQ%3D%3D; CM=%1%PremiumMobSess%2C%2C-1%7Ct4b-pc%2C%2C-1%7CRestAds%2FRPers%2C%2C-1%7CRCPers%2C%2C-1%7CWShadeSeen%2C%2C-1%7CTheForkMCCPers%2C%2C-1%7CHomeASess%2C%2C-1%7CPremiumSURPers%2C%2C-1%7CPremiumMCSess%2C%2C-1%7CRestPartSess%2C%2C-1%7CRestPremRSess%2C%2C-1%7CCCSess%2C%2C-1%7CPremRetPers%2C%2C-1%7CViatorMCPers%2C%2C-1%7Csesssticker%2C%2C-1%7CPremiumORSess%2C%2C-1%7Ct4b-sc%2C%2C-1%7CRestAdsPers%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS2%2C%2C-1%7Cb2bmcpers%2C%2C-1%7CPremMCBtmSess%2C%2C-1%7CPremiumSURSess%2C%2C-1%7CMC_IB_UPSELL_IB_LOGOS%2C%2C-1%7CLaFourchette+Banners%2C%2C-1%7Csess_rev%2C%2C-1%7Csessamex%2C%2C-1%7CPremiumRRSess%2C%2C-1%7CTADORSess%2C%2C-1%7CAdsRetPers%2C%2C-1%7CTARSWBPers%2C%2C-1%7CSPMCSess%2C%2C-1%7CTheForkORSess%2C%2C-1%7CTheForkRRSess%2C%2C-1%7Cpers_rev%2C%2C-1%7CSPMCWBPers%2C%2C-1%7CRBAPers%2C%2C-1%7CRestAds%2FRSess%2C%2C-1%7CHomeAPers%2C%2C-1%7CPremiumMobPers%2C%2C-1%7CRCSess%2C%2C-1%7CLaFourchette+MC+Banners%2C%2C-1%7CRestAdsCCSess%2C%2C-1%7CRestPartPers%2C%2C-1%7CRestPremRPers%2C%2C-1%7Csh%2C%2C-1%7Cpssamex%2C%2C-1%7CTheForkMCCSess%2C%2C-1%7CCCPers%2C%2C-1%7Cb2bmcsess%2C%2C-1%7CSPMCPers%2C%2C-1%7CPremRetSess%2C%2C-1%7CViatorMCSess%2C%2C-1%7CPremiumMCPers%2C%2C-1%7CAdsRetSess%2C%2C-1%7CPremiumRRPers%2C%2C-1%7CRestAdsCCPers%2C%2C-1%7CTADORPers%2C%2C-1%7CTheForkORPers%2C%2C-1%7CPremMCBtmPers%2C%2C-1%7CTheForkRRPers%2C%2C-1%7CTARSWBSess%2C%2C-1%7CPremiumORPers%2C%2C-1%7CRestAdsSess%2C%2C-1%7CRBASess%2C%2C-1%7CSPORPers%2C%2C-1%7Cperssticker%2C%2C-1%7CSPMCWBSess%2C%2C-1%7C; _ga=GA1.2.1263546022.1543459137; _gid=GA1.2.1598330286.1543459137; TAPD=tripadvisor.cn; __gads=ID=66734a6c073e7b69:T=1543459146:S=ALNI_MZwraFHo7bc75nGWE1zCtVD9u1D6A; BEPIN=%1%1675d7f8d5c%3Busr02t.daodao.com%3A10023%3B; TATravelInfo=V2*AY.2018*AM.12*AD.9*DY.2018*DM.12*DD.10*A.2*MG.-1*HP.2*FL.3*DSM.1543461899953*RS.1; SecureLogin2=3.4%3AAA0jf9ns6b8vw2hUzaP6tpnq8tXNu9owLPZHEZQ95DSYjxUjVtKuSYwPCJZjppm87eNTwf0IgdvRFXflIliqJ9MAN7CSRBaTZFqstkyGtehLERItncRGqDmc4RPnB4M3D9SJA99HHiRvmHpQYyR4JpYMaEh8LMQOgUyKkKgGvILPT8cBswAC3u%2BQ44f%2BrLAMLPrG5mOsDS0pdKp%2FSpWWZ6I%3D; TAAuth3=3%3A6e47ac2c9ca57bedee223b0ac57b7eac%3AAEVdSb1iniBWkcJ6U%2FU%2FxBq7jvouNzgzw4kDTUUsON1XS9K7AcMSdbWp16pyJM%2BQcDd9IR5iCrKfgFI0X%2FJkdFhEYolvagNfXbBcWrJh%2BOfWQPvfxXMclHg2Jrf6H%2F4b3i0bosqEPQu%2BsbjF7mMb9avBlF6y69divSJIpq3kwHBaPlGJaLzg2GApQZHwJDZujg%3D%3D; TAReturnTo=%1%%2FAttraction_Review-g60763-d1687489-Reviews-The_National_9_11_Memorial_Museum-New_York_City_New_York.html; roybatty=TNI1625!AKa%2FvLcj24TrFl0BgeR1fsgC2%2BjWHDTTTu14SiBLXMoRApdv3QBqvIsWe86CDp9uYFPsqMC%2BD9nwJA%2BQcJxuJnmQPcmMdGvct%2BAsk0XyZwJOXaXuoP6QtOKrSDjDZK5CvipAMoTlLc0Vuwqm2YXIzL8NFrzkKf4rEwlpJSQ6td%2Br%2C1; _gat_UA-79743238-4=1; TASession=%1%V2ID.6148AB87E0F0080BB020F990E676C063*SQ.180*LP.%2FLangRedirect%3Fauto%3D3%26origin%3Dzh%26pool%3DB%26returnTo%3D%252FAttractions-g60763-Activities-New_York_City_New_York%5C.html*PR.39766%7C*LS.MetaPlacementAjax*GR.6*TCPAR.5*TBR.97*EXEX.84*ABTR.3*PHTB.34*FS.27*CPU.0*HS.recommended*ES.popularity*AS.popularity*DS.5*SAS.popularity*FPS.oldFirst*TS.365E50A0AE76014759C62B9ACD8BC613*LF.zhCN*FA.1*DF.0*IR.3*OD.zh*FLO.60763*TRA.false*LD.1687489; TAUD=LA-1543459127762-1*RDD-1-2018_11_29*HDD-2771829-2018_12_09.2018_12_10.1*LD-3619201-2018.12.9.2018.12.10*LG-3619203-2.1.F.'
}

url_save = 'https://www.tripadvisor.cn/Saves/1438042'
wb_data = requests.get(url_save,headers=headers)
soup = BeautifulSoup(wb_data.text,'lxml')
print(soup)
'''
# get_webs('https://www.tripadvisor.cn/Attractions-g60763-Activities-oa30-New_York_City_New_York.html#FILTERED_LIST')

for single_url in urls:
    # print(single_url)
    get_webs(single_url)