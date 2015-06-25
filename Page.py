"""
Page class that all page models can inherit from
There are useful wrappers for common Selenium operations
"""

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
import unittest,time,logging
from Base_Logging import Base_Logging

class Page(unittest.TestCase):
    "Page class that all page models can inherit from"

    def __init__(self,selenium_driver,base_url='https://mail.google.com/'):
        "Constructor"
        #We assume relative URLs start without a / in the beginning
        if base_url[-1] != '/': 
            base_url += '/' 
        self.base_url = base_url
        self.driver = selenium_driver
        self.start() #Visit and initialize xpaths for the appropriate page

        self.log_obj = Base_Logging(level=logging.DEBUG)
     

    def open(self,url):
        "Visit the page base_url + url"
        url = self.base_url + url
        if self.driver.current_url != url:
            self.driver.get(url)


    def get_page_xpaths(self,section):
        "open configurations file,go to right sections,return section obj"
        pass
        

    def get_xpath(self,xpath):
        "Return the DOM element of the xpath OR the 'None' object if the element is not found"
        dom_element = None
        dom_element = self.driver.find_element_by_xpath(xpath)
        return dom_element
    
    
    def click_element(self,xpath):
        "Click the button supplied"
        link = self.get_xpath(xpath)
        if link is not None:
            try:
                link.click()
            except Exception,e:
                self.write('Exception when clicking link with xpath: %s'%xpath)
                self.write(e)
            else:
                return True

        return False
    
               
    def set_text(self,xpath,value):
        "Set the value of the text field"
        text_field = self.get_xpath(xpath)
        try:
            text_field.clear()
        except Exception, e:
            self.write('ERROR: Could not clear the text field: %s'%xpath)
        if value is None:
          return
        else:
          text_field.send_keys(value)
          
          
    def get_text(self,xpath):
        "Return the text for a given xpath or the 'None' object if the element is not found"
        text = ''
        try:
            text = self.get_xpath(xpath).text
        except Exception,e:
            self.write(e)
            return None
        else:
            return text.encode('utf-8')
        

    def get_dom_text(self,dom_element):
        "Return the text of a given DOM element or the 'None' object if the element has no attribute called text"
        text = ''
        try:
            text = dom_element.text
        except Exception, e:
            self.write(e)
            return None
        else:
            return text.encode('utf-8')
        

    def select_dropdown_option(self, select_locator, option_text):
        "Selects the option in the drop-down"
        #dropdown = self.driver.find_element_by_id(select_locator)
        dropdown = self.driver.find_element_by_xpath(select_locator)
        for option in dropdown.find_elements_by_tag_name('option'):
            if option.text == option_text:
                option.click()
                break


    def check_element_present(self,xpath):
        " This method checks if the web element is present in page or not and returns True or False accordingly"
        try:
            self.get_xpath(xpath)
        except NoSuchElementException:
            return False
        return True
    
            
    def submit_search(self):
        " Clicks on Search button"
        self.click_button(self.search_button)

                        
    def teardown(self):
        " Tears down the driver"
        self.driver.close()
        

    def write(self,msg,level='info'):
        " This method can be used to include logging"
        #print msg
        self.log_obj.write(msg,level)
        

    def wait(self,wait_seconds=5):
        " Performs wait for time provided"
        time.sleep(wait_seconds)
