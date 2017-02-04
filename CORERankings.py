#!/usr/bin/python
# Allow Display of elements in HTML

import DataCalculation
import CoreFiles
import csv

class Rankings:

    """ Process for looking at each teams statistics and ranking them accordingly
        for further analysis """

    def __init__(self):

        """ Creates 2D dictionary: _teams_data
            Key = Team Number; Value = Team's team_data dictionary
                team_data: Key = Report Category; Value = Value or Score """

        self._team_dictionary = {}
        self._team_numbers = []
        self._teams_data = {}

        self._db_connection = CoreFiles.pymysql.connect(host=CoreFiles.DatabaseCredentials.DB_HOST,
                                                        user=CoreFiles.DatabaseCredentials.DB_USER,
                                                        password=CoreFiles.DatabaseCredentials.DB_PASS,
                                                        db=CoreFiles.DatabaseCredentials.DB_NAME,
                                                        charset='utf8mb4',
                                                        cursorclass=CoreFiles.pymysql.cursors.DictCursor)
        try:
            with self._db_connection.cursor() as cursor:
                cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='example'")
                id = cursor.fetchone()
                while id is not None:
                    self._team_numbers.append(id['TABLE_NAME'])
                    id = cursor.fetchone()
        finally:
            self._db_connection.close()

        for teams in self._team_numbers:
            self._team_dictionary[teams] = DataCalculation.TeamData(teams)
        for populate in self._team_dictionary:
            self._team_dictionary[populate].populate_data()
        for teams in self._team_numbers:
            self._teams_data[teams] = self._team_dictionary[teams].team_data

    def _sort_by_second(self, item):

        """ Internal Function Used with the sorted() function as
            a key to sort using the second value of a tuple """

        return item[1]

    def _sort_by_first(self, item):

        """ Internal Function Used with the sorted() function as
            a key to sort using the first value of a tuple """

        return item[0]

    def rank_ascending(self, RANK_HEADER):

        """  Orders teams from worst to best on given report statistic
            - Pass Constant from REPORT_HEADER to rank by
            - Returns Ordered list of team numbers """

        # Potential optimization after testing
        data_list = []
        score = []
        sorted_teams = []
        for team in self._teams_data:
            for category in (self._teams_data[team]):
                if category == RANK_HEADER:
                    score.append(self._teams_data[team][category])
        for (teamNumber, value) in zip(self._team_numbers, score):
            data_list.append((teamNumber, value),)
        return sorted(data_list, key=self._sort_by_second)
        """sorted_data_list = sorted(data_list, key=self._sort_by_second)
        for item in sorted_data_list:
            sorted_teams.append(item[0])
        return sorted_teams"""

    def rank_descending(self, RANK_HEADER):

        """  Orders teams from best to worst on given report statistic
            - Pass Constant from REPORT_HEADER to rank by
            - Returns Ordered list of team numbers """

        # Potential optimization after testing
        data_list = []
        score = []
        sorted_teams = []
        for team in self._teams_data:
            for category in (self._teams_data[team]):
                if category == RANK_HEADER:
                    score.append(self._teams_data[team][category])
        for (teamNumber, value) in zip(self._team_numbers, score):
            data_list.append((teamNumber, value),)
        return sorted(data_list, key=self._sort_by_second, reverse=True)
        """sorted_data_list = sorted(data_list, key=self._sort_by_second, reverse=True)
        for item in sorted_data_list:
            sorted_teams.append(item[0])
        return sorted_teams"""

    def display_ranks(self, rank_list, category_name):

        """ Displays table of teams in ranked order
            - rank_list = generated list of tuples that contains;
                [0] Team Number
                [1] Score
            - category_name = Report statistic the table was generated from
            (nondependent and used for naming and table readability)"""

        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<title>Team 2062s Scouting Match Table Report</title>')
        print('</head>')
        print('<link href="style.css" rel="stylesheet" type="text/css" />')
        print('<table>')
        print('<tr>')
        # Set's up first row
        print('<td> CORE ' + category_name + ' RANKINGS </td>')
        print('<td>' + '{:%b-%d %H:%M:%S}'.format(CoreFiles.datetime.datetime.now()) + '</td>')
        print('</tr>')
        count = 1
        for team in rank_list:
            print('<tr>')
            print('<td>' + str(count) + '. ' + str(team[0]) + '</td>')
            print('<td>' + str(team[1]) + '</td>')
            print('</tr>')
            count += 1
        print('</table>')
        print('<body>')
        print('</body>')
        print('</html>')

    def check_CSV(self, rank_list):
        # noah
        with open('rankings.csv', 'wb') as csvfile:
            fieldnames = ['Team_number','Score']
            writer = csv.writer(csvfile, delimiter=',', fieldnames=fieldnames, lineterminator='\n')
            writer.writeheader()
        for team in rank_list:
            writer.writerow({'Team_number': team[0], 'Score': team[1]})
print("Content-type:text/html\r\n\r\n")
print('<html>')
print('<head>')
print('<title>Team 2062s Scouting Match Table Report</title>')
print('</head>')

ranking = Rankings()
ranking.display_ranks(ranking.rank_ascending(CoreFiles.Constants.REPORT_HEADER[1]), 'High Goals')

print('<body>')
print('</body>')
print('</html>')