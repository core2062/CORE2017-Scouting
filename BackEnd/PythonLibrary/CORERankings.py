#!/usr/bin/python
# Allow Display of elements in HTML

import COREDependencies
import DataCalculation


class _MyHTTPRedirectHandler(COREDependencies.urllib.request.HTTPRedirectHandler):
    def http_error_302(self, req, fp, code, msg, headers):
        print('Follow redirect...')
        return COREDependencies.urllib.request.HTTPRedirectHandler.http_error_302(self, req, fp, code, msg, headers)

    http_error_301 = http_error_303 = http_error_307 = http_error_302


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
        self._form_data = {}
        self._csv_name = 'CSV'
        self._rank_option_name = 'ranking_type'
        self._form = COREDependencies.cgi.FieldStorage()
        self._rank_option_data = []

        self._db_connection = COREDependencies.pymysql.connect(host=COREDependencies.COREDatabaseCredentials.DB_HOST,
                                                               user=COREDependencies.COREDatabaseCredentials.DB_USER,
                                                               password=COREDependencies.COREDatabaseCredentials.DB_PASS,
                                                               db=COREDependencies.COREConstants.COMPETITION_NAME,
                                                               charset='utf8mb4',
                                                               cursorclass=COREDependencies.pymysql.cursors.DictCursor)

        try:
            with self._db_connection.cursor() as cursor:
                cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='" +
                               str(COREDependencies.COREConstants.COMPETITION_NAME) + "'")
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

    def change_form_names(self, csv_name='CSV', rank_option_name='ranking_type'):

        """ Changes the form names for CSV and general rank options to user specified
            - csv_name: name associated with the form checkbox value that is intended to download
            a CSV file containing the ranking report in addition to visually displaying the table
            - rank_option_name: name associated with the ranking form radio that contains values of
            all possible reporting options """

        self._csv_name = str(csv_name)
        self._rank_option_name = str(rank_option_name)

    def register_rank_option(self, field_value, rank_statistic, rank_order='descending', category_options=None):

        """ Registers form radio options and specifies how they should be ranked.
            - rank_statistic = form value of given radio_name that is identical to
            a RANK_HEADER name which is desired to be ranked by
            - rank_order = how the data should be ranked. Currently the only supported field options are:
                'descending' - Ranking from best to worst
                'ascending' - Ranks from worst to best
                'category' - Ranks given a tuple (category_options) of all possible submission data
                for the supplied rank_statistic category. Intended to be used for ranking based on a
                priority of strings. """

        if rank_order == 'category':
            if category_options is None:
                print("No category ranking options supplied by: " + rank_statistic)
            else:
                self._rank_option_data.append((field_value, rank_statistic, rank_order, category_options))
        else:
            self._rank_option_data.append((field_value, rank_statistic, rank_order))

    def _sort_by_first(self, item):

        """ Internal Function Used with the sorted() function as
            a key to sort using the first value of a tuple """

        return item[0]

    def _sort_by_second(self, item):

        """ Internal Function Used with the sorted() function as
            a key to sort using the second value of a tuple """

        return item[1]

    def _rank_ascending(self, RANK_HEADER):

        """  Orders teams from worst to best on given report statistic
            - Pass Constant from REPORT_HEADER to rank by
            - Returns Ordered tuple of team number, score pairs """

        # Potential optimization after testing
        data_list = []
        score = []
        for team in self._teams_data:
            for category in (self._teams_data[team]):
                if category == RANK_HEADER:
                    score.append(self._teams_data[team][category])
        for (teamNumber, value) in zip(self._team_numbers, score):
            data_list.append((teamNumber, value),)
        return sorted(data_list, key=self._sort_by_second)

    def _rank_descending(self, RANK_HEADER):

        """  Orders teams from best to worst on given report statistic
            - Pass Constant from REPORT_HEADER to rank by
            - Returns Ordered tuple of team number, score pairs"""

        # Potential optimization after testing
        data_list = []
        score = []
        for team in self._teams_data:
            for category in (self._teams_data[team]):
                if category == RANK_HEADER:
                    score.append(self._teams_data[team][category])
        for (teamNumber, value) in zip(self._team_numbers, score):
            data_list.append((teamNumber, value),)
        return sorted(data_list, key=self._sort_by_second, reverse=True)

    def _rank_category(self, RANK_HEADER, priorities):

        """ Orders teams from best to worst on a set of name priorities
            - priorities = tuple of all possible radio values for the statistic
            that are in order in which they should be displayed
            - Pass Constant from REPORT_HEADER to rank by
            - Returns Ordered tuple of team number, statistic pairs"""

        # dictionary of list of tuples, yay :D
        data_list = []
        score = []
        priority_dictionary = {}
        sort_list = []
        for item in priorities:
            priority_dictionary[item] = []
        for team in self._teams_data:
            for category in (self._teams_data[team]):
                if category == RANK_HEADER:
                    score.append(self._teams_data[team][category])
        for (teamNumber, value) in zip(self._team_numbers, score):
            priority_dictionary[score] = ((teamNumber, value),)
        for team in data_list:
            for item in priority_dictionary:
                if team[1] == priority_dictionary[item]:
                    priority_dictionary[item].append(team,)
        for order in priorities:
            for category in priority_dictionary:
                if order == category:
                    for team in priority_dictionary[category]:
                        sort_list.append(team,)
        return sort_list

    def _download_csv(self, rank_list, category_name):

        """
            - Needs to be finished
            x - create file if not exist
        """

        with open('rankings.csv', 'w', newline='\r\n') as file:
            field = ['Team_number', 'Score']
            csv_write = COREDependencies.csv.DictWriter(file, fieldnames=field)
            header = {'Team_number': category_name,
                      'Score': str('{:%b-%d %H:%M:%S}'.format(COREDependencies.datetime.datetime.now()))}
            csv_write.writerow(header)
            for team in rank_list:
                dict = {'Team_number': team[0], 'Score': team[1]}
                csv_write.writerow(dict)
            file.close()
        """site = COREDependencies.urllib.request.urlopen(
            "http://scouting.core2062.com/testdev/BackEnd/PythonLibrary/rankings.csv")
        site.retrieve("http://scouting.core2062.com/testdev/BackEnd/PythonLibrary/rankings.csv", "rankings.csv")
        with open('rankings.csv', "w", newline='') as f:
            writer = COREDependencies.csv.writer(f)
            writer.writerows(f)"""

    def generate_table(self):

        """ Displays table of teams in ranked order based on what the form desires. Also generates and
            downloads a CSV file if specified.
            - Table name is dictated by the name of the desired ranking statistic"""

        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<title>Team 2062s Scouting Match Table Report</title>')
        print('</head>')
        print('<body>')
        print('<link href="COREStyle_std.css" rel="stylesheet" type="text/css" />')
        for item in self._rank_option_data:
            if self._form.getvalue(self._rank_option_name) == item[0]:
                if item[2] == 'ascending':
                    rank_list = self._rank_ascending(item[1])
                elif item[2] == 'descending':
                    rank_list = self._rank_descending(item[1])
                elif item[2] == 'category':
                    rank_list = self._rank_category(item[1], item[3])
                else:
                    rank_list = 0
                    print("Invalid Ranking Method!")
                print('<table>')
                print('<tr>')
                print('<td> CORE ' + item[1] + ' RANKINGS </td>')
                print('<td>' + '{:%b-%d %H:%M:%S}'.format(COREDependencies.datetime.datetime.now()) + '</td>')
                print('</tr>')
                count = 1
                for team in rank_list:
                    print('<tr>')
                    print('<td>' + str(count) + '. ' + str(team[0]) + '</td>')
                    print('<td>' + str(team[1]) + '</td>')
                    print('</tr>')
                    count += 1
                print('</table>')
                if self._form.getvalue(self._csv_name) == 'Yes':
                    self._download_csv(rank_list, item[1])
            else:
                print('No ranking data for given category')
        print('</body>')
        print('</html>')

form_data = Rankings()
#form_data.change_form_names(COREDependencies.COREConstants.RANK_REPORT_FIELD_NAMES['CSV'],
#                            COREDependencies.COREConstants.RANK_REPORT_FIELD_NAMES['ranking_options'])
for item in COREDependencies.COREConstants.RANK_OPTIONS:
    if item[1] == 'category':
        form_data.register_rank_option(item[0], item[1], item[2])
    else:
        form_data.register_rank_option(item[0],  item[1])
form_data.generate_table()