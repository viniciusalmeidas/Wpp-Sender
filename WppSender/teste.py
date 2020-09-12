from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from time import sleep
import os 


vector = [5521987471804]
path = os.getcwd().replace("\\","/")+'/chromedriver.exe'
driver = webdriver.Chrome(executable_path= path)
driver.get("http://web.whatsapp.com")
sleep(10)

try:
    driver.get('https://web.whatsapp.com/send?phone={}'.format(vector))
    sleep(6)            
    image_path = "C:/Users/VINÍCIUS/Pictures/Banski.jpg"
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
#Add file to send by file path
    driver.find_element_by_css_selector("input[type='file']").send_keys(image_path)
#Click to send
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()
except Exception:
    sleep(10)
    print("Error on: :( ")

def send_image(driver, image_path):
    driver.find_element_by_css_selector("span[data-icon='clip']").click()
    driver.find_element_by_css_selector("input[type='file']").send_keys(image_path)
    driver.find_element_by_xpath("//*[@id='app']/div/div/div[2]/div[2]/span/div/span/div/div/div[2]/span/div/div").click()