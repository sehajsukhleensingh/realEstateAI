from concurrent.futures import ThreadPoolExecutor 
import numpy as np 
import pandas as pd
import time
import selenium
from selenium import webdriver 
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from bs4 import BeautifulSoup as bs

dt = pd.read_csv('99acres-gurgaon.csv')
links = dt['links']

urls = []
for url in links:
    urls.append(url)


urls = urls[2320:]

def scraper(url):
    
    data = {
    "society": np.nan, "price": np.nan, "area": np.nan, "areaWithType": np.nan,
    "bedRooms": np.nan, "bathRooms": np.nan, "additionalRooms": np.nan, "address": np.nan,
    "floorNum": np.nan, "facing": np.nan, "agePossesion": np.nan, "nearbyLocation": np.nan,
    "description": np.nan, "furnishDetails": np.nan, "features": np.nan, "propertyId": np.nan,'links':np.nan
    }
    
    options = Options()

    options.add_argument("--disable-blink-features=AutomationControlled")  # Reduce bot detection
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36")
    
    
    # Initialize WebDriver
    service = Service('/Users/sehajsukhleensingh/.wdm/drivers/chromedriver/mac64/133.0.6943.126/chromedriver-mac-arm64/chromedriver')
    driver = webdriver.Chrome(service=service, options=options)

    
    try:
        driver.get(url)
        time.sleep(5)
        
        response = driver.page_source
    
        soup = bs(response ,  'lxml')
        
        try: data['links'] = url
        except:pass
        try: data["price"] = soup.find('span', id='pdPrice2').text.strip()
        except: pass
        try: data["society"] = soup.find('span', class_='component__pdPropAddress').text.split(',')[0]
        except: pass
        try: data["area"] = soup.find('span', id='superbuiltupArea_span').text.strip()
        except: pass
        try: data["areaWithType"] = soup.find('span', id='builtupArea_span').text.strip()
        except: 
            try: data["areaWithType"] = soup.find('span', id='carpetArea_span').text.strip()
            except: pass
        try: data["facing"] = soup.find('span', id='facingLabel').text.strip()
        except: pass
        try: data["floorNum"] = soup.find('span', id='floorNumLabel').text.strip()
        except: pass
        try: data["agePossesion"] = soup.find('span', id='agePossessionLbl').text.strip()
        except: pass
        try: data["address"] = driver.find_element(by = By.XPATH , value = '//*[@id="FactTableComponent"]/tbody/tr[2]/td[2]/div[2]').text
        except: pass
        try: data["description"] = soup.find('span', id='description').text.strip()
        except: pass
        try:
            ul = soup.find_all('ul', id='features')
            data["furnishDetails"] = [li.text.strip() for li in ul[0].find_all('li')] if ul else np.nan
            data["furnishDetails"] = str(data["furnishDetails"])
        except: pass
        try: 
            data["features"] = [li.text.strip() for li in ul[1].find_all('li')] if ul else np.nan
            data["features"] = str(data["features"])
        except: pass
        try: data["bedRooms"] = soup.find('span', id='bedRoomNum').text.strip()
        except: pass
        try: data["bathRooms"] = soup.find('span', id='bathroomNum').text.strip()
        except: pass
        try: data["additionalRooms"] = soup.find('span', id='additionalRooms').text.strip()
        except: pass
        try:
            spanlis = soup.find_all('span', class_='NearByLocation__infoText')
            data["nearbyLocation"] = [item.text.strip() for item in spanlis] if spanlis else np.nan
            data["nearbyLocation"] = str(data["nearbyLocation"])
        except: pass
        try: data["propertyId"] = soup.find('span', id='Prop_Id').text.strip()
        except: pass

        print(f"Scraped: {url}")

    except:
        print('Couldnt connect to link ... ')
        driver.quit()

    finally:
        driver.quit()
        return data

pool = ThreadPoolExecutor(max_workers = 5)

with pool as executor:
    results = list(executor.map(scraper , urls))

print(len(results))

dt1 = pd.DataFrame()
for dict in results:
    temp = pd.DataFrame([dict])
    dt1 = pd.concat([dt1,temp],ignore_index = True)    

dt = pd.read_csv('dt.csv')

dt = pd.concat([dt,dt1],ignore_index = True)

dt.to_csv('dt.csv',index = False)

