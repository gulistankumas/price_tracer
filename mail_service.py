import smtplib

MY_EMAİL="testmailbygk@gmail.com"
MY_PASSWORD="jwcxnngkpujkawxe"

with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAİL, password=MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAİL, 
            to_addrs='',
            msg='')
