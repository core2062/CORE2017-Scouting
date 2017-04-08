#!/usr/bin/python
# Allow Display of elements in HTML

""" Simple interface for scout users to select the team/match they are designated
    to scout. Sends match and team data to full scout form as prepopulated data in order to
    prevent match/team number errors that would break the system."""

import COREDependencies

COREDependencies.framework_begining()
cellColorizer = COREDependencies.COREClassColor.ColorTeam()
print('<table width="100%">')
print('<thead>')
print('<tr>')
print('<th rowspan="2" width="20%">Match #</th>')
print('<th colspan="3" width="40%">Blue Alliance</th>')
print('<th colspan="3" width="40%">Red Alliance</th>')
print('</tr>')
print('<tr>')
for i in range(1, 7):
    if i <= 3:
        print('<th> Blue Team #' + str(i) + '</th>')
    else:
        print('<th> Red Team #' + str((i-3)) + '</th>')
print('</tr>')
print('</thead>')
match_num = 1
for match in COREDependencies.COREMatchSchedule.SCHEDULE:
    print('<tr>')
    print('<td>' + str(match_num) + '</td>')
    for team in match:
        if cellColorizer.submit_color(team, match_num)  == None:
            print('<td><a href ="prepopulate.php?team=' + str(team) + '&match=' + str(match_num) +
                  '">' + str(team) + ' </td>')
        else:
            print('<td class ="' + cellColorizer.submit_color(team, match_num) +
                  '">' + str(team) + ' </td>')
    print('</tr>')
    match_num += 1
print('</table>')
print('<form action="prepopulate.php" method="get">')
print('MatchNumber= <input type="number" name="match" required>')
print('TeamNumber= <input type="number" name="team" required>')
print('<input type="submit" value="submit"><br>')
print('</form>')
COREDependencies.framework_end()