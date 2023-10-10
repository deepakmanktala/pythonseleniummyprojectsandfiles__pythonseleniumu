from selenium import webdriver
import re

driver = webdriver.Chrome()
driver.get('https://www.tripsavvy.com/telephone-numbers-for-top-airlines-54594')

doc = driver.page_source
print(doc)
phones = re.findall(r'[\d]{3}-?[\d]{3}-[\d]{4}', doc)

for phone in phones:
    print(phone)