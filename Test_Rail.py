"""
TestRail integration
"""

import dotenv,os,testrail,Conf_Reader


def get_testrail_conf():
    "Get the testrail account credentials from the testrail.env file"
    testrail_file = os.path.join(os.path.dirname(__file__),'testrail.env')
    #TestRail Url
    testrail_url = Conf_Reader.get_value(testrail_file,'TESTRAIL_URL')
    client = testrail.APIClient(testrail_url)
    #TestRail User and Password
    client.user = Conf_Reader.get_value(testrail_file,'TESTRAIL_USER')
    client.password = Conf_Reader.get_value(testrail_file,'TESTRAIL_PASSWORD')

    return client


def update_testrail(case_id,run_id,result_flag,msg=""):
    "Update TestRail for a given run_id and case_id"
    update_flag = False
    #Get the TestRail client account details
    client = get_testrail_conf()

    #Update the result in TestRail using send_post function. 
    #Parameters for add_result_for_case is the combination of runid and case id. 
    #status_id is 1 for Passed, 2 For Blocked, 4 for Retest and 5 for Failed
    status_id = 1 if result_flag is True else 5

    if run_id is not None:
        try:
            result = client.send_post(
                'add_result_for_case/%s/%s'%(run_id,case_id),
                {'status_id': status_id, 'comment': msg })
        except Exception,e:
            print 'Exception in update_testrail() updating TestRail.'
            print 'PYTHON SAYS: '
            print e
        else:
            print 'Updated test result for case: %s in test run: %s with msg:%s'%(case_id,run_id,msg)
        
    return update_flag
