import logging
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as Ec
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service

logging.getLogger('selenium').setLevel(logging.WARNING)

chrome_options = Options()
#chrome_options.add_argument("--headless")
chrome_options.add_argument("--log-level=3")
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

chrome_services =Service(ChromeDriverManager().install())

driver = webdriver.Chrome(service=chrome_services,options=chrome_options)

driver.get("http://127.0.0.1:5500/TextToSpeech/bry.html")

def speak(text):
    try:
        element_to_click = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="text"]')))
        element_to_click.click()

        element_to_click.send_keys(text)
        print(text)

        sleep_duration=min(0.2+len(text)//5,5)

        button_to_click = WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,'//*[@id="button"]')))
        button_to_click.click()

        time.sleep(sleep_duration)

        element_to_click.clear()
        
    except Exception as E:
       print("Error : ", E )

speak("hello")
speak("hey i am Agies")
speak("hey there i am agies from ai i will work for my day")