from datetime import datetime 
a = datetime.now()
with open("record.txt", "a", encoding="utf-8") as file:
    file.write(f"{a}\n") 
