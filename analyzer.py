import json
import os

def filter_content(raw_data):
    keywords = ['exploit', 'vulnerability', 'bypass', 'cve', 'security']
    relevant_info = []

    for item in raw_data:
        if any(key in item.lower() for key in keywords):
            relevant_info.append(item.strip())

    return relevant_info

def save_to_brain(new_data):
    brain_path = 'data/brain.json'
    
    # Đảm bảo thư mục tồn tại
    os.makedirs('data', exist_ok=True)

    if os.path.exists(brain_path):
        with open(brain_path, 'r', encoding='utf-8') as f:
            try:
                brain = json.load(f)
            except:
                brain = {"learned": []}
    else:
        brain = {"learned": []}

    brain['learned'].extend(new_data)
    
    with open(brain_path, 'w', encoding='utf-8') as f:
        json.dump(brain, f, ensure_ascii=False, indent=4)
        
