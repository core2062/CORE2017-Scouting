#!/usr/bin/python
# Allow Display of elements in HTML

""" Creates an 'advanced' team analysis interface. Displays all calculated report statistics in
    addition to all raw data for the team in the database. Supports providing a picture of the
    team's robot in folder '../RobotPictures'. The picture should be the team number in order
    for the display to recognize it. """

import COREDependencies
import CORETeamData
import DataCalculation

form = COREDependencies.cgi.FieldStorage()
team_number = int(form.getvalue('team_number'))
raw_team_data = CORETeamData.Team(team_number)
calculated_team_data = DataCalculation.TeamData(team_number)
calculated_team_data.populate_data()

print("Content-type:text/html\r\n\r\n")
print('<html class="no-js" lang="en">')
print('<head>')
print('<meta charset="utf-8">')
print('<link rel="shortcut icon" href="favicon.ico" />')
print('<meta name="description" content="CORE 2062 Scouting">')
print('<meta name="author" content="CORE2062">')
print('<meta name="robots" content="noindex, nofollow">')
print('<meta name="theme-color" content="#ff731c" />')
print('<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />')
print('<title>CORE 2062 Scouting | Match Display</title>')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" ' +
      'integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" ' +
      'integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />')
print('<link rel="stylesheet" href="css/app.css">')
print('<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="' +
      'sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>')
print('</head>')
print('<body link="##000000">')
print(str(team_number))
print('<img src="http://2062scouting.imgix.net/' + str(team_number) +
      '.jpg" alt="Team Image Not Available" width="25%" height="25%">')
print('<table>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS:
    print('<td>', dictionary_key, '</td>')
for dictionary_key in COREDependencies.COREConstants.MATCH_HEADERS:
    print('<td>', dictionary_key, '</td>')
for dictionary_key in COREDependencies.COREConstants.RANK_ONLY_HEADERS:
    print('<td>', dictionary_key, '</td>')
print('</tr>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS:
    print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
for dictionary_key in COREDependencies.COREConstants.MATCH_HEADERS:
    print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
for dictionary_key in COREDependencies.COREConstants.RANK_ONLY_HEADERS:
    print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
print('</tr>')
print('</table>')

print('<table>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.ALL_NAMES:
    print('<td>', dictionary_key, '</td>')
print('</tr>')
for rows in range(0, (raw_team_data.num_data_entries(COREDependencies.COREConstants.MATCH_NUMBER['match_number']))):
    print('<tr>')
    for dictionary_key in COREDependencies.COREConstants.ALL_NAMES:
        print('<td>', raw_team_data._category_dictionary[dictionary_key][rows-1], '</td>')
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
