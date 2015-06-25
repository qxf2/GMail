"""
Test case for login and search 
"""
import dotenv,os,sys,PageFactory,Test_Rail,Conf_Reader
from optparse import OptionParser
from DriverFactory import DriverFactory


def check_options(options):
    "Check if the command line options are valid"
    options_flag = True
    options.config_file = os.path.abspath(options.config_file)

    #Check if the config file exists and is a file
    if os.path.exists(options.config_file):
        if not os.path.isfile(options.config_file):
            print '\n****'
            print 'Config file provided is not a file: '
            print options.config_file
            print '****'
            options_flag = False
    else:
        print '\n****'
        print 'Unable to locate the provided config file: '
        print options.config_file
        print '****'
        options_flag = False

    return options_flag


def run_search_inbox_test(browser,conf,base_url,sauce_flag,browser_version,platform,testrail_run_id):
    "Login to Gmail using the page object model"
    # get the test account credentials from the .credentials file
    credentials_file = os.path.join(os.path.dirname(__file__),'login.credentials')
    username = Conf_Reader.get_value(credentials_file,'LOGIN_USER')
    password = Conf_Reader.get_value(credentials_file,'LOGIN_PASSWORD')

    #Result flag used by TestRail
    result_flag = False
    
    #Setup a driver
    #create object of driver factory
    driver_obj = DriverFactory()
    driver = driver_obj.get_web_driver(browser,sauce_flag,browser_version,platform)
    driver.maximize_window()
    

    #Create a login page object
    login_obj = PageFactory.get_page_object("login",driver)
    if (login_obj.login(username,password)):
        msg = "Login was successful"
        result_flag = True
        login_obj.write(msg)
    else:
        msg = "Login failed"
        login_obj.write(msg)
        
    #Create an object for main page with header and menu
    main_obj = PageFactory.get_page_object("main",driver)
    main_obj.wait(3)
    
    #Search the inbox for message by subject 'POM' and open the message
    if main_obj.header_obj.search_by_subject('POM'):
        main_obj.write("Search successful")
        result_flag = True
    else:
        main_obj.write("Search text was not found")
        result_flag = False
        
    #Go to inbox
    main_obj.menu_obj.select_menu_item('inbox')

    #Update TestRail
    if testrail_run_id is not None:
        login_obj.write('About to update TestRail')
        case_id = 67
        Test_Rail.update_testrail(case_id,testrail_run_id,result_flag,msg=msg)

    main_obj.teardown()

    
#---START OF SCRIPT
if __name__=='__main__':
    #Accept command line parameters
    usage = "\n----\n%prog -b <OPTIONAL: Browser> -c <OPTIONAL: configuration_file> -u <OPTIONAL: APP URL> -v <OPTIONAL: Browser version> -p <OPTIONAL: Platform> -s <OPTIONAL: sauce lab flag>\n----\nE.g.:%prog -b FF -c .conf -u https://basecamp.com -s Y -v 26 -p \"Windows 8\"\n---"
    parser = OptionParser(usage=usage)

    parser.add_option("-b","--browser",
                      dest="browser",
                      default="firefox",
                      help="Browser. Valid options are firefox, ie and chrome")                      
    parser.add_option("-c","--config",
                      dest="config_file",
                      default=os.path.join(os.path.dirname(__file__),'data.conf'),
                      help="The full or relative path of the test configuration file")
    parser.add_option("-u","--app_url",
                      dest="url",
                      default="https://gmail.com",
                      help="The url of the application")
    parser.add_option("-s","--sauce_flag",
                      dest="sauce_flag",
                      default="N",
                      help="Run the test in Sauce labs: Y or N")
    parser.add_option("-v","--version",
                      dest="browser_version",
                      help="The version of the browser: a whole number",
                      default=None)
    parser.add_option("-p","--platform",
                      dest="platform",
                      help="The operating system: Windows 7, Linux",
                      default="Windows 7")
    parser.add_option("-r","--test_run_id",
                      dest="testrail_run_id",
                      default=None,
                      help="The test run id in TestRail")
                      
    (options,args) = parser.parse_args()

    if check_options(options): 
        #Run the test only if the options provided are valid
        run_search_inbox_test(browser=options.browser,conf=os.path.abspath(options.config_file),base_url=options.url,sauce_flag=options.sauce_flag,browser_version=options.browser_version,platform=options.platform,testrail_run_id=options.testrail_run_id)
    else:
        print 'ERROR: Received incorrect input arguments'
        print parser.print_usage()
