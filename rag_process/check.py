from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv
import os

# parent_dir1 = os.path.dirname(os.path.abspath(__file__))
# parent_dir2 = os.path.dirname(parent_dir1)
# dotenv_path = os.path.join(parent_dir2, '.env')

load_dotenv('../dkk_system/pipeline/.env')
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"),)

# examine_file_name = "disaster_response_guide"
stores_list = client.file_search_stores.list()
store = next((s for s in stores_list if s.display_name == "disaster_response_guide"), None)
print(f"Checking documents in store: {store.display_name} ({store.name})")  
# Use the 'documents' sub-service.
# The SDK requires the store ID to be passed as 'parent'.
store_docs = client.file_search_stores.documents.list(
    parent=store.name
)

for doc in store_docs:
    print(f"- Document Display Name: {doc.display_name}")
    print(f"  Document Resource Name: {doc.name}")
    # Note: 'state' is part of the Document object in this SDK
    # print(f"  State: {doc.state}") 
    print("---")