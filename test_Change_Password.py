__author__ = 'Deepak Manktala'


from CAL.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from CAL.Src.PageObject.Pages.CALLoginPage import Login
from CAL.Src.PageObject.Pages.CALForgotPasswordPage import Forgot
from CAL.Src.PageObject.Pages.CALFogotEmailConfirmation import ForgotConfirm
from CAL.Src.PageObject.Pages.CALChangePasswordConfirm import ChangePasswordConfirm
from CAL.Src.PageObject.Pages.CALChangePassword import ChangePassword
from CAL.Test.TestUtility.ScreenShot import SS
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CAL_Change_Password(EnvironmentSetup):

    def test_Login_Page(self):

# Screenshots relative paths
        ss_path = "/Test_CAL_Change_Password/"

# Using the driver instpances created in EnvironmentSetup
        driver = self.driver
        self.driver.get("https://cal.omniintegrate.com/omnisolutions")
        self.driver.set_page_load_timeout(20)

# Creating object of SS screenshots utility
        ss = SS(driver)
        expected_title = "Login - Omni Global Solutions"
# Validating Page title with the expected one through catching exception

        try:
            if driver.title == expected_title:
                print("Omni Login WebPage loaded successfully")
                self.assertEqual(driver.title,expected_title)
        except Exception as e:
            print('e'+ "WebPage Failed to load")

# verifying if the logo present or not in homepage
# creating an instance of class and passing the current driver instance

        m = Login( driver )
        if m.getlogo().is_displayed():
            print(m.getlogo().get_attribute('title')+" Logo Successfully Displayed")
        else:
            print("Omni Logo not Displayed")
#asserting other elements in the home page
        try:
            print("Sign in button is available as  "+m.getsignin().get_attribute('id'))
            print("Remember box  with "+str(m.getcheckbox().get_attribute('class'))+" is visible.")

        except Exception as e:
            print(e)
            print("Element not present")

        #Follow normal login flow
        x = Login(driver)
        ss.ScreenShot( ss_path + "LoginPage.png" )
        # Entering the username in the corresponding field
        x.username.clear()
        x.username.send_keys( "Deepak" )
        # Entering the password
        x.password.clear()
        x.password.send_keys( "Omni@123" )
        # clicking check box and taking screen shot
        x.rememberme_checkbox.click()
        ss.ScreenShot( ss_path + "Enteredcredentials.png" )
        x.sign_in.send_keys(Keys.RETURN)
        sleep( 15 )

        y = ChangePassword(driver)
        y.hello_user.send_keys(Keys.RETURN)
        sleep(2)
        y.change_password.send_keys(Keys.RETURN)
        sleep(10)

        changepasswordlink = driver.find_element_by_xpath("//a[text()='Change your password']")
        changepasswordlink.send_keys(Keys.RETURN)

        sleep(7)

        z = ChangePasswordConfirm(driver)
        z.chngpwdoldpwd.clear()
        z.chngpwdoldpwd.send_keys("Omni@123")
        z.chngpwdnewpwd.clear()
        z.chngpwdnewpwd.send_keys("Omni@123")
        z.chngpwdconfirmpwd.clear()
        z.chngpwdconfirmpwd.send_keys("Omni@123")
        sleep(1)
        z.changepwdbutton.send_keys(Keys.RETURN)

        self.driver.set_page_load_timeout( 20 )
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//p[text()='Your password has been changed.']") ))
        if self.driver.element.is_displayed():
            print("Your password is changed successfully ")

        else:
            print( "Password change had an issue" )

        ss.ScreenShot( ss_path + "PasswordChanged.png" )

        # Sign out from the Project board status
        temp_sign_out = driver.find_element( By.XPATH, "//a[contains(text(),'Sign Out')]" )
        temp_sign_out.click()
        sleep( 4 )
        ss.ScreenShot( ss_path + "SignedOut.png" )
        # self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//input[@id='UserName']") ))
        sleep( 5 )

if __name__ == '__main__':
    unittest.main()
