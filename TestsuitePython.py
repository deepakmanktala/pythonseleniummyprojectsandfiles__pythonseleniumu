import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod


class HomePageTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://www.amazon.in")
        cls.driver.implicitly_wait( 30 )



    def test_next_page_ad(self):
        # check language options dropdown on Home page
        self.assertTrue( self.is_element_present(By.ID, "// *[contains( @ id,'gw-desktop-herotator')] / div / div / div / div[3] / a / i / span" ) )

    def test_shopping_cart_empty_message(self):
        # check content of My Shopping Cart block on Home page
        shopping_cart_icon = self.driver.find_element_by_css_selector("#nav-cart > span.nav-cart-icon.nav-sprite")
        shopping_cart_icon.click()
        shopping_cart_status = \
            self.driver.find_element_by_css_selector("p.empty").text
        self.assertEqual( "Your Shopping Cart is empty.",shopping_cart_status )
        close_button = self.driver.find_element_by_css_selector("#activeCartViewForm > div > p > a:nth-child(3)")
        close_button.click()



    def test_search_by_category(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id( "twotabsearchtextbox" )
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys( "phones" )
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//*[contains(@id,'result_18')]/div/div[3]/div[1]/a/h2")
        self.assertEqual( 1, len( products ) )


    def test_search_by_name(self):
        # get the search textbox
        self.search_field = self.driver.find_element_by_id( "twotabsearchtextbox" )
        self.search_field.clear()
        # enter search keyword and submit
        self.search_field.send_keys( "salt shaker" )
        self.search_field.submit()
        # get all the anchor elements which have product names
        # displayed currently on result page using
        # find_elements_by_xpath method
        products = self.driver.find_elements_by_xpath("//*[contains(@id,'result_1')]/div/div[3]/div[1]/a/h2")
        self.assertEqual( 0, len( products ) )
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