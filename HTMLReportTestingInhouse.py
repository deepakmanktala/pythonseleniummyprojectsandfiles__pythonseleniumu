import unittest
import HtmlTestRunner
import os
from CAL.Test.Scripts.test_login_user import CAL_Login_User
from CAL.Test.Scripts.test_Login_Page import CAL_LOGIN
from CAL.Test.Scripts.test_forgot_password import CAL_Forgot_Password
from CAL.Test.Scripts.test_Login_Admin_Page import CAL_Admin_Login_User
from CAL.Test.Scripts.test_Project_Status_Page import CAL_Project_Status
from CAL.Test.Scripts.test_board_status_page import CAL_Board_Status
from CAL.Test.Scripts.test_Register_Page import CAL_Register_New_User
# get the directory path to output report file
dir = os.getcwd()

# get all tests from Login, Forgot,Project and Board
#login_user_test         = unittest.TestLoader().loadTestsFromTestCase(CAL_LOGIN)
# login_test              = unittest.TestLoader().loadTestsFromTestCase(CAL_Login_User)
# forgot_test             = unittest.TestLoader().loadTestsFromTestCase(CAL_Forgot_Password)
# project_status_test     = unittest.TestLoader().loadTestsFromTestCase(CAL_Project_Status)
board_status_test       = unittest.TestLoader().loadTestsFromTestCase(CAL_Board_Status)
# admin_login_test        = unittest.TestLoader().loadTestsFromTestCase(CAL_Admin_Login_User)
# register_user_test      = unittest.TestLoader().loadTestsFromTestCase(CAL_Register_New_User)
# # create a test suite combining different tests
smoke_tests = unittest.TestSuite([board_status_test])
# open the report file
outfile = open(dir + "\SmokeTestReport1.html", "w")
# configure HTMLTestRunner options
#coder1= HtmlTestRunner.HTMLTestRunner()
runner = HtmlTestRunner.HTMLTestRunner( output='C:\\Users\\owner\\PycharmProjects\\Omni-CAL\\CAL\\Test\\TestReport\\', stream=outfile, report_title= 'Test Report', descriptions='Smoke Tests')
# run the suite using HTMLTestRunner
runner.run(smoke_tests)