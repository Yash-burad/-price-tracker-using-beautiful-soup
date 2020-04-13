# -*- coding: utf-8 -*-
"""
Created on Sun Apr 12 12:41:12 2020

@author: kus
"""

from bs4 import BeautifulSoup
import requests
import smtplib
import time
def send_mail():
    server=smtplib.SMTP('smtp.gmail.com' , 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('yashburad9@gmail.com','ukzqlatjwygrgpal')
    
    subject="THE PRICE FOR YOUR PRODUCT FELL DOWN "
    body="CHECK THE LINK "+URL
    
    msg=f"Subject: {subject}\n\n{body}"
    server.sendmail('yashburad9@gmail.com','yashburad9@gmail.com',msg)
    
    print("MAIL HAS BEEN SENT !!")
    server.quit()

def check_price():    
    URL='https://www.flipkart.com/philips-qt3310-15-runtime-30-min-trimmer-men/p/itmc7efd5003ea13?pid=SHVEHHFBMHJZUZWS&lid=LSTSHVEHHFBMHJZUZWSKCNLNB&marketplace=FLIPKART&spotlightTagId=BestsellerId_zlw%2F79s%2Fby3&srno=s_1_2&otracker=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_8_na_na_na&fm=SEARCH&iid=f0016f29-9995-4a4e-a7de-592f437d3729.SHVEHHFBMHJZUZWS.SEARCH&ppt=sp&ppn=sp&ssid=mq6o4rbwzk0000001586675366400&qH=dc098acd2ef82486'

    headers={"User-Agent":'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/80.0.3987.163 Safari/537.36'}
    page=requests.get(URL, headers=headers)

    soup=BeautifulSoup(page.content,'html.parser')

    price=soup.find(class_="_1vC4OE _3qQ9m1").get_text()[1:]
    intprice=float(price[0:5].replace(',','.'))
    print(intprice)


    if(intprice<1.000):
        send_mail()
    
while(True):
    check_price()
    time.sleep(86400)
        

    