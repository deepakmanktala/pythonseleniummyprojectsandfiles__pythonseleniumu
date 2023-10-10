# Entering the username in the corresponding field
m.username.clear()
m.username.send_keys( "Deepak" )
# Entering the password
m.password.clear()
m.password.send_keys( "Omni@123" )
# clicking check box and taking screen shot
m.rememberme_checkbox.click()
ss.ScreenShot( ss_path + "Enteredcredentials.png" )
m.signin.click()
sleep( 4 )

self.driver.set_page_load_timeout( 20 )
self.driver.element = WebDriverWait( self.driver, 10 ).until(
    EC.presence_of_element_located( (By.XPATH, "//a[@title='Manage' and contains(text(),'Hello')]") ) )
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
n = Login( driver )
# Sign In Using Invalid Username and Invalid Password credentials
n.username.clear()
n.username.send_keys( "Deeeepak" )
# Entering the password
n.password.clear()
n.password.send_keys( "Omnnnni@123" )
# clicking check box and taking screen shot
n.rememberme_checkbox.click()
ss.ScreenShot( ss_path + "InvalidUserandpassword.png" )
n.signin.click()
sleep( 4 )
self.driver.element = WebDriverWait( self.driver, 10 ).until(
    EC.presence_of_element_located( (By.XPATH, "//li[contains(text(),'Invalid login attempt.')]") ) )

o = Login( driver )
# Sign In Using Invalid Username and Valid Password credentials
o.username.clear()
sleep( 3 )
o.username.send_keys( "Deeeepak" )
# Entering the password
o.password.clear()
o.password.send_keys( "Omni@123" )
# clicking check box and taking screen shot
o.rememberme_checkbox.click()
ss.ScreenShot( ss_path + "wrongusername.png" )
o.signin.click()
sleep( 4 )
self.driver.element = WebDriverWait( self.driver, 10 ).until(
    EC.presence_of_element_located( (By.XPATH, "//li[contains(text(),'Invalid login attempt.')]") ) )

p = Login( driver )
# Sign In Using Valid Username and Invalid Password credentials
p.username.clear()
sleep( 3 )
p.username.send_keys( "Deepak" )
# Entering the password
p.password.clear()
p.password.send_keys( "Omnnnni@123" )
# clicking check box and taking screen shot
p.rememberme_checkbox.click()
ss.ScreenShot( ss_path + "WrongPassword.png" )
p.signin.click()
sleep( 4 )
self.driver.element = WebDriverWait( self.driver, 10 ).until(
    EC.presence_of_element_located( (By.XPATH, "//li[contains(text(),'Invalid login attempt.')]") ) )
ss.ScreenShot( ss_path + "Invalid.png" )
print( "Invalid credentials do not allow access" )
