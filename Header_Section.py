"""
Page object model for the page header
"""
from Page import Page


class Header_Section(Page):
    "Page object for the page header"

    def start(self):
        "Xpath of all the field"
        #Search and profile
        self.search_textbox = "//input[@id='gbqfq']"
        self.search_button = "//button[@id='gbqfb']"
        self.account_dropdown = "//a[@title='Google Account: test@qxf2.com']"
        self.signout_button = "//a[text()='Sign out']"
        self.search_result = "//span[contains(text(),'%s')]"


    def search_by_subject(self,searchtext):
        self.set_text(self.search_textbox,'subject:'+searchtext)
        self.click_element(self.search_button)
        self.wait(3)
        self.driver.refresh()
        self.wait(3)
        if self.check_element_present(self.search_result%searchtext):
            self.click_element(self.search_result%searchtext)
            self.write("Message for query '%s'"%searchtext)
            return True
        else:
            self.write("No search result")
            return False
        
        
        
        
        
    

