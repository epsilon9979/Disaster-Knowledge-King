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

# 1. delete all files in all stores, then delete the stores themselves
stores = client.file_search_stores.list()
for store in stores:
    print(f"\nCleaning Store: {store.display_name} ({store.name})")
    
    try:
        # The correct path is client.file_search_stores.documents.list
        # You must pass the store name as the 'parent' parameter
        store_files = client.file_search_stores.documents.list(parent=store.name)
        
        has_files = False
        for f_link in store_files:
            has_files = True
            print(f"  -> Deleting document: {f_link.name}")
            
            # The correct path is client.file_search_stores.documents.delete
            # You must include config={'force': True} for a clean removal
            client.file_search_stores.documents.delete(
                name=f_link.name, #########################################################################
                config={'force': True}
            )
        
        if has_files:
            print("  Waiting for sync...")
            time.sleep(2)
        
        # Finally delete the store itself
        client.file_search_stores.delete(name=store.name, config={'force': True})
        print(f"  [OK] Successfully removed Store")
        
    except Exception as e:
        print(f"  [Error] Failed: {e}")