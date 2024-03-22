import requests
import lxml
from bs4 import BeautifulSoup
from csv import DictWriter
import datetime as dt

field_names = ['WEBSITE', 'PRİCE']

url = "https://www.trendyol.com/nespresso/c30-essenza-mini-kahve-makinesi-beyaz-p-3464686?boutiqueId=61&merchantId=603035&sav=true"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"

}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")
pricetag=soup.find('span',class_='prc-dsc')
print(pricetag.get_text())