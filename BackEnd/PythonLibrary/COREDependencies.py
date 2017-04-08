""" Files and functions needed by other files """
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


def framework_begining():
    print("Content-type:text/html\r\n\r\n")
    print('<html class="no-js" lang="en">')
    print('<head>')
    print('<meta charset="utf-8">')
    print('<link rel="shortcut icon" href="favicon.ico" />')
    print('<meta name="description" content="CORE 2062 Scouting">')
    print('<meta name="author" content="CORE2062">')
    print('<meta name="robots" content="noindex, nofollow">')
    print('<meta name="theme-color" content="#ff731c" />')
    print('<meta name="viewport" content="width=device-width, initial-scale=1.0, user-scalable=no">')
    print('<title>CORE 2062 Scouting | Team Select</title>')
    print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" ' +
          'integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />')
    print(
        '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" ' +
        'integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />')
    print('<link rel="stylesheet" href="css/app.css">')
    print('<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="' +
          'sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>')
    print('</head>')
    print('<body>')


def framework_end():
    print('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="' +
          'sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>')
    print('<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity=' +
          '"sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>')
    print('<script>')
    print('$(document).foundation();')
    print('</script>')
    print('</body>')
    print('</html>')


