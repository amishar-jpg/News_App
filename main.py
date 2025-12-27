import requests
import sys
from config import api_key

sys.stdout.reconfigure(encoding='utf-8')

query = input("Enter topic you want to search news for: ")

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-11-27&sortBy=publishedAt&apiKey={api_key}"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]
for index,article in enumerate(articles):
    print(index+1, article["title"],article["url"])
    print("\n***************************************************************************************************\n")
    # print("Total articles found:", len(articles))
