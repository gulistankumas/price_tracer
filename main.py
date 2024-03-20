import requests
import lxml
from bs4 import BeautifulSoup
import pandas

#---------- Url'den company name bulma---------------
data=pandas.read_csv("price_tags.csv")
data_dict=data.to_dict()
website_list=data["WEBSITE"].to_list()
print(website_list)

def find_company_in_url(url):
    for company_name in website_list:
        L_company_name=company_name.lower()
        if L_company_name in url:
            return company_name
    return "No company name found in the link"

#----------------------------------------------------