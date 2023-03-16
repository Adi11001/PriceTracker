'''
In this program we will be polling the price of a game on gameloot to see if the price goes below a certain threshold.
If the price is below a threshold the user will get notified using email.
Following are the steps performed
1. Get the html for the website to be scraped
2. Get the price of the product using the tag of its container
3. Check if the price is less than the threshold. If it is then send email else wait for 15 minutes and look again
'''
import requests
import smtplib
import time

from bs4 import BeautifulSoup
from csv import writer
#Track Price of Assassins creed Ezio collection every minute and send mail if price is less than 900rs 
url = 'https://gameloot.in/shop/assassins-creed-the-ezio-collection-ps4-pre-owned/'
price_threshold=700
#Class of the price tag to be tracked
price_class='woocommerce-Price-amount amount'

#Infinite Loop to keep Looking
while True:
    #request the from url
    page = requests.get(url)

    soup = BeautifulSoup(page.content,'html.parser')

    #Get the price using the class of the tag
    price = float(soup.find('span', class_=price_class).text[4:])
    if price < price_threshold:
        print("Yippie")
        #Code to send Email
        smt=smtplib.SMTP('smtp.gmail.com', 587)
        smt.ehlo()
        smt.starttls()
        smt.login('gameending25@gmail.com', 'tbhwobrawhvsufhn')
        smt.sendmail('gameending25@gmail.com',
                    'waniaditya2525@gmail.com',
                    f"Subject: Headphone Price Notifier\n\nHi, Price has dropped to {price}.Buy it!")
        smt.quit()
    else:
        print("Bad Luck")
    print(price)
    #Wait for a 15 minutes and retry 
    time.sleep(60*15) #Time in seconds