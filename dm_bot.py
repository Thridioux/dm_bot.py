import selenium
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys 
from time import sleep
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



driver_service = Service(executable_path="C:\Program Files (x86)\chromedriver.exe")  # Type the path of your web driver that u installed before.You can install from here https://chromedriver.chromium.org/downloads
driver = webdriver.Chrome(service=driver_service)

my_username ='**********' # your instagram account username
my_password ='**********' # your instagram account password

users =['yanchar_test.1','********']  # Users that u wanna send a message 

messages=['selam erdem ben ']  # A message 


driver.get('https://www.instagram.com')

search_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
search_password.send_keys(my_username)

search_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
search_password.send_keys(my_password)
search_password.send_keys(Keys.RETURN)

not_now1 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Not Now']"))).click()
not_now2 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]"))).click()

driver.get("https://www.instagram.com/direct/new/")

for user in users:
	WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input"))).send_keys(user)
	search_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"(//*[name()='circle'])[3]"))).click()

	
	WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div"))).click()
	text_area = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[1]/div/div/div/div[1]/div/div/div/div[1]/div[1]/section/div/div[2]/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
	text_area.send_keys(messages)
	text_area.send_keys(Keys.RETURN)
	driver.get("https://www.instagram.com/direct/new/")
























	







        
            


           
           








    
    











