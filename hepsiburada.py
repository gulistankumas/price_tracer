import requests
import lxml
from bs4 import BeautifulSoup
from csv import DictWriter
import datetime as dt

field_names = ['WEBSITE', 'PRİCE']

url = "https://www.hepsiburada.com/samsung-galaxy-tab-s7-fe-4gb-64gb-12-4-wifi-tablet-mystic-black-p-HBCV00000SGHS6?magaza=Hepsiburada"
header = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
    "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"

}

response = requests.get(url, headers=header)

soup = BeautifulSoup(response.content, "lxml")

price=soup.find('span',attrs={'data-bind': "markupText:'currentPriceBeforePoint'"}).get_text()


price_without_currency = price.split(" ")[0].split(".")
whole_price="".join(price_without_currency)
print(whole_price)


dict = {'WEBSITE':"Hepsiburada", 'PRİCE':whole_price}

with open('data.csv', 'a') as f_object:
    Dictwriter_object= DictWriter(f_object,fieldnames=field_names)
    Dictwriter_object.writerow(dict)
    f_object.close()
