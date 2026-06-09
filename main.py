import requests
from bs4 import BeautifulSoup
import analyzer  # Import file mày vừa tạo

def scrape_data(url):
    try:
        response = requests.get(url, timeout=10)
        soup = BeautifulSoup(response.text, 'html.parser')
        return [p.text for p in soup.find_all('p')]
    except:
        return []

def main():
    target_url = "https://viblo.asia/tags/security"
    raw_data = scrape_data(target_url)
    
    # Gọi thằng analyzer để xử lý
    cleaned_data = analyzer.filter_content(raw_data)
    analyzer.save_to_brain(cleaned_data)
    
    # Ghi log như bình thường
    # ... (giữ nguyên phần ghi log của mày)

if __name__ == "__main__":
    main()
    
