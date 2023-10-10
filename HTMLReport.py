import unittest
import HtmlTestRunner
import os
from fbtests import HomePageTest
from firsttest import SearchTest
# get the directory path to output report file
dir = os.getcwd()

# get all tests from SearchProductTest and HomePageTest class
search_test = unittest.TestLoader().loadTestsFromTestCase(SearchTest)
home_page_tests = unittest.TestLoader().loadTestsFromTestCase(HomePageTest)
# create a test suite combining search_test and home_page_test
smoke_tests = unittest.TestSuite([home_page_tests, search_test])
# open the report file
outfile = open(dir + "\SmokeTestReport.html", "w")
# configure HTMLTestRunner options
#coder1= HtmlTestRunner.HTMLTestRunner()
runner = HtmlTestRunner.HTMLTestRunner( output='C:\\Users\\owner\\PycharmProjects\\untitled\\Unittest\\', stream=outfile, report_title= 'Test Report', descriptions='Smoke Tests')
# run the suite using HTMLTestRunner
runner.run(smoke_tests)