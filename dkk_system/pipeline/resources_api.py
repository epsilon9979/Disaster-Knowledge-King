import requests
from parameter import get_para
from datetime import datetime
from Step import STEPS

class get_resource(STEPS):
    
    def process(self, data, database):
        print("\n in resource ##############################################################")
        round = data.pop()
        api_url = get_para('info_api')[round]
        num = int(get_para('resources_amount')[round]) 

        # 設定 HTTP 請求標頭（headers），這裡加入了 User-Agent 模擬瀏覽器，避免伺服器擋爬蟲或回傳 HTML。
        headers = {"User-Agent": "Mozilla/5.0"}
        response = requests.get(api_url, headers=headers)
        if response.status_code == 200:
            rawdata = response.json()[0:num]
        else:
            print(f"請求失敗，狀態碼：{response.status_code}")
        
        #判斷內容是否為縣市相關，並替原始資料集增添一項"所有相關縣市"
        county_list = get_para('county_list')
        table_name = get_para('TABLE_NAME')
        rawdata_2 = []
        for news in rawdata:
            content = news['內容']
            county = []
            for i in county_list:
                if i in content:
                    county.append( table_name[ county_list.index(i) ] )
            if len(county)>0:
                news['county'] = county
                rawdata_2.append(news)
        
        for news in rawdata_2:
            date = news['上版日期'] 
            y,m,d = map(int,date.split('-'))
            newdate = datetime(y+1911, m, d)
            news['上版日期'] = newdate
            if round == 1:
                news['來源網址'] = "https://www.ey.gov.tw/Page/6485009ABEC1CB9C"
            if round == 2:
                news['來源網址'] = "https://www.ey.gov.tw/Page/AE4885326ADF43DD"
                
        rawdata_2.append(round)
        print(rawdata_2)    
        return rawdata_2
    