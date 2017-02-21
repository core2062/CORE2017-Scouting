""" Files needed by other files """
import pymysql.cursors
import cgi
import datetime
import csv
import urllib.request
import os
import sys
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__)))) # 1 folder above
sys.path.append(os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))) #2 folders above
import COREConstants
import COREDatabaseCredentials
import COREClassColor
import COREMatchSchedule


