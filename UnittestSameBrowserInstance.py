import unittest
from selenium import webdriver

class search(unittest.TestCase):
    def setUp(inst):
        inst.driver = webdriver.Chrome()
        inst.driver.implicitly_wait(30)
        inst.driver.maximize_window()
        inst.driver.get("https://www.google.com")


    def test_search_by_text(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("Selenium Interview Questions")
        self.search_field.submit()


        lists = self.driver.find_elements_by_class_name("r")
        numberofsearch = len(lists)
        self.assertEqual(11, len(lists))

    def test_search_by_name(self):
        self.search_field = self.driver.find_element_by_name("q")
        self.search_field.clear()
        self.search_field.send_keys("Selenium  Questions")
        self.search_field.submit()


        lists = self.driver.find_elements_by_class_name("r")
        numberofsearch = len(lists)
        self.assertEqual(11, len(lists))

    def tearDown(inst):
        inst.driver.minimize_window()
        inst.driver.quit()


if __name__ == '__main__':
    unittest.main()