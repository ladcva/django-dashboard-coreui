# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
import pymysql

pymysql.version_info = (2, 0, 3, "final", 0)
pymysql.install_as_MySQLdb()