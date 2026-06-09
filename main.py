import asyncio
import aiohttp
from bs4 import BeautifulSoup
from analyzer import filter_content, save_to_brain

# Mỏ vàng dữ liệu về hack/code
urls = [
    "https://thehackernews.com/",
    "https://www.exploit-db.com/",
    "https://portswigger.net/daily-swig",
    "https://www.darkreading.com/",
    "https://nvd.nist.gov/vuln/latest",
    "https://dev.to/",
    "https://github.com/trending"
]

async def fetch(session, url):
    try:
        async with session.get(url, timeout=10) as response:
            html = await response.text()
            soup = BeautifulSoup(html, 'html.parser')
            # Lấy tiêu đề từ nhiều loại thẻ
            tags = soup.find_all(['h1', 'h2', 'h3'])
            return [tag.get_text().strip() for tag in tags]
    except:
        return []

async def main():
    async with aiohttp.ClientSession(headers={'User-Agent': 'Mozilla/5.0'}) as session:
        tasks = [fetch(session, url) for url in urls]
        results = await asyncio.gather(*tasks)
        
    all_data = [item for sublist in results for item in sublist]
    cleaned_data = filter_content(all_data)
    save_to_brain(cleaned_data)
    print(f"Vét xong {len(cleaned_data)} item dữ liệu chất!")

if __name__ == "__main__":
    asyncio.run(main())
# Async Engine Enabled
