#!/usr/bin/python

# Allow Display of elements in HTML

import pymysql.cursors
import CoreFiles

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Team 2062s Scouting Match Table Report</title>')
print('</head>')

connection = pymysql.connect(host=CoreFiles.DatabaseCredentials.DB_HOST,
                                               user=CoreFiles.DatabaseCredentials.DB_USER,
                                               password=CoreFiles.DatabaseCredentials.DB_PASS,
                                               database=CoreFiles.DatabaseCredentials.DB_NAME,
                                               charset='utf8mb4',
                                               cursorclass=CoreFiles.pymysql.cursors.DictCursor)

"""try:
    with connection.cursor() as cursor:
        test = "INSERT INTO `2062` (`hasAuto`, `defenceType`, `hasDefender`, `numhighgoals`, `numlowgoals`, `comments`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(test, ('nope', 'yes', 'nope', 32, 1, 'gobolyguk'))
    connection.commit()
finally:
    connection.close()
"""
team_number = 1
dictionary = {}

try:
    with connection.cursor() as cursor:
        sql = ("SELECT * FROM `1` ORDER BY `match_id`")
        cursor.execute(sql)
        #all_data = cursor.fetchall()

        id = cursor.fetchone()
        count = 0
        while id is not None:
            keys = id.keys()
            values = id.values()
            if count == 0:
                for (key, value) in zip(keys, values):
                    dictionary[key] = (value,)
                count = 1
            else:
                for (key, value) in zip(keys, values):
                    dictionary[key] += (value,)
            id = cursor.fetchone()
finally:
    connection.close()


for item in dictionary:
    print("<p>" + item + "</p>")
    for thing in dictionary[item]:
        print("<p>" + str(thing) + "</p>")





print('<body>')
print('</body>')
print('</html>')
