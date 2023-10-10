from selenium import webdriver
driver = webdriver.Chrome()
'''My driver path for webdriver.chrome is put in python  and python/scripts folder, other wise under chrome driver we need to put full path'''
driver.set_page_load_timeout(1800)
driver.get('http://www.omniintegrate.com')
driver.maximize_window()
driver.implicitly_wait(120)
driver.get_screenshot_as_file("omni1.png")
driver.quit()