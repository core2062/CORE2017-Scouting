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
finally:
    db_connection.close()
for team in team_numbers:
    int_nums.append(int(team))
int_nums.sort()
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
print('<title>CORE 2062 Scouting | Match Display</title>')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" ' +
      'integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" ' +
      'integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="css/app.css">')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="' +
      'sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>')
print('</head>')
print('<body>')
print('<b> Teams: </b>')
print('<table>')
for team in int_nums:
    print('<tr>')
    print('<td><img src="/testdev/BackEnd/RobotPictures/' + str(team) +
          '.jpg" alt="Team Image Not Available" width="25%" height="25%"></td>')
    print('<td><a href="/testdev/BackEnd/PythonLibrary/CORETeamReport.py?team_number=' +
          str(team) + '">' + str(team) + '</a></td>')
    print('</tr>')
print('</table>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="' +
      'sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity=' +
      '"sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>')
print('<script>')
print('$(document).foundation();')
print('</script>')
print('</body>')
print('</html>')