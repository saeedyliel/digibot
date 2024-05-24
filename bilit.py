from selenium import webdriver
from selenium.webdriver.support import expected_conditions as Ec
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

driver=webdriver.Firefox()
driver.get('https://alibaba.ir')


btn='/html/body/div[1]/div[1]/header/div[1]/div/div/div/button'
btn_click=WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,btn)))
btn_click.click()


mobile_input='/html/body/div/div[2]/div/div/form/div[1]/div/input'
user_input=WebDriverWait(driver,10).until(Ec.element_to_be_clickable((By.XPATH,mobile_input)))
user_input.send_keys('9168194573')
user_input.send_keys(Keys.ENTER)


# btn='//*[@id="auth"]/div/form/div[2]/button[1]'
# btn_click=WebDriverWait(driver,10).until(Ec.element_to_be_clickable(By.XPATH,(btn)))
# btn_click.click()