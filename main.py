import os
import json
import datetime
import random

# Tạo cấu trúc thư mục nếu chưa có
os.makedirs('data', exist_ok=True)
os.makedirs('logs', exist_ok=True)

def get_timestamp():
    now = datetime.datetime.now()
    return now.strftime("[%d/%m/%Y|%H:%M:%S]")

def log_event(message):
    timestamp = get_timestamp()
    log_entry = f"{timestamp} {message}\n"
    print(log_entry) # In ra console cho dễ theo dõi
    with open('logs/evolution.log', 'a', encoding='utf-8') as f:
        f.write(log_entry)

def learn_and_evolve():
    # Giả lập việc AI tự học kiến thức mới
    knowledge_db = ["Exploit logic", "Web structure analysis", "Bypass pattern", "Data scraping"]
    new_knowledge = random.choice(knowledge_db)
    
    # Ghi vào bộ nhớ
    brain_file = 'data/brain.json'
    data = {"last_learned": new_knowledge, "timestamp": str(datetime.datetime.now())}
    with open(brain_file, 'w', encoding='utf-8') as f:
        json.dump(data, f, indent=4)
        
    log_event(f"Already studied {new_knowledge}...")
    log_event(f"I understand the code structure for {new_knowledge}...")

if __name__ == "__main__":
    learn_and_evolve()
      
