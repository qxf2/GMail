"""
Page object model for the login page
"""
from Page import Page


class Login_Page(Page):
    "Page object for the Login page"

    def start(self):
        self.url = ""
        self.open(self.url) 
        # Assert Title of the Login Page and Login
        self.assertIn("Gmail", self.driver.title)      

        "Xpath of all the field"
        #Login 
        self.login_email = "//input[@name='Email']"
        self.login_next_button = "//input[@id='next']"
        self.login_password = "//input[@placeholder='Password']"
        self.login_signin_button = "//input[@id='signIn']"
    

    def login(self,username,password):
        "Login using credentials provided" 
        login_flag = False
        self.set_login_email(username)
        self.submit_next()
        self.set_login_password(password)
        self.submit_login()
        title = self.driver.title
        if username in title:
            self.write("Login Success",level='debug')
            login_flag = True
        else:
            self.write("FAIL: Login error",level='debug')
            self.write("      Obtained driver title: "+title,level='debug')
            self.write("      Expected the string %s in the title"%username,level='debug')
        
        return login_flag


    def set_login_email(self,username):
        "Set the username on the login screen"
        self.set_text(self.login_email,username)


    def submit_next(self):
        #Weird - GMail sometimes separates the username and password on different steps
        self.click_element(self.login_next_button)
        self.wait(3)
        

    def set_login_password(self,password):
        "Set the password on the login screen"
        self.set_text(self.login_password,password)


    def submit_login(self):
        "Submit the login form"
        self.click_element(self.login_signin_button)
        self.wait(7)
