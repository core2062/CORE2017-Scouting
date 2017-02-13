#!/usr/bin/python
# Allow Display of elements in HTML

import COREMatchSchedule
import COREDependencies


class ColorTeam:

    """ Determines the label color for each team cell in order for the user to better understand what data
        is submitted and when to generate reports """

    def __init__(self):

        """ Connects to database and populates dictionaries and arrays with team and match data """

        self._schedule = COREMatchSchedule.SCHEDULE
        self._teams_in_db = []
        self._team_matches_in_db = {}

        self._db_connection = COREDependencies.pymysql.connect(host=COREDependencies.COREDatabaseCredentials.DB_HOST,
                                                               user=COREDependencies.COREDatabaseCredentials.DB_USER,
                                                               password=COREDependencies.COREDatabaseCredentials.DB_PASS,
                                                               db=COREDependencies.COREDatabaseCredentials.DB_NAME,
                                                               charset='utf8mb4',
                                                               cursorclass=COREDependencies.pymysql.cursors.DictCursor)

        try:
            with self._db_connection.cursor() as cursor:
                cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE" +
                               " TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='example'")
                table_name = cursor.fetchone()
                while table_name is not None:
                    self._teams_in_db.append(table_name['TABLE_NAME'])
                    table_name = cursor.fetchone()

                for team in self._teams_in_db:
                    count = 0
                    cursor.execute(("SELECT " + COREDependencies.COREConstants.MATCH_NUMBER['match_number'] +
                                    " FROM `" + str(team) + "` ORDER BY `match_id`"))
                    matches = cursor.fetchone()

                    while matches is not None:
                        values = matches.values()
                        if count == 0:
                            for value in values:
                                self._team_matches_in_db[team] = (value,)
                            count = 1
                        else:
                            for value in values:
                                self._team_matches_in_db[team] += (value,)
                        matches = cursor.fetchone()
                    # Goal is to create dictionary with key team number and value: tuple of all match submitions
        finally:
            self._db_connection.close()

    def _find_team_from_schedule(self, team_number):

        """ Searches the match schedule for all instances where the desired team_number is present
            - team_number: team that is to be searched for
            - returns: list of all match numbers where team_number exists """

        match_num = 1
        instances = []
        for match in COREDependencies.COREMatchSchedule.SCHEDULE:
            for team in match:
                if team == team_number:
                    instances.append(match_num)
            match_num += 1
        return instances

    def _find_highest_match(self):

        """ Finds the most recent match number submitted
            - returns: int """
        highest = 1
        for team in self._team_matches_in_db:
            for match in self._team_matches_in_db[team]:
                if match > highest:
                    highest = match
        return highest

    def find_color(self, team_number, match_number):

        """
        Grey - Not Submited post match
        Blue - Submited data
        Green - Ready to Generate Report
        Red - Not Ready to Generate Report
        """
        validate = False
        exists = False
        team_matches = self._find_team_from_schedule(team_number)

        """Validate Existance"""
        for match in team_matches:
            if match == match_number:
                # -- makes sure team exists in schedule
                validate = True
        if validate == False:
            # -- print some error or something that team is not in schedule placeholder error 'color'
            return 'error'

        """Blue"""
        for team in self._team_matches_in_db:
            if team == team_number:
                # -- finds team in db
                exists = True
                for matches in self._team_matches_in_db[team]:
                    if matches == match_number:
                        return 'blue'
                    # -- if match submitted in db is same as match num make blue

        """Grey"""
        if exists is True:
            if self._find_highest_match() >= match_number:
                return 'grey'
        # -- if team is in db and the match concerned with is lower than latest match submitted, turn grey

        """Green / Red"""
        if exists is False:
            if match_number == team_matches[0]:
                return 'green'
            else:
                return 'red'
            # -- if it doesnt exist but should exist make red, otherwise if it doesnt exist but it's first instance make green

        # -- Post matches in db (when to generate)

        if exists is True and match_number > self._find_highest_match():
            matches_in_db = self._find_team_from_schedule(team_number)
            highest_in_db = 1
            for match in matches_in_db:
                if match > highest_in_db:
                    highest_in_db = match
            count = 0
            for match in team_matches:
                count += 1
                if match == highest_in_db:
                    break
            if match_number == team_matches[count]:
                return 'green'
            # -- if no other color, red
        return 'red'

cellColorizer = ColorTeam()


print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Team 2062s Scouting Match Table Report</title>')
print('</head>')
print('<body>')
print('<link href="COREStyle_matchselect.css" rel="stylesheet" type="text/css" />')

print('<table>')
print('<tr>')
print('<td> CORE MATCH SCHEDULE </td>')
for i in range(1, 7):
    if i <= 3:
        print('<td> RED' + str(i) + '</td>')
    else:
        print('<td> RED' + str((i-3)) + '</td>')
print('</tr>')
match_num = 1
for match in COREDependencies.COREMatchSchedule.SCHEDULE:
    print('<tr>')
    print('<td><a href="COREMatchReport.py?RedTeam1=' + str(match[0]) +
          '&RedTeam2=' + str(match[1]) + '&RedTeam3=' + str(match[2]) +
          '&BlueTeam1=' + str(match[3]) + '&BlueTeam2=' + str(match[4]) +
          '&BlueTeam3=' + str(match[5]) + '&MatchNumber=' + str(match_num) +
          '">' + str(match_num) + '</td>')
    for team in match:
        print('<td class ="' + cellColorizer.find_color(team, match) + '"> ' + str(team) + ' </td>')
    print('</tr>')
    match_num += 1
print('</table>')
print('</body>')
print('</html>')
