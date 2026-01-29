from google import genai
from google.genai import types
from pydantic import BaseModel
from dotenv import load_dotenv
import os
import time
# parent_dir1 = os.path.dirname(os.path.abspath(__file__))
# parent_dir2 = os.path.dirname(parent_dir1)
# dotenv_path = os.path.join(parent_dir2, '.env')

load_dotenv('pipeline/.env')
client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"),)
stores_list = client.file_search_stores.list()
store = next((s for s in stores_list if s.display_name == "disaster_response_guide"), None)
store_name = "disaster_response_guide"

# 1. Define your file path
file_path = r"C:\新加坡研討會\RAG_resources\Winter-Weather.md"
file_display_name = "winter-weather"

# 2. Upload and Link in one go
print(f"Uploading and linking {file_path} to store {store.name}...")

operation = client.file_search_stores.upload_to_file_search_store(
    file=file_path,
    file_search_store_name=store.name,
    config=types.UploadToFileSearchStoreConfig(
        display_name=file_display_name,
        mime_type="text/markdown"
    )
)

# 3. Wait for the operation to complete (Indexing takes time)
print("Waiting for indexing to complete...")
while not operation.done:
    # time.sleep(2)
    operation = client.operations.get(operation)

print("Successfully added and indexed in RAG store.")