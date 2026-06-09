import requests
from bs4 import BeautifulSoup
from analyzer import filter_content, save_to_brain

def main():
    # Danh sách các web mày muốn cào
    urls = [
        "https://viblo.asia/latest",
        "https://securityaffairs.com/"
    ]
    
    all_data = []
    
    for url in urls:
        try:
            response = requests.get(url, headers={'User-Agent': 'Mozilla/5.0'})
            soup = BeautifulSoup(response.text, 'html.parser')
            # Lấy tất cả các thẻ h3 (thường là tiêu đề bài viết)
            data = [h3.get_text() for h3 in soup.find_all('h3')]
            all_data.extend(data)
        except Exception as e:
            print(f"Lỗi khi cào {url}: {e}")

    # Lọc và lưu vào bộ não
    cleaned_data = filter_content(all_data)
    save_to_brain(cleaned_data)
    print("Xong rồi nhé!")

if __name__ == "__main__":
    main()
    
