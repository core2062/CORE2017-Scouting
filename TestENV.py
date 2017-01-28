#!/usr/bin/python

import pymysql.cursors
import CoreFiles
# Connect to the database
connection = pymysql.connect(host=CoreFiles.DatabaseCredentials.DB_HOST,
                                               user=CoreFiles.DatabaseCredentials.DB_USER,
                                               password=CoreFiles.DatabaseCredentials.DB_PASS,
                                               database=CoreFiles.DatabaseCredentials.DB_NAME,
                                               charset='utf8mb4',
                                               cursorclass=CoreFiles.pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        #sql = "INSERT INTO `users` (`email`, `password`) VALUES (%s, %s)"
        #cursor.execute(sql, ('webmaster@python.org', 'very-secret'))
        test = "INSERT INTO `2062` (`hasAuto`, `defenceType`, `hasDefender`, `numhighgoals`, `numlowgoals`, `comments`) VALUES (%s, %s, %s, %s, %s, %s)"
        cursor.execute(test, ('nope', 'yes', 'nope', 32, 1, 'gobolyguk'))

    # connection is not autocommit by default. So you must commit to save
    # your changes.
    connection.commit()
finally:
    connection.close()