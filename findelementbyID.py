from selenium import webdriver

driver = webdriver.Chrome()

driver.get("https://www.google.com")

try:
    driver.find_element_by_class_name("gb_P")
    print("Test Pass ID Found")

except Exception as e:
    print("Exception found test fail", format(e))

driver.close()