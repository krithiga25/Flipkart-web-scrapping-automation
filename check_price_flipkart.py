import requests
from bs4 import BeautifulSoup
import smtplib
import os
EMAIL_ADDRESS = os.environ.get('EMAIL_USER')
EMAIL_PASSWORD =os.environ.get('EMAIL_PASS')
URL='https://www.flipkart.com/into-the-wild/p/itmfbz266k9fmfnc?pid=9780330351690&lid=LSTBOK9780330351690XUAHK2&marketplace=FLIPKART&srno=s_1_1&otracker=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&otracker1=AS_QueryStore_OrganicAutoSuggest_1_15_na_na_na&fm=SEARCH&iid=afbee0a0-6587-4762-87c2-689ece02f800.9780330351690.SEARCH&ppt=sp&ppn=sp&ssid=sfoqkmu3j48xa03k1611761833116&qH=9cf706bc76b8a0bb'
headers = {

    'User_Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:84.0) Gecko/20100101 Firefox/84.0'
}
def check_price():
  page= requests.get(URL, headers=headers)
  soup = BeautifulSoup(page.content, 'html.parser')
  name = soup.find('span', class_="B_NuCI")#finding using span and class

  converted_name= name.text
  #print(converted_name)
  price =soup.find('div', class_ ="_30jeq3 _16Jk6d")
  price_text = price.text
  global converted_price
  converted_price = price_text[1:4]
  print(converted_price)
  global f
  f = int(converted_price)
  #print(f)
check_price()



def send_mail_price():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
    subject = 'Price has dropped for Into the wild!' \
              ' price is '+ converted_price +' rupees.'
    body = URL
    msg = f"Subject:{subject}\n\n{body}"
    server.sendmail(
        EMAIL_ADDRESS,
        EMAIL_ADDRESS,
        msg
    )
    server.quit()
    #print("Mail sent successfully!")
if(f<300):

    send_mail_price()
    #print('yes')
