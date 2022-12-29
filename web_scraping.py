import requests
import pandas as p
import csv
from bs4 import BeautifulSoup
#asking permission to website to access their website content or data
#sending my request as response to website ,so with that of response we can do next step
response=requests.get('https://www.flipkart.com/mobiles/~cs-rqdgyi17sh/pr?sid=tyy%2C4io&collection-tab-name=Redmi++A1+Plus&param=32423&otracker=clp_bannerads_1_6.bannerAdCard.BANNERADS_Redmi-A1-Plus-PL-saleiso_mobile-phones-store_JOEAMV91VLOD')
soup=BeautifulSoup(response.content,'html.parser')
#start code
names=soup.find_all('div',class_='_4rR01T')
name=[]
for i in names:
    d=i.get_text()
    name.append(d)   
prices=soup.find_all('div',class_='_30jeq3 _1_WHN1')
price=[]
for i in prices:
    d=i.get_text()
    price.append(d)    
ratings=soup.find_all('div',class_='_3LWZlK')
rate=[]
for i in ratings:
    d=i.get_text()
    rate.append(float(d))       
images=soup.find_all('img',class_='_396cs4 _3exPp9')
image=[]
for i in images:
    d=i['src']
    image.append(d)
links=soup.find_all('a',class_='_1fQZEK')
link=[]
for i in links:
    d="https://www.flipkart.com"+i['href']
    link.append(d)  
df=p.DataFrame()
df['Names']=name 
df['prices']=price
df['ratings']=rate
df['images']=image
df['links']=link
df.to_csv('redmi.csv')
