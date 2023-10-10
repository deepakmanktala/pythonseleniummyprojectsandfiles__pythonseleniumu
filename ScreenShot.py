__author__ = 'Deepak Manktala'


from selenium import webdriver
class SS(object):

    def __init__(self, driver):
        self.driver = driver

    def ScreenShot(self, path):
        directory = "C:/Users/owner/PycharmProjects/Omni-CAL/CAL/Screenshots"
        self.driver.get_screenshot_as_file(directory+path)