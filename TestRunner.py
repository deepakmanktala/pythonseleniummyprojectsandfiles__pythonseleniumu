from unittest import TestLoader, TestSuite, TextTestRunner
from CAL.Test.Scripts.test_Login_Page import CAL_LOGIN
from CAL.Test.Scripts.test_login_user import CAL_Login_User
from CAL.Test.Scripts.test_forgot_password import CAL_Forgot_Password
from CAL.Test.Scripts.test_board_status_page import CAL_Board_Status
from CAL.Test.Scripts.test_Project_Status_Page import CAL_Project_Status
from CAL.Test.Scripts.test_Register_Page import CAL_Register_New_User
from CAL.Test.Scripts.test_Login_Admin_Page import CAL_Admin_Login_User

import testtools as testtools


if __name__ == "__main__":

    loader = TestLoader()
    suite = TestSuite((
        loader.loadTestsFromTestCase( CAL_Login_User),
        loader.loadTestsFromTestCase( CAL_LOGIN),
        loader.loadTestsFromTestCase( CAL_Forgot_Password),
        loader.loadTestsFromTestCase( CAL_Admin_Login_User ),
        loader.loadTestsFromTestCase( CAL_Project_Status ),
        loader.loadTestsFromTestCase( CAL_Board_Status ),
        loader.loadTestsFromTestCase( CAL_Register_New_User ),

        ))

#run test sequentially using simple TextTestRunner
    runner = TextTestRunner(verbosity=3)
    runner.run(suite)


# #run test parallel using concurrent_suite
    concurrent_suite = testtools.ConcurrentStreamTestSuite(lambda: ((case, None) for case in suite))
    concurrent_suite.run(testtools.StreamResult())