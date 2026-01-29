from google import genai
from google.genai import types
from pydantic import BaseModel
from Step import STEPS
from parameter import get_para
from dotenv import load_dotenv
import os

load_dotenv()
API_key = os.getenv("GEMINI_API_KEY")
gemini_model = get_para('gemini_model')
client = genai.Client(api_key=API_key)
chat = client.chats.create(model="gemini-2.5-flash-lite")
stores_list = client.file_search_stores.list()
store = next((s for s in stores_list if s.display_name == "disaster_response_guide"), None)

def gemini(content):
    response = chat.send_message(
        content,
        config=types.GenerateContentConfig(
            tools=[
                types.Tool(
                    file_search=types.FileSearch(
                        file_search_store_names=[store.name]
                    )
                )
            ]
        )
    )
    return response

content = ""
while content != "end":
    content = input("Input: ")
    response = gemini(content)
    print("\nGemini:",response.text,"\n")