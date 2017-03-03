""" Files needed by other files """
import pymysql.cursors
import cgi
import datetime
import csv
import urllib.request
import os
import sys
# Access to one folder above
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
# Access to two folders above
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))))
import COREConstants
import COREDatabaseCredentials
import COREClassColor
import COREMatchSchedule


