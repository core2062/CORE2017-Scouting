#!/usr/bin/python
# Allow Display of elements in HTML

import COREDependencies
import CORETeamData
import DataCalculation

form = COREDependencies.cgi.FieldStorage()
team_number = int(form.getvalue('team_number'))
raw_team_data = CORETeamData.Team(team_number)
calculated_team_data = DataCalculation.TeamData(team_number)
calculated_team_data.populatedata()

print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title> Team Analysis Page</title>')
print('</head>')
print('<body>')
print('<img src="/testdev/BackEnd/RobotPictures/' + str(team_number) +
      '.jpg" alt="Team Image Not Available" width="25%" height="25%">')

print('<table>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.REPORT_HEADER:
    print('<td>', dictionary_key, '</td>')
print('</tr>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.REPORT_HEADER:
    print('<td>' + str(calculated_team_data.team_data[dictionary_key]) + '</td>')
print('</tr>')
print('</table>')

print('<table>')
print('<tr>')
for dictionary_key in COREDependencies.COREConstants.ALL_NAMES:
    print('<td>', dictionary_key, '</td>')
print('</tr>')
for rows in range(1, len(raw_team_data._get_data('match_id'))):
    print('<tr>')
    for dictionary_key in COREDependencies.COREConstants.ALL_NAMES:
        print(raw_team_data._category_dictionary[dictionary_key][rows-1])
    print('</tr>')
print('</table>')

print('</body>')
print('</html>')
