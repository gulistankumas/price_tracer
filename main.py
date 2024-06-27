import requests
import lxml
from bs4 import BeautifulSoup
import pandas
from csv import DictWriter
import csv
import smtplib

MY_EMAİL="testmailbygk@gmail.com"
MY_PASSWORD="jwcxnngkpujkawxe"

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
#print(found_company)

#---------------------------------------------------------------
tag=data[data.WEBSITE == found_company]
price_tag= tag.iloc[0]['PRICE_TAG']
#print(price_tag)


#---------------bulunan price ve company name data.csvye yazılır.---------
def find_price(url,tag,company):
    field_names = ['WEBSITE', 'PRİCE']
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "lxml")

    price=soup.find(class_=tag).get_text()
    #print(price)
    price_without_currency = price.split(" ")[0].split(".")
    #print(price_without_currency)
    whole_price="".join(price_without_currency)
    
    
    dict = {'WEBSITE':company, 'PRİCE':whole_price}

    with open('data.csv', 'a') as f_object:
        Dictwriter_object= DictWriter(f_object,fieldnames=field_names)
        Dictwriter_object.writerow(dict)
        f_object.close()
    return whole_price
#------------------------------------------------------------------------
#founded=find_price(url,price_tag,found_company)


price_info=pandas.read_csv("data.csv")
data_dict=price_info.to_dict()
#print(data_dict)

#----------------------price güncelle----------
def update_price(company,new_price):
    with open('data.csv', mode='r') as file:
        reader = csv.DictReader(file)
        rows = list(reader)

    field_names = ['WEBSITE', 'PRICE']
    for row in rows:
        if row['WEBSITE'] == company:
            row['PRICE'] = new_price

    with open('data.csv', mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=field_names)
        writer.writeheader()
        writer.writerows(rows)
    return new_price
    


#------------------price degismi mi kontrol eder---------------
        
def is_price_chanced(company,url,tag):
    field_names = ['WEBSITE', 'PRİCE']
    response = requests.get(url, headers=header)
    soup = BeautifulSoup(response.content, "lxml")
    price_data=price_info[price_info.WEBSITE == company]

    if price_data.empty:
            return "empty dataframe"
    else:
        old_price=price_data.iloc[0]['PRICE']
        print(old_price)
    
    price=soup.find(class_=tag).get_text()
    price_without_currency = price.split(" ")[0].split(".")
    new_price="".join(price_without_currency)
    print(new_price)

    price_diff = int(new_price) - int(old_price)
    if price_diff == 0:
        return "The price has not changed."
    elif price_diff > 0:
        return update_price(found_company,new_price)
    else:
        return  update_price(found_company,new_price)
    
#-------------------------------------------------------------
    
price_check=is_price_chanced(found_company,url,price_tag)

#----------------------------------------------------------
import datetime as dt

now=dt.datetime.now()
hour= now.hour
minute=now.minute
if hour == 10 or 23 :
    #if minute==00:
    if price_check == "The price has not changed.":
        print("The price has not changed.")
    elif price_check != "empty dataframe":
        with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAİL, password=MY_PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAİL, 
                    to_addrs='email',
                    msg='The price of the product you are following has dropped ! ')



