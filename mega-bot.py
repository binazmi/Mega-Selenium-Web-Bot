#import sys
#sys.path.insert(0, r"C:\Python310\Lib\site-packages")
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import time  
from selenium.webdriver.common.keys import Keys  
print("sample test case started")  
driver = webdriver.Chrome(ChromeDriverManager().install())
#driver=webdriver.firefox()  
#driver=webdriver.ie()  
#maximize the window size  
driver.maximize_window()  
#navigate to the url
print("\n====== Navigating to WEBSITE ======\n")
driver.get("https://mega.nz/login")

# Cert Invalid Bypass
#myElem = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, "details-button")))
#driver.find_element_by_id("details-button").click()
#myElem = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, "proceed-link")))
#driver.find_element_by_id("proceed-link").click()

#identify the Google search text box and enter the value
print("\n====== Finding Elements ======\n")
myElem = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.ID, "login-name2")))
#driver.manage().timeouts().implicitlyWait(300, TimeUnit.SECONDS);
# ENTER the username in send keys
driver.find_element_by_id("login-name2").send_keys("")
# ENTER the password in send keys
driver.find_element_by_id("login-password2").send_keys("")

driver.find_element_by_xpath("//button[@class='mega-button positive login-button large right']").click()
# //*[@id='login_form']/button/span
print("\n====== Navigating to POST LOGIN ======\n")
myElem = WebDriverWait(driver, 200).until(EC.presence_of_element_located((By.XPATH, "//span[text()='My Files']")))
print("\n====== VALIDATION FOUND ======\n")
time.sleep(10)  
#close the browser  
driver.close()  
print("PLUGIN TEST SUCCESSFUL!!!")  
