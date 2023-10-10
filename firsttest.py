import unittest
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod


class SearchTest(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.implicitly_wait(30)
        cls.driver.maximize_window()
        # navigate to the application home page
        cls.driver.get("http://www.amazon.in")


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


if __name__ == '__main__':
    unittest.main(verbosity=3)