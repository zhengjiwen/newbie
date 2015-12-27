#_*_coding:utf-8_*_
__author__ = 'Alex Li'

import os

BASE_DIR  = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


BIND_HOST = '127.0.0.1'
BIND_PORT = 1212

USER_HOME = '%s/var/users' %BASE_DIR
USER_ACCOUNT = {
    'alex':{'password':'alex123',
            'quotation': 209710000, #1GB
            'expire': '2016-01-22'
            },
    'rain':{'password':'rain123',
        'quotation': 2000000, #2GB
        'expire': '2016-01-22'
        },
}
