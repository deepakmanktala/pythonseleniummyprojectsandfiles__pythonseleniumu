from selenium import webdriver
# create a new Firefox session
driver = webdriver.Chrome()
driver.implicitly_wait(30)
driver.maximize_window()
# navigate to the application home page
driver.get("https://www.flipkart.com/")
# get the search textbox
python_button = driver.find_elements_by_xpath("/html/body/div[2]/div/div/button")
python_button.click()

search_field = driver.find_element_by_name("q")
search_field.clear()
# enter search keyword and submit
search_field.send_keys("phones")
search_field.submit()
# get all the anchor elements which have product names displayed
# currently on result page using find_elements_by_xpath method
products = driver.find_elements_by_class_name("_2cLu-l")
# get the number of anchor elements found
driver.implicitly_wait(30)
print ("Found " + str(len(products)) + " products:")
# iterate through each anchor element and print the text that is
# name of the product
for product in products:
    print(product.text)
# close the browser window
driver.quit()