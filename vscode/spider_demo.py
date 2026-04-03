import requests
url = "https://movie.douban.com/j/chart/top_list?type=11&interval_id=100%3A90&action=&start=0&limit=10"
headers = {
     "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36",
     "Referer": "https://movie.douban.com/chart"
}
response = requests.get(url, headers=headers)
data = response.json()
print("=== 豆瓣电影排行榜 ===")
for i, item in enumerate(data, 1):
     print(f"{i}. {item['title']}")
input("按回车键退出")
