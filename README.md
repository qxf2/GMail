This is sample code to support Qxf2 Service's tutorial on Page Object Model with Selenium and Python.
URL: http://qxf2.com/blog/page-object-model-selenium-python/


---------
1. SETUP
---------
a. Install Python 2.x
b. Install Selenium
c. Add both to your PATH environment variable
d. If you do not have it already, get pip 
e. 'pip install python-dotenv'
f. Update 'login.credentials' with your credentials

-------
2. RUN
-------
a. python Search_Inbox_Test.py
b. For more options: python Search_Inbox_Test.py -h  

-----------
3. ISSUES?
-----------
a. If Python complains about an Import exception, please 'pip install $module_name'
b. If you are not setup with the drivers for the web browsers, you will see a helpful error from Selenium telling you where to go and get them
c. If login fails, its likely that you forgot to update the login.credentials file
d. Exception? 'module object has no attribute load_dotenv'? You have the wrong dotenv module. So first 'pip uninstall dotenv' and then 'pip install python-dotenv'
e. Others: Contact mak@qxf2.com

