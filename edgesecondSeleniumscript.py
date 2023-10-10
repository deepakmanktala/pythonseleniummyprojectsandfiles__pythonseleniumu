from selenium import webdriver
driver = webdriver.Edge()
'''My driver path for webdriver.chrome is put in python  and python/scripts folder, other wise under chrome driver we need to put full path'''
driver.set_page_load_timeout(1800)
driver.get('http://www.facebook.com')
driver.maximize_window()
driver.implicitly_wait(120)
driver.get_screenshot_as_file("C:\\Users\owner\\PycharmProjects\\untitled\\Screeshots\\fbw1.png")
driver.find_element_by_id("email").send_keys("deepak.manktala@gmail.com")
driver.find_element_by_name("pass").send_keys("*****")
driver.find_element_by_id("loginbutton").click()
driver.get_screenshot_as_file("C:\\Users\\owner\\PycharmProjects\\untitled\\Screeshots\\omnijjw1.png")
driver.implicitly_wait(50)
driver.quit()