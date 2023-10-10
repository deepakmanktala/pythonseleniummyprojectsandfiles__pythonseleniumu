__author__ = 'Deepak Manktala'


from CAL.Src.TestBase.EnvironmentSetUp import EnvironmentSetup
from CAL.Src.PageObject.Pages.CALLoginPage import Login
from CAL.Test.TestUtility.ScreenShot import SS
from time import sleep
import requests # $ python -m pip install requests
from requests.auth import HTTPBasicAuth
import json
from selenium.webdriver.common.keys import Keys
from CAL.Src.PageObject.Pages.CALBoardStatusPage import BoardStatus
from CAL.Src.PageObject.Pages.CALProjectBoardPage import ProjectBoard
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By
from builtins import classmethod
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC
import unittest

class CAL_Board_Status(EnvironmentSetup):

    def test_Login_Page(self):

# Screenshots relative paths
        ss_path = "/Test_CLA_Board_Status_Page/"

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
        sleep(3)
        m.sign_in.send_keys(Keys.RETURN)
        sleep(4)


        self.driver.set_page_load_timeout(20)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//a[@title='Manage' and contains(text(),'Hello')]") ))
        if self.driver.element.is_displayed():
            print("User is able to login successfully with valid credentials")
        else:
            print("Login not successful")

        ss.ScreenShot( ss_path + "ProjectStatus.png" )


        o = ProjectBoard(driver)
        o.board_status_link.send_keys(Keys.RETURN)

        # p = BoardStatus(driver)
        # p.driver.element = WebDriverWait( p.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//h1[contains(text(),'Board Status')]" )))
        # p.board_type_dropdown.send_keys(Keys.RETURN)
        # sleep(1)

        selecteddropdown = Select(driver.find_element_by_xpath("//select[@id='SelectedBoard']"))
        selecteddropdown.select_by_value("2")
        print("Value 2 is selected")
        sleep(7)

        x = BoardStatus(driver)
        print("Value 2 is selected")
        sleep(10)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//b[(text()='Visa')]") ))
        print("Value 2 is selected")

        Visa = driver.find_element_by_xpath("//a[@href='https://cal.omniintegrate.com/OmniSolutions/JIRA/Board/GetBoardIssues?boardID=2&labels=Visa&boardName=mPOS_Contactless%20cards']")
        Visa.send_keys(Keys.RETURN)
        print("Visa is selected")
        sleep(4)

        ss.ScreenShot( ss_path + "VisaTestCases.png" )
        sleep(4)
        self.driver.find_element_by_xpath("//li[@class='Done']").click()
        ss.ScreenShot( ss_path + "DoneVisaTestCases.png" )
        sleep(2)
        self.driver.find_element_by_xpath("//p[text()='InQA']").click()
        ss.ScreenShot( ss_path + "InQAVisaTestCases.png" )
        sleep(2)
        self.driver.find_element_by_xpath("//p[text()='ToDo']").click()
        ss.ScreenShot( ss_path + "ToDoVisaTestCases.png" )
        sleep(2)

        self.driver.back()
        sleep(5)

        selecteddropdown = Select(driver.find_element_by_xpath("//select[@id='SelectedBoard']"))
        selecteddropdown.select_by_value("2")
        print("Value 2 is selected")
        sleep(7)
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//b[(text()='MasterCard')]") ))
        print("Value 2 is selected")

        MC = driver.find_element_by_xpath("//a[@href='https://cal.omniintegrate.com/OmniSolutions/JIRA/Board/GetBoardIssues?boardID=2&labels=MasterCard&boardName=mPOS_Contactless%20cards']")
        MC.send_keys(Keys.RETURN)
        print("Master Card from other project is selected")
        sleep(4)
        ss.ScreenShot( ss_path + "MCTestCases.png" )
        sleep(4)
        self.driver.find_element_by_xpath("//li[@class='Done']").click()
        ss.ScreenShot( ss_path + "DoneMCTestCases.png" )
        sleep(2)


        self.driver.find_element_by_xpath( "//p[text()='InQA']" ).click()
        ss.ScreenShot( ss_path + "InQAMCTestCases.png" )
        sleep( 2 )
        self.driver.find_element_by_xpath( "//p[text()='ToDo']" ).click()
        ss.ScreenShot( ss_path + "ToDoMCTestCases.png" )
        sleep( 2 )
        sleep(2)
        # all_options       = [z.get_attribute('value') for z in selecteddropdown.options]
        #
        # for x in all_options:
        #     selecteddropdown.select_by_value(x)
        #     sleep(4)

#         p.demo_board1.send_keys(Keys.RETURN)
#         sleep(5)
# #         n = ProjectBoard(driver)
#
#         #Printing values of First project EC
#         FirstProject= (n.getprojectkey1().get_attribute("innerHTML"))
#         #project1 = driver.find_element_by_xpath("//td[text()='EC')]//parent::tr")
#         project1name =driver.find_element_by_xpath("//td[text()='EC']//following-sibling::td").get_attribute("innerHTML")
#         project1status = driver.find_element_by_xpath("//td[text()='EC']//following-sibling::td[2]").get_attribute("innerHTML")
#         project1progresspercentage = driver.find_element_by_xpath("//td[text()='EC']//following-sibling::td[3]//child::div//child::div[@class='progress-bar']").get_attribute('aria-valuenow')
#         print(FirstProject+' project '+project1name + ' is having status as ' + project1status+ 'with pass percentage ' +project1progresspercentage+ ' percent.')
#
#         #Printing values of second project ECP
#
#
#         SecondProject = (n.getprojectkey2().get_attribute( "innerHTML" ))
#         # project1 = driver.find_element_by_xpath("//td[text()='EC')]//parent::tr")
#         project2name = driver.find_element_by_xpath( "//td[text()='ECP']//following-sibling::td" ).get_attribute( "innerHTML" )
#         project2status = driver.find_element_by_xpath( "//td[text()='ECP']//following-sibling::td[2]" ).get_attribute("innerHTML" )
#         project2progresspercentage = driver.find_element_by_xpath("//td[text()='ECP']//following-sibling::td[3]//child::div//child::div[@class='progress-bar']" ).get_attribute('aria-valuenow' )
#         print( SecondProject+ ' project ' + project2name + ' is having status as ' + project2status + 'with pass percentage ' + project2progresspercentage + ' percent.' )
#

        sleep(2)
        url2 = "https://jira.omniintegrate.com:8443/rest/agile/1.0/board/141/project"
        user1, password1 = "mayank.gupta@omniintegrate.com", "Omni@123"
        r2 = requests.get(url2,auth=HTTPBasicAuth(user1, password1)) # send auth unconditionally
        r2.raise_for_status() # raise an exception if the authentication fails
        data2 = str(r2.content)
        # print('Data Start')
        # print(data1)
        # print('Data End')
        data3 = str(data2[2:-1])
        # print('data 2 start')
        # print(data2)
        # print('Data 2 end in here')
        # print('JSON one key')
        jsondata1 = json.loads(data3)
        # print(jsondata["values"][0]["key"])
        # print(jsondata["values"][0]["name"])
        # print('continues watever you are doing')
        if (jsondata1["values"][0]["key"]) == "ECP":
            print(jsondata1["values"][0]["key"]+' Project'+' having name' +jsondata1["values"][0]["name"] +' exists in JIRA API sent for project status')
        else:
            print(jsondata1["values"][0]["key"]+' Project is not found from JIRA API for project status')

# # #Sign out from the Project board status
        temp_sign_out = driver.find_element( By.XPATH, "//a[contains(text(),'Sign Out')]" )
        temp_sign_out.click()
        sleep(4)
        ss.ScreenShot( ss_path + "SignedOut.png" )
        self.driver.element = WebDriverWait( self.driver, 10 ).until(EC.presence_of_element_located( (By.XPATH, "//input[@id='UserName']") ))


if __name__ == '__main__':
    unittest.main()
