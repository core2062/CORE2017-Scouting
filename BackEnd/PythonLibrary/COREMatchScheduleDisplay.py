#!/usr/bin/python
# Allow Display of elements in HTML

""" Creates a simple user interface for the user to generate match reports based on the
    COREMatchSchedule for upcoming or past matches. """

import COREDependencies

COREDependencies.framework_begining()
print('<body link="##000000">')

cellColorizer = COREDependencies.COREClassColor.ColorTeam()
print('<table width="100%">')
print('<thead>')
print('<tr>')
print('<th rowspan="2" width="20%">Match #</th>')
print('<th colspan="3" width="40%">Red Alliance</th>')
print('<th colspan="3" width="40%">Blue Alliance</th>')
print('</tr>')
print('<tr>')
for i in range(1, 7):
    if i <= 3:
        print('<th> Red Team #' + str(i) + '</th>')
    else:
        print('<th> Blue Team #' + str((i-3)) + '</th>')
print('</tr>')
print('</thead>')
match_num = 1
for match in COREDependencies.COREMatchSchedule.SCHEDULE:
    print('<tr>')
    print('<td class ="' + cellColorizer.header_color(match_num, match) +
          '"><a href="COREMatchReport.py?RedTeam1=' + str(match[0]) +
          '&RedTeam2=' + str(match[1]) + '&RedTeam3=' + str(match[2]) +
          '&BlueTeam1=' + str(match[3]) + '&BlueTeam2=' + str(match[4]) +
          '&BlueTeam3=' + str(match[5]) + '&MatchNumber=' + str(match_num) +
          '">' + str(match_num) + '</td>')
    for team in match:
        print('<td class ="' + cellColorizer.find_color(team, match_num) + '"> ' + str(team) + ' </td>')
    print('</tr>')
    match_num += 1
print('</table>')
# brett make this better plz, ty m8
print('<form action="COREMatchReport.py" method="post">')
print('MatchNumber= <input type="number" name="MatchNumber" required>')
print('RedTeam1= <input type="number" name="RedTeam1" required>')
print('RedTeam2= <input type="number" name="RedTeam2" required>')
print('RedTeam3= <input type="number" name="RedTeam3" required>')
print('BlueTeam1= <input type="number" name="BlueTeam1" required>')
print('BlueTeam2= <input type="number" name="BlueTeam2" required>')
print('BlueTeam3= <input type="number" name="BlueTeam3" required>')
print('<input type="submit" value="submit"><br>')
print('</form>')
COREDependencies.framework_end()