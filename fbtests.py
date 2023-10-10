import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
import time


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("https://www.facebook.com")




    def test_email_home_page(self):
        # check language options dropdown on Home page
        self.assertTrue( self.is_element_present(By.ID, "email") )

    def test_fb_password(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.is_element_present(By.ID,"pass")
        self.assertTrue( self.is_element_present( By.ID, "pass" ) )

    def test_fb_login(self):
        wait = WebDriverWait( self, 10 )
        user = self.driver.find_element_by_id("email")
        user.clear()
        user.send_keys("deepak.manktala@gmail.com")
        fbpwd = self.driver.find_element_by_id("pass")
        fbpwd.clear()
        fbpwd.send_keys("Muktsar@33")
        wait.until( EC.visibility_of_element_located(self.driver.find_element_by_xpath("//*[contains(@id,'u_0_4')]"))).click()
        self.assertTrue( self.is_element_present( By.CLASS_NAME, "_2md" ) )

    def test_fb_login_with_lambda(self):
        driver = self.driver
        facebookUsername = 'deepak.manktala@gmail.com'
        facebookPassword = 'Muktsar@33'

        emailFieldID = 'email'
        passFieldID = 'pass'
        loginButtonXpath = '//*[@id="u_0_2"]'
        fbLogoXpath = '//*[@id="js_1d"]/div/div/div[1]/div[1]/h1/a'

        emailFieldElement = WebDriverWait( driver, 10 ).until(
            lambda driver: driver.find_element_by_id( emailFieldID ) )
        passFieldElement = WebDriverWait( driver, 10 ).until( lambda driver: driver.find_element_by_id( passFieldID ) )
        loginButtonElement = WebDriverWait( driver, 10 ).until(
            lambda driver: driver.find_element_by_xpath( loginButtonXpath ) )
        emailFieldElement.clear()
        emailFieldElement.send_keys( facebookUsername )
        passFieldElement.clear()
        passFieldElement.send_keys( facebookPassword )
        loginButtonElement.click()
        WebDriverWait( driver, 10 ).until( lambda driver: driver.find_element_by_xpath( fbLogoXpath ) )

    # def test_search_by_category(self):
    #     # get the search textbox
    #     self.search_field = self.driver.find_element_by_id( "twotabsearchtextbox" )
    #     self.search_field.clear()
    #     # enter search keyword and submit
    #     self.search_field.send_keys( "phones" )
    #     self.search_field.submit()
    #     # get all the anchor elements which have product names
    #     # displayed currently on result page using
    #     # find_elements_by_xpath method
    #     products = self.driver.find_elements_by_xpath("//*[contains(@id,'result_18')]/div/div[3]/div[1]/a/h2")
    #     self.assertEqual( 1, len( products ) )
    #
    #
    # def test_search_by_name(self):
    #     # get the search textbox
    #     self.search_field = self.driver.find_element_by_id( "twotabsearchtextbox" )
    #     self.search_field.clear()
    #     # enter search keyword and submit
    #     self.search_field.send_keys( "salt shaker" )
    #     self.search_field.submit()
    #     # get all the anchor elements which have product names
    #     # displayed currently on result page using
    #     # find_elements_by_xpath method
    #     products = self.driver.find_elements_by_xpath("//*[contains(@id,'result_1')]/div/div[3]/div[1]/a/h2")
    #     self.assertEqual( 0, len( products ) )
    @classmethod
    def tearDown(cls):
           # close the browser window
        cls.driver.quit()

    def is_element_present(self, how, what):
        """
        Utility method to check presence of an element on page
        :params how: By locator type
        :params what: locator value
        """
        try:
            self.driver.find_element( by=how, value=what )
        except NoSuchElementException as e: return False
        return True

if __name__ == '__main__':
    unittest.main(verbosity=3)