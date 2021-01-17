from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Firefox(executable_path="PATH_TO_GECKODRIVER")
driver.get('https://web.whatsapp.com/')
wait = WebDriverWait(driver, 60)
name = 'Name'
msg = 0
count = 500
wait.until(EC.presence_of_element_located(
    (By.XPATH, f'//span[@title = "{name}"]')))
user = driver.find_element_by_xpath(f'//span[@title = "{name}"]')
user.click()
inp_xpath = '//*[@id="main"]/footer/div[1]/div[2]/div/div[2]'
input_box = wait.until(EC.presence_of_element_located((
    By.XPATH, inp_xpath)))
for i in range(count):
    input_box.send_keys(msg + Keys.ENTER)
