import time
import pandas as pd
import numpy as np
from selenium import webdriver
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup as bs
from concurrent.futures import ThreadPoolExecutor
import random 

df = pd.read_csv('/Users/sehajsukhleensingh/Documents/projects/Project1/scraping/links-gurgaon-homes.csv')
links = df['link']

urls = []
for i in links:
    urls.append(i)

url = urls[2190:2120]

  
def driverRotation():
    options = webdriver.ChromeOptions()

    options.add_argument("--disable-blink-features=AutomationControlled")  # Prevents detection as bot
    #options.add_argument("--start-maximized")  # Opens browser in full screen
    #options.add_argument("--incognito")  # Opens browser in Incognito mode
    options.add_argument("--disable-popup-blocking")  # Prevents blocking of popups
    options.add_argument("--disable-infobars")  # Removes 'Chrome is being controlled by automated test software'
    options.add_argument("--disable-gpu")  # Reduces detection based on GPU usage
    options.add_argument("--no-sandbox")  # Byaddress = np.nan OS security model
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36")
    options.add_experimental_option("prefs", {"profile.managed_default_content_settings.images": 2})
    
    # proxy = proxyRotation(proxies)
    # options.add_argument(f'--proxy-server=https://{proxy}')
    
    s = Service(service = '/Users/sehajsukhleensingh/.wdm/drivers/chromedriver/mac64/133.0.6943.126/chromedriver-mac-arm64/chromedriver')
    
    driver = webdriver.Chrome(service = s , options = options)
    
    return driver 

def scraper(link):
    
    driver = driverRotation()
    
    driver.get(link)
    time.sleep(2)

    oldH = driver.execute_script('return document.body.scrollHeight')

    while True:

        driver.execute_script('window.scrollTo(0,document.body.scrollHeight)')
        time.sleep(1)

        newH = driver.execute_script('return document.body.scrollHeight')

        if newH == oldH:
            html = driver.page_source
            break
        oldH = newH
        
    soup = bs(html,'lxml')
    driver.quit()

    try:
        address = soup.find('span',class_= 'component__pdPropAddress').get_text()
    except:
        address = np.nan
    try:
        society = soup.find('span',class_='component__pdPropAddress').get_text()
    except:
        society = np.nan
    try:
        area = soup.find('span',id='superArea_span').get_text()
    except:
        area = np.nan
    try:
        bedrooms = soup.find('span',id='bedRoomNum').get_text()
    except:
        bedrooms = np.nan
    try:
        bathrooms = soup.find('span',id='bathroomNum').get_text()
    except:
        bathrooms = np.nan
    try:
        additionalRooms = soup.find('span',id='additionalRooms').get_text()
    except:
        additionalRooms = np.nan
    try:
        balcony = soup.find('span',id='balconyNum').get_text()
    except:
        balcony = np.nan
    try:
        floorNum = soup.find('span',id='floorNumLabel').get_text()
    except:
        floorNum = np.nan
    try:
        facing = soup.find('span',id='facingLabel').get_text()
    except:
        facing = np.nan
    try:
        agePossession = soup.find('span',id='agePossessionLbl').get_text()
    except:
        agePossession = np.nan
    try:
        nbl = soup.find_all('span',class_='NearByLocation__infoText')
        nearByLocation = str([i.get_text() for i in nbl ])
    except:
        nearByLocation = np.nan
    try:
        description = soup.find('div',class_='component__pdDescription').get_text()
    except:
        description = np.nan
    try:
        ul = soup.find_all('ul',id='features')
        furnishDetials = str([i.get_text() for i in ul[0]])
    except:
        furnishDetials = np.nan
    try:
        features = str([i.get_text() for i in ul[1]])
    except:
        features = np.nan
    try:
        propertyId = soup.find('span',id='Prop_Id').get_text()
    except:
        propertyId = np.nan
        
    finally:
        
        print(f'Scraped link : {link}')
        
        return { "society": society,"area": area,'propertyType':'House',"bedRooms": bedrooms,"bathRooms": bathrooms,
                "additionalRooms": additionalRooms,"address":address,"floorNum": floorNum,'balcony':balcony,
            "facing": facing,"agePossesion": agePossession,"nearbyLocation": nearByLocation,"description": description,
            "furnishDetails": furnishDetials,"features": features,"propertyId": propertyId,"links": link }
            

pool = ThreadPoolExecutor(max_workers = 5)

with pool as executer:
    results = list(executer.map(scraper,url))

print(len(results))    

temp = pd.DataFrame()

for value in results:
    df = pd.DataFrame([value])
    temp = pd.concat([temp,df],ignore_index = True)

df = pd.read_csv('/Users/sehajsukhleensingh/Documents/projects/Project1/scraping/data-homes.csv')

df = pd.concat([df,temp],ignore_index =True)

df.to_csv('/Users/sehajsukhleensingh/Documents/projects/Project1/scraping/data-homes.csv',index = False)




