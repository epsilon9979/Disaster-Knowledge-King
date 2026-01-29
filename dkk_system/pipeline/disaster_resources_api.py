import requests
from bs4 import BeautifulSoup
from parameter import get_para
from dotenv import load_dotenv
from datetime import datetime
from Step import STEPS
import os

load_dotenv()

class get_resource_dkk(STEPS):
    
    def process(self, data, database):
        print("\n in resource ##############################################################")
        round = data.pop()

        API_KEY = os.getenv('NEWS_APIKEY')
        BASE_URL = get_para('BASE_URL') 
        media = get_para('MEDIA')[round-3]
        num =  get_para('resources_amount')[round] 

        def scrapt(link):
            response = requests.get(link)
            if response.status_code == 200:
                soup = BeautifulSoup(response.content, 'html.parser')  # 解析 HTML 內容
                paragraphs = soup.find_all('p') # 這裡可以根據需要提取具體的內容。 例如，提取所有的段落文字
                material = ''
                for paragraph in paragraphs:
                    a = paragraph.get_text()
                    material = material + a
                return material
            else:
                print("無法訪問網頁，狀態碼:", response.status_code)

        disaster_news = []
        disaster_types = get_para('disaster_types')
        disaster_rag_link = get_para('disaster_rag_link')
        for type in disaster_types:
            if round == 6:
                params = {
                    'q': f'{type}',  # 依照文章關鍵字
                    'domains': media,  
                    'apiKey': API_KEY,  # API 金鑰
                    'language': 'en',  # 語言設置
                    'sortBy': 'publishedAt',  # 按發佈時間排序(relevancy, popularity, publishedAt)
                    'pageSize': num  # 返回的新聞數量
                }
            else:
                params = {
                    'q': f'{type}',  # 依照文章關鍵字
                    'sources': media,  
                    'apiKey': API_KEY,  # API 金鑰
                    'language': 'en',  # 語言設置
                    'sortBy': 'publishedAt',  # 按發佈時間排序(relevancy, popularity, publishedAt)
                    'pageSize': num  # 返回的最大新聞數量
                }

            rag_link = disaster_rag_link[disaster_types.index(type)]
            response = requests.get(BASE_URL, params=params)
            if response.status_code == 200:
                data = response.json()
                for news in data['articles']:
                    if type in news['title'].lower():  #二次新聞過濾，確保文章主題是指定災害類別
                        link = news['url']
                        rawdate = news['publishedAt'] # 2024-09-27T10:50:34Z
                        article = scrapt(link)
                        date = datetime.strptime(rawdate, "%Y-%m-%dT%H:%M:%SZ")
                        material = {}
                        material['內容'] = article
                        material['上版日期'] = date
                        material['county'] = ["disaster"]
                        material['標題'] = news['title']
                        material['來源網址'] = link
                        material['rag_link'] = rag_link ###########################################
                        disaster_news.append(material)
                        print(material, "\n\n")
                        continue
                
            else:
                print(f"請求失敗，狀態碼: {response.status_code}")
                print("錯誤詳情:", response.json())
            
        disaster_news.append(round)            
        # print(disaster_news)
        return disaster_news