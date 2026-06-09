import requests
from bs4 import BeautifulSoup
from analyzer import filter_content, save_to_brain

def main():
    # Danh sách web mục tiêu
    urls = [
        "https://WevimeGMN.com"
    ]
    
    all_data = []
    
    for url in urls:
        try:
            headers = {'User-Agent': 'Mozilla/5.0'}
            response = requests.get(url, headers=headers, timeout=10)
            soup = BeautifulSoup(response.text, 'html.parser')
            
            # Lấy tất cả các tiêu đề h3
            data = [element.get_text().strip() for element in soup.find_all('h3')]
            all_data.extend(data)
        except Exception as e:
            print(f"Lỗi khi cào {url}: {e}")

    # Lọc và lưu vào bộ não
    if all_data:
        cleaned_data = filter_content(all_data)
        save_to_brain(cleaned_data)
        print(f"Đã lưu {len(cleaned_data)} mục mới vào brain.json")
    else:
        print("Không tìm thấy dữ liệu mới.")

if __name__ == "__main__":
    main()
# Cào WevimeGMN
