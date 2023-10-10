import selenium
from selenium import webdriver

driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.get("https://www.fedex.com/apps/fedextrack")
driver.implicitly_wait(130)
driver.find_element_by_class_name("//*[@id=""]/div/form/div[1]/div/form/div[1]/div/div/input").clear()
driver.find_element_by_class_name("//*[@id=""]/div/form/div[1]/div/form/div[1]/div/div/input").send_keys("1235555566")
driver.find_element_by_class_name("//*[@id=""]/div/form/div[1]/div/form/div[1]/div/div/input").submit()

print("Tracking info for shipment")

