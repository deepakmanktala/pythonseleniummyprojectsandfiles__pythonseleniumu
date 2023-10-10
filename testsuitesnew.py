import unittest
from fbtests import HomePageTest
from firsttest import SearchTest

# get all tests from SearchProductTest and HomePageTest class
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_test])
# run the suite
unittest.TextTestRunner(verbosity=4).run(smoke_tests)