from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver = webdriver.Chrome()
'''My driver path for webdriver.chrome is put in python  and python/scripts folder, other wise under chrome driver we need to put full path'''
driver.set_page_load_timeout(1800)
print(driver.title)
driver.get('http://www.python.org')
driver.maximize_window()
driver.implicitly_wait(120)
driver.get_screenshot_as_file("C:\\Users\owner\\PycharmProjects\\untitled\\Screeshots\\python3.png")

print(driver.title)
assert "Python" in driver.title
assert "to" in driver.title

elem = driver.find_element_by_name("q")
elem.clear()
elem.send_keys("pycon")
elem.send_keys(Keys.RETURN)

assert "India " in driver.page_source

driver.find_element_by_id("email").send_keys("deepak.manktala@gmail.com")
driver.find_element_by_name("pass").send_keys("M*****3")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("C:\\Users\\owner\\PycharmProjects\\untitled\\Screeshots\\python77.png")
driver.implicitly_wait(50)
driver.quit()