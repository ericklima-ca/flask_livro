# -*- coding: utf-8 -*-
# python 3.9.6

import sys
from importlib import reload


from app import create_app
from config import app_config, app_active

config = app_config[app_active]
config.APP = create_app(app_active)

if __name__ == '__main__':
    config.APP.run(host = config.IP_HOST, port = config.PORT)
    reload(sys)