"""
Page object model for the login page
"""
from Page import Page


class Nav_Menu(Page):
    "Page object for the side menu"

    def start(self):      
        "Xpath of all the field"
        #Navigation Menu
        self.inbox = "//a[contains(@href, '#inbox')]"
        self.sent_mail = "//a[contains(@href, '#sent')]"
        self.drafts= "//a[contains(@href, '#drafts')]"
		
	
    def select_menu_item(self,menu_item):
	"select menu item"
	if menu_item=="inbox":
	    if self.click_element(self.inbox):
                self.write ("Opened the inbox")
	elif menu_item=="sent_mail":
	    if self.click_element(self.sent_mail):
                self.write ("Opened the sent mail folder")
	elif menu_item=="drafts":
	    if self.click_element(self.drafts):
                self.write ("Opened the drafts folder")
	else: 
	    print "cannot find given menu_item" 
			
		

