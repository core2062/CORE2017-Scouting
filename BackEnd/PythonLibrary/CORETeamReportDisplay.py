#!/usr/bin/python
# Allow Display of elements in HTML

""" Creates a simple user interface for the user to select teams to generate an advanced
    report based on the teams available in the database. Supports providing a picture of the
    team's robot in folder '../RobotPictures'. The picture should be the team number in order
    for the display to recognize it. """

import COREDependencies

team_numbers = []
int_nums = []
db_connection = COREDependencies.pymysql.connect(host=COREDependencies.COREDatabaseCredentials.DB_HOST,
                                                 user=COREDependencies.COREDatabaseCredentials.DB_USER,
                                                 password=COREDependencies.COREDatabaseCredentials.DB_PASS,
                                                 db=COREDependencies.COREConstants.COMPETITION_NAME,
                                                 charset='utf8mb4',
                                                 cursorclass=COREDependencies.pymysql.cursors.DictCursor)
try:
    with db_connection.cursor() as cursor:
        cursor.execute(
            "SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" +
            str(COREDependencies.COREConstants.COMPETITION_NAME) + "'")
        id = cursor.fetchone()
        while id is not None:
            team_numbers.append(id['TABLE_NAME'])
            id = cursor.fetchone()
except Exception as e:
    # Debug Code for Creating Database
    print("Content-type:text/html\r\n\r\n")
    print('<html>')
    print('<head>')
    print('<title>Error Console</title>')
    print('</head>')
    print('<body>')
    print('Oh no, something went wrong with SQL<br>')
    print('Printing statement below...<br>')
    print('ERROR SELECTING TABLE NAMES')
    print('<p> ------------ </p>')
    print(e)
    print('</body>')
    print('</html>')
finally:
    db_connection.close()

for team in team_numbers:
    if team != 'None':
        int_nums.append(int(team))
int_nums.sort()
COREDependencies.framework_begining()
print('<b> Teams: </b>')
print('<table>')
for team in int_nums:
    print('<tr>')
    print('<td><img src="http://2062scouting.imgix.net/' + str(team) +
          '.jpg?h=200" alt="Team Image Not Available"></td>')
    print('<td><a href="CORETeamReport.py?team_number=' +
          str(team) + '">' + str(team) + '</a></td>')
    print('</tr>')
print('</table>')
COREDependencies.framework_end()