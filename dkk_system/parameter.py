def get_para(goal):
    para={
        'BASE_URL':'https://newsapi.org/v2/everything',
        'MEDIA':['cnn', 
                 'reuters', 
                 'associated-press', 
                 'channelnewsasia.com'], #CNN、路透社、美聯社、亞洲新聞台
        
        'info_api':['https://opendata.ey.gov.tw/NewOpenData/json/34', 
                    'https://opendata.ey.gov.tw/NewOpenData/json/154', 
                    'https://opendata.ey.gov.tw/NewOpenData/json/153'], #政策、新聞、決議       
        'gemini_model':"gemini-2.5-flash-lite",
        'ChatGPT_model':"gpt-4o-mini",
        'resources_amount':[0, 0, 0, 0, 5, 5, 5], #政策、新聞、決議、國際新聞、路透社、美聯社、亞洲新聞台
        'expire_days':92,
        'update_days':3,
        'amount_per_category':200,
        'interim':3,
        'DATABASE_NAME':'questions_warehouse',
        'TABLE_NAME':['Keelung', 'New_Taipei', 'Taipei', 'Taipei', 'Taoyuan', 'Hsinchu', 'Miaoli', 'Taichung', 'Taichung',
                      'Changhua', 'Nantou', 'Yunlin', 'Chiayi', 'Tainan', 'Tainan', 'Kaohsiung', 'Pingtung', 'Taitung',
                      'Taitung', 'Hualien', 'Yilan', 'Lienchiang', 'Kinmen', 'Penghu', 'international', 'energy', 'disaster'],
        'county_list':['基隆','新北','臺北','台北','桃園','新竹','苗栗','臺中', '台中','彰化','南投','雲林', '嘉義','臺南', 
                        '台南', '高雄','屏東','臺東','台東','花蓮','宜蘭','連江','金門','澎湖','international', 'energy', 'disaster'],
        'disaster_types':['avalanche', 'earthquake', 'fire', 'explosion', 'extreme heat',
                          'flood', 'hazardous materials', 'hurricane', 'typhoon', 'debris flow', 
                          'pandemic', 'severe weather', 'thunderstorms', 'lightning strike',
                          'tornado', 'tsunami', 'volcano', 'wildfire', 'snowstorm'], 
        'disaster_rag_link':['avalanche', 'earthquakes', 'home-fires', 'explosions', 'heat', 
                            'floods', 'hazmat', 'hurricanes', 'hurricanes', 'landslides-debris-flow',
                            'pandemic', 'severe-weather', 'thunderstorms-lightning', 'thunderstorms-lightning',
                            'tornadoes', 'tsunamis', 'volcanoes', 'wildfires', 'winter-weather'],
        }
    
    return para[goal]