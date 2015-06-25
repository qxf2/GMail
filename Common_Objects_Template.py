"""
Page object model for the Main
"""
from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from Page import Page
from Header_Section import Header_Section
from Nav_Menu import Nav_Menu


class Common_Objects_Template(Header_Section,Nav_Menu):
    "Page object for the Main page"

    def start(self):
        """self.header_obj = Header_Page(self.driver)"""
        "Xpath of all the field"
        #Main
        
