import requests

api_key = "d2904786182146a5a7657b22bf013a94"
query = "technology"

url = f"https://newsapi.org/v2/everything?q={query}&from=2025-11-27&sortBy=publishedAt&apiKey={api_key}"

print(url)

r = requests.get(url)
data = r.json()

articles = data["articles"]
for article in articles:
    print(article["title"],article["url"])
print("Total articles found:", len(articles))