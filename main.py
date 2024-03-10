import requests
import lxml
from bs4 import BeautifulSoup

url = "https://www.amazon.com.tr/Notebook-Laptop-F1502ZA-EJ1527-i5-1235U-%C4%B0%C5%9Flemci/dp/B0CJYC9ZC1?ref_=Oct_DLandingS_D_7b4c67f8_0"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7",
    "Accept-Encoding":"gzip, deflate, br, zstd",
    "Cookie": "PHPSESSID=a8d901af30182d24b6017f9eb17a908b; _ga=GA1.2.550020601.1710094136; _gid=GA1.2.553676157.1710094136; _ga_VL41109FEB=GS1.2.1710094136.1.0.1710094136.0.0.0",
    "Accept" :"text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7"
}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
print(soup.prettify())

price = soup.find(class_="a-offscreen").get_text()
price_without_currency = price.split("TL")[1]
price_as_float = float(price_without_currency)
print(price_as_float)