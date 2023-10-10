__author__ = 'Deepak Manktala'

class Locator(object):

#Generic Lcoators
        omni_logo = "//img[@title='Omni Integration']"
        copyright_label = "//span[contains(text(),'Copyright')]"
#Login  page locators

        username = "//input[@id='UserName']"
        password = "//input[@id='Password']"
        rememberme_checkbox = "//span[@class='checkmark']"
        sign_in = "//input[@id='login']"
        forgot_password = "//a[contains(text(),'Forgot Password')]"
        login_heading= "//h3[contains(text(),'Login into your account')]"
        #invalid_login = "//li[contains(text(),'Invalid login attempt.')]"

#Forgot Page Locators
        forgot_heading      = "//h3[contains(text(),'Forgot Password')]"
        emailid             = "//input[@id='Email']"
        sendlink            = "//input[@value='Send Link']"
        loginlink           = "//a[@id='loginLink']"


#Project Board page locator
        project_status_heading = "//h1[contains(text(),'Project Status')]"
        project_status_link = "//a[contains(text(),'Project Status')]"
        board_status_link = "//a[contains(text(),'Board Status')]"
        hello_user = "//a[@title='Manage' and contains(text(),'Hello')]"
        change_password = "//a[@title='Manage' and contains(text(),'Change Password')]"
        sign_out = "//a[contains(text(),'Sign Out')]"
        project_key1 = "//td[(text()='EC')]"
        project_key2 = "//td[(text()='ECP')]"

#Board Status page locators
        board_status_heading = "//h1[contains(text(),'Board Status')]"
        board_type_dropdown  = "//select[@id='SelectedBoard']"
        demo_board1          = "//option[(text()='Retailex_Application_1- Contact Cards')]"
        demo_board2          = "//option[contains(text(),'mPOS_Contactless cards')]"

#Admin Page locators

        adminlink        = "//a[text()='Admin']"
        registerlink     = "//a[@id='registerLink']"
        adminpageheading = "//h1[contains(text(),'Admin Panel')]"
        usertest1        = "//span[contains(text(),'test1')]"
        usertest2        = "//span[contains(text(),'test2')]"
        Notassigned      = "//option[contains(text(),'NotAssigned')]"
        boardmanagertest1= "//td//select[@id='UserType-12']//option[@value='BoardManager']"
        projectmanagertest1 = "//td//select[@id='UserType-12']//option[@value='ProjectManager']"
        savebuttontest1     = "//div//a[@id='Save-12']"
        roledropdown        = "//select[@id='UserType-12']"


#Registration Page Locators
#Registration Page aLocators

        registerheading     = "//h3[contains(text(),'Register')]"
        registeremail       = "//input[@id='Email']"
        registerusername    = "//input[@id='UserName']"
        registerpassword    = "//input[@id='Password']"
        registerconfirmpwd  = "//input[@id='ConfirmPassword']"
        registersubmitbutton= "//input[@type='submit' and @value='Register']"
        registercancel      = "//b[contains(text(),'Cancel')]"

#Changepassword Confirmation Page

        changepwdoldpwd     = "//input[@id='OldPassword']"
        changepwdnewpwd     = "//input[@id='NewPassword']"
        changepwdconfirmpwd = "//input[@id='ConfirmPassword']"
        changepwdbutton     = "//input[@value='Change Password']"
#BoardStatus page Locators

