import requests
import lxml
from bs4 import BeautifulSoup
import pandas
from csv import DictWriter

#---------- Url'den company name bulma---------------------------
data=pandas.read_csv("price_tags.csv")
data_dict=data.to_dict()
website_list=data["WEBSITE"].to_list()

url = "https://www.teknosa.com/yenilenmis-samsung-galaxy-s23-128-gb-yesil-cep-telefonu-1-yil-garantili-p-790182141"
header = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.0.0 Safari/537.36",
        "Accept-Language": "tr-TR,tr;q=0.9,en-US;q=0.8,en;q=0.7"

    }

def find_company_in_url(url):
    for company_name in website_list:
        L_company_name=company_name.lower()
        if L_company_name in url:
            return company_name
    return "No company name found in the link"

found_company = find_company_in_url(url)

#---------------------------------------------------------------
tag=data[data.WEBSITE == found_company]
price_tag= tag.PRICE_TAG[0]


#---------------bulunan price ve company name data.csvye yazılır.---------
def find_price(url,tag):
    field_names = ['WEBSITE', 'PRİCE']
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "lxml")

    price=soup.find(class_=tag).get_text()
    price_without_currency = price.split(" ")[0].split(".")
    whole_price="".join(price_without_currency)
    
    
    dict = {'WEBSITE':"Teknosa", 'PRİCE':whole_price}

    with open('data.csv', 'a') as f_object:
        Dictwriter_object= DictWriter(f_object,fieldnames=field_names)
        Dictwriter_object.writerow(dict)
        f_object.close()
#------------------------------------------------------------------------

founded=find_price(url,price_tag)

price_info=pandas.read_csv("data.csv")
data_dict=price_info.to_dict()
def is_price_chanced():
    price_data=price_info[price_info.WEBSITE == found_company]
    old_price=price_info.PRICE[3]
    return old_price

p=is_price_chanced()
print(p)