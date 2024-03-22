import datetime as dt
from main import is_price_chanced,found_company,url,price_tag

now=dt.datetime.now()
hour= now.hour
minute=now.minute
if hour == 10 or 22 :
    if minute==00:
       is_price_chanced(found_company,url,price_tag)
