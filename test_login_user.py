__author__ = 'Deepak Manktala'


from CAL.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from CAL.Src.PageObject.Pages.CALLoginPage import Login
from CAL.Test.TestUtility.ScreenShot import SS
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CAL_Login_User(EnvironmentSetup):

    def test_Login_Page(self):

# Screenshots relative paths
        ss_path = "/Test_CLA_LoginPage/"

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

        #Screenshot before logging in
        ss.ScreenShot( ss_path + "LoginPage.png" )
        #Entering the username in the corresponding field
        m.username.clear()
        m.username.send_keys("Deepak")
        #Entering the password
        m.password.clear()
        m.password.send_keys("Omni@123")
        #clicking check box and taking screen shot
        m.rememberme_checkbox.click()
        ss.ScreenShot( ss_path + "Enteredcredentials.png" )
        sleep(15)
        m.sign_in.send_keys(Keys.RETURN)
        sleep(4)


        self.driver.set_page_load_timeout(20)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//a[@title='Manage' and contains(text(),'Hello')]") ))
        if self.driver.element.is_displayed():
            print("User is able to login successfully with valid credentials")
        else:
            print("Login not successful")

        ss.ScreenShot( ss_path + "ProjectStatus.png" )

        #Sign out from the Project board status
        temp_sign_out = driver.find_element( By.XPATH, "//a[contains(text(),'Sign Out')]" )
        temp_sign_out.click()
        sleep(4)
        ss.ScreenShot( ss_path + "SignedOut.png" )
        #self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//input[@id='UserName']") ))
        sleep(5)
        n = Login( driver )
    #Sign In Using Invalid Username and Invalid Password credentials
        n.username.clear()
        n.username.send_keys("Deeeepak")
        #Entering the password
        n.password.clear()
        n.password.send_keys("Omnnnni@123")
        #clicking check box and taking screen shot
        n.rememberme_checkbox.click()
        ss.ScreenShot( ss_path + "InvalidUserandpassword.png" )
        n.sign_in.send_keys(Keys.RETURN)
        sleep(4)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//li[contains(text(),'Invalid login attempt.')]") ))


        o = Login( driver )
        #Sign In Using Invalid Username and Valid Password credentials
        o.username.clear()
        sleep(3)
        o.username.send_keys("Deeeepak")
        #Entering the password
        o.password.clear()
        o.password.send_keys("Omni@123")
        #clicking check box and taking screen shot
        o.rememberme_checkbox.click()
        ss.ScreenShot( ss_path + "wrongusername.png" )
        o.sign_in.click()
        sleep(4)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//li[contains(text(),'Invalid login attempt.')]") ))

        p = Login(driver)
        #Sign In Using Valid Username and Invalid Password credentials
        p.username.clear()
        sleep(3)
        p.username.send_keys("Deepak")
        #Entering the password
        p.password.clear()
        p.password.send_keys("Omnnnni@123")
        #clicking check box and taking screen shot
        p.rememberme_checkbox.click()
        ss.ScreenShot( ss_path + "WrongPassword.png" )
        p.sign_in.click()
        sleep(4)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//li[contains(text(),'Invalid login attempt.')]") ))
        ss.ScreenShot( ss_path + "Invalid.png" )
        print("Invalid credentials do not allow access")

if __name__ == '__main__':
    unittest.main()
