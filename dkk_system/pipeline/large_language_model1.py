from google import genai
from google.genai import types
from pydantic import BaseModel
from Step import STEPS
from parameter import get_para
from dotenv import load_dotenv
import os

class question(BaseModel):
    Question: str
    Option_A: str
    Option_B: str
    Option_C: str
    Option_D: str
    Correct_Answer: str
    Explanation: str

class manufacture(STEPS):
    
    def process(self, data, database):
        print("\n in manufacture ##############################################################")
        load_dotenv()
        API_key = os.getenv("GEMINI_API_KEY")
        gemini_model = get_para('gemini_model')
        county_list = get_para('county_list')
        table_name = get_para('TABLE_NAME')

        def gemini_normal(content):
            response = chat.send_message(content, config = types.GenerateContentConfig(
                response_mime_type = "application/json",
            ))
            # answer = response.text.strip("\n").strip()
            answer = response.text
            return answer, response.usage_metadata.total_token_count
        
        def gemini_search(content):
            response = chat.send_message(content, config = types.GenerateContentConfig(
                tools = [
                    types.Tool(
                        google_search = types.GoogleSearch()
                    )
                ],
            ))
            answer = response.text
            return answer, response.usage_metadata.total_token_count

        def gemini_final(content):
            response = chat.send_message(content, config = types.GenerateContentConfig(
                response_schema = list[question],
                response_mime_type = "application/json",
            ))
            # answer = response.text.strip("\n").strip()
            answer = response.text
            return answer, response.usage_metadata.total_token_count

        series = []
        for news in data:
            for city in news['county']:
                county = county_list[ table_name.index(city) ]
                token_usage = 0
                content = news['內容']
                client = genai.Client(api_key=API_key)
                chat = client.chats.create(model=gemini_model)
                
                prompt1 = f"你現在是宣傳公關，閱讀{content}，請整理出「四大重點」以及「跟{county}的關聯」"
                prompt2 = f"根據這五個要點，幫我出一題選擇題，「目的是讓使用者知道發生什麼事」且「要跟{county}有關」。架構包含問題、四個選項、正確答案。"
                prompt3 = "接著給我答案解釋，90字以內，並務必確保文句中沒有「選項」和「A、B、C、D」等字眼"
                prompt4 = "把「答案解釋」加在上述已完成之選擇題的最後，並回傳 '問題', '選項A', '選項B', '選項C', '選項D', '正確答案' 和 '答案解釋'."
                        
                order = prompt1
                response1 = gemini_search(order)
                token_usage += response1[1]
                response2 = gemini_normal(prompt2)
                token_usage += response2[1]
                response3 = gemini_normal(prompt3)
                token_usage += response3[1]
                response4 = gemini_final(prompt4)
                token_usage += response4[1]
                print("response4: ", response4[0]) ######################################
                print("Total token usage: ", token_usage)
                
                questions = {}
                questions['rawquestion'] = response4[0]
                questions['county'] = news['county'][0]
                questions['time'] = news['上版日期']
                questions['title'] = news['標題']
                questions['url'] = news['來源網址']
                series.append(questions)

        # print(series)

        return series        