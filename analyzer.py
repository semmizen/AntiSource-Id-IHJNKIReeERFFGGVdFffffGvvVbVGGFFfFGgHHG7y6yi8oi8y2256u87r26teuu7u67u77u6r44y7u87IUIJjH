import json
import os

def filter_content(raw_data):
    # Những từ khóa mày muốn "vét" sâu vào
    keywords = ['exploit', 'vulnerability', 'bypass', 'cve', 'security', 'hack', 'patch']
    relevant_info = []
    
    for item in raw_data:
        # Nếu dòng nào chứa từ khóa thì giữ lại
        if any(key in item.lower() for key in keywords):
            relevant_info.append(item.strip())
            
    return relevant_info

def save_to_brain(new_data):
    brain_path = 'data/brain.json'
    
    # Load bộ nhớ cũ, nếu chưa có thì tạo mới
    if os.path.exists(brain_path):
        with open(brain_path, 'r', encoding='utf-8') as f:
            try:
                brain = json.load(f)
            except:
                brain = {"learned": []}
    else:
        brain = {"learned": []}
    
    # Cập nhật kiến thức mới vào bộ não
    brain['learned'].extend(new_data)
    
    with open(brain_path, 'w', encoding='utf-8') as f:
        json.dump(brain, f, indent=4, ensure_ascii=False)
          
