__author__ = 'Deepak Manktala'


from CAL.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from CAL.Src.PageObject.Pages.CALLoginPage import Login
from CAL.Src.PageObject.Pages.CALForgotPasswordPage import Forgot
from CAL.Src.PageObject.Pages.CALFogotEmailConfirmation import ForgotConfirm
from CAL.Test.TestUtility.ScreenShot import SS
from time import sleep
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CAL_Forgot_Password(EnvironmentSetup):

    def test_Login_Page(self):

# Screenshots relative paths
        ss_path = "/Test_CAL_Forgot_Page/"

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

        print("Forgot password link is"+str(m.getforgotpassword().get_attribute('href')))
        #Screenshot before logging in
        ss.ScreenShot( ss_path + "ForgotPasswordLoginPage.png" )

        m.forgot_password.click()
        self.driver.element = WebDriverWait( self.driver, 10 ).until( EC.presence_of_element_located( (By.XPATH, "//input[@value='Send Link']") ) )
        ss.ScreenShot( ss_path + "ForgotPasswordLandingPage.png" )
        sleep(4)
        print("Forgot password page is displayed")
        #Instantitaing new object p for forgot password link
        p = Forgot( driver )
        p.emailid.clear()
        p.emailid.send_keys("deepak.manktala@omniintegrate.com")
        p.sendlink.click()
        print("Password link is sent on email entered."  )
        sleep(5)

        self.driver.element = WebDriverWait( self.driver, 20 ).until( EC.presence_of_element_located( (By.XPATH, "//p[contains(text(),'Please check your email to reset your password')]") ) )
        print("Forgot password link confirmation is displayed")
        ss.ScreenShot( ss_path + "AfterMailSent.png" )

        #Click on Sign in link
        n = ForgotConfirm(driver)
        n.loginlink.click()

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
        x.sign_in.click()
        sleep( 10 )

        self.driver.set_page_load_timeout( 20 )
        self.driver.element = WebDriverWait( self.driver, 10 ).until(  EC.presence_of_element_located( (By.XPATH, "//a[@title='Manage' and contains(text(),'Hello')]") ) )
        if self.driver.element.is_displayed():
            print( "User is able to login successfully with valid credentials" )
        else:
            print( "Login not successful" )

        ss.ScreenShot( ss_path + "ProjectStatus.png" )

        # Sign out from the Project board status
        temp_sign_out = driver.find_element( By.XPATH, "//a[contains(text(),'Sign Out')]" )
        temp_sign_out.click()
        sleep( 4 )
        ss.ScreenShot( ss_path + "SignedOut.png" )
        # self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//input[@id='UserName']") ))
        sleep( 5 )

if __name__ == '__main__':
    unittest.main()
