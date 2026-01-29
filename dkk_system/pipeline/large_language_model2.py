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
    Response_Method: str

class manufacture_plus(STEPS):
    
    def process(self, data, database):
        print("\n in manufacture ##############################################################")
        load_dotenv()
        API_key = os.getenv("GEMINI_API_KEY")
        gemini_model = get_para('gemini_model')

        def gemini_normal(content):
            response = chat.send_message(content, config = types.GenerateContentConfig(
                response_mime_type = "application/json",
            ))
            # answer = response.text.strip("\n").strip()
            answer = response.text
            return answer, response.usage_metadata.total_token_count

        def gemini_rag(content):
            response = chat.send_message(
                content, 
                config = types.GenerateContentConfig(
                    tools=[
                        types.Tool(
                            file_search=types.FileSearch(
                                file_search_store_names=[store.name],
                            )
                        )
                    ]
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
            token_usage = 0
            content = news['內容']
            
            client = genai.Client(api_key=API_key)
            chat = client.chats.create(model=gemini_model)
            stores_list = client.file_search_stores.list()
            store = next((s for s in stores_list if s.display_name == "disaster_response_guide"), None)
            
            prompt1 = f"You are now a global disaster intelligence expert. Please organize the article from link '{news['來源網址']}' into four key points, focusing on the damages caused."
            # prompt1 = "You are now a global disaster intelligence expert. Please organize the article into four key points, focusing on the damages caused." ###
            prompt2 = "Based on these four key points, create a multiple-choice question with four options, designed so that people can use reasoning to arrive at the answer and understand what happened. Please also provide the correct answer."
            prompt3 = 'Then provide an explanation for the answer in under 70 words, and ensure that "the text does not contain the words \'option\' or \'A, B, C, D\'." '
            prompt4 = f'Next, "based on the knowledge of {news["rag_link"]}, please tell me how to respond if i am personally involved in the case of this article, within 70 words.'
            prompt5 = "Based on the content above, return the 'Question', 'Option_A', 'Option_B', 'Option_C', 'Option_D', 'Correct_Answer', 'Explanation', and 'Response_Method'."
                       
            order = prompt1
            response1 = gemini_search(order)
            token_usage += response1[1]
            response2 = gemini_normal(prompt2)
            token_usage += response2[1]
            response3 = gemini_normal(prompt3)
            token_usage += response3[1]
            response4 = gemini_rag(prompt4)
            token_usage += response4[1]
            response5 = gemini_final(prompt5)
            token_usage += response5[1]
            print("response5: ", response5[0]) ######################################
            print("Total token usage: ", token_usage)
            
            questions = {}
            questions['rawquestion'] = response5[0]
            questions['county'] = news['county'][0]
            questions['time'] = news['上版日期']
            questions['title'] = news['標題']
            questions['url'] = news['來源網址']
            series.append(questions)

        # print(series)

        return series        