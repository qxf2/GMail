"""
Page object model for the main page
"""
from Page import Page
from Header_Section import Header_Section
from Nav_Menu import Nav_Menu


class Main_Page(Page):
    "Page object for the Main page"

    def start(self):
        self.url = ""
        self.open(self.url) 

        #Create a Header Section object
        self.header_obj = Header_Section(self.driver)
        #Create a Menu object
        self.menu_obj = Nav_Menu(self.driver)
        
