from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service

import time
import urllib.request

chrome_options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
URL = 'https://www.google.co.kr/imghp'
driver.get(url=URL)
driver.implicitly_wait(time_to_wait=10)
keyElement = driver.find_element(By.NAME, "q")
keyElement.send_keys('빨간구두')
keyElement.send_keys(Keys.RETURN)


SCROLL_PAUSE_TIME = 1
# Get scroll height
last_height = driver.execute_script("return document.body.scrollHeight")
while True:
    # Scroll down to bottom
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    # Wait to load page
    time.sleep(SCROLL_PAUSE_TIME)
    # Calculate new scroll height and compare with last scroll height
    new_height = driver.execute_script("return document.body.scrollHeight")
    if new_height == last_height:
        try:
            driver.find_element(By.CSS_SELECTOR, '.mye4qd').click()
        except:
            break
    last_height = new_height


images =  driver.find_elements(By.CSS_SELECTOR, '#islrg > div.islrc > div > a.wXeWr.islib.nfEiy > div.bRMDJf.islir > img')

imageURL = []
for image in images:
    if image.get_attribute('src') is not None:
        imageURL.append(image.get_attribute('src'))

for seq, urlImg in enumerate(imageURL):
    urllib.request.urlretrieve(urlImg, 'C:/open/' + str(seq) + '.jpg')