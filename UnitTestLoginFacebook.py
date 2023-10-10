import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait

import time

class PythonOrgSearch(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get("https://www.facebook.com/")
        self.driver.maximize_window()


    '''Test case method should start with text test'''
    def test_fb_login(self):
        driver = self.driver
        facebookUsername='deepak.manktala@gmail.com'
        facebookPassword= 'Muktsar@33'

        emailFieldID = 'email'
        passFieldID = 'pass'
        loginButtonXpath = '//*[@id="u_0_2"]'
        fbLogoXpath = '//*[@id="js_1d"]/div/div/div[1]/div[1]/h1/a'


        emailFieldElement  = WebDriverWait(driver, 10).until( lambda driver: driver.find_element_by_id(emailFieldID))
        passFieldElement   = WebDriverWait(driver, 10).until( lambda  driver: driver.find_element_by_id(passFieldID))
        loginButtonElement = WebDriverWait(driver, 10).until( lambda driver: driver.find_element_by_xpath(loginButtonXpath))
        emailFieldElement.clear()
        emailFieldElement.send_keys(facebookUsername)
        passFieldElement.clear()
        passFieldElement.send_keys(facebookPassword)
        loginButtonElement.click()

        WebDriverWait(driver, 10).until( lambda driver: driver.find_element_by_xpath(fbLogoXpath))



    def tearDown(self):
        self.driver.quit()

if __name__=="__main__":
    unittest.main()









'''
driver = webdriver.Chrome()
'''
'''My driver path for webdriver.chrome is put in python  and python/scripts folder, other wise under chrome driver we need to put full path'''
'''driver.set_page_load_timeout(1800)
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
driver.quit()'''