"""
A simple conf reader.
For now, we just use dotenv and return a key.
In future, you can make this a class and extend get_value()
"""

import dotenv,os


def get_value(conf,key):
    "Return the value in conf for a given key"
    value = None
    try:
        dotenv.load_dotenv(conf)
        value = os.environ[key]
    except Exception,e:
        print 'Exception in get_value'
        print 'file: ',conf
        print 'key: ',key

    return value


