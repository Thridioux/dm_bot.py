import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



# Initialize the driver
driver = webdriver.Chrome()
driver.maximize_window()

# Login to Instagram
driver.get('https://www.instagram.com')

my_username ='yanchar_test.1' # your instagram account username
my_password ='' # your instagram account password

users =['faruk_erdemcelik',]  # Users that u wanna send a message 

messages=['hey its me  ']  # A message 

search_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='username']")))
search_password.send_keys(my_username)

search_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//input[@name='password']")))
search_password.send_keys(my_password)
search_password.send_keys(Keys.RETURN)
time.sleep(5)

not_now1 = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"//button[text()='Not Now']"))).click()

driver.get("https://www.instagram.com/direct/new/")

for user in users:
	WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[1]/div/div[2]/input"))).send_keys(user)
	search_password = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[2]/div[2]/div[1]/div/div[2]/div[2]/div"))).click()

	
	WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[2]/div/div/div[1]/div/div[2]/div/div/div/div/div[2]/div/div[1]/div/div[3]/div/button/div"))).click()
	text_area = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,"/html/body/div[2]/div/div/div[1]/div/div/div/div[1]/div[1]/div/div[2]/div/section/div/div/div/div/div[2]/div[2]/div/div[2]/div/div/div[2]/textarea")))
	text_area.send_keys(messages)
	text_area.send_keys(Keys.RETURN)
	driver.get("https://www.instagram.com/direct/new/")

driver.quit()	

