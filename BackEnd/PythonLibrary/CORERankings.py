#!/usr/bin/python
# Allow Display of elements in HTML

import COREDependencies
import DataCalculation


class Rankings:

    """ Process for looking at each teams statistics and ranking them accordingly
        for further analysis and decision making"""

    def __init__(self):

        """ Creates 2D dictionary: _teams_data
            Key = Team Number; Value = Team's team_data dictionary
                team_data: Key = Report Category; Value = Value or Score """

        self._team_dictionary = {}
        self._team_numbers = []
        self._teams_data = {}
        self._form_data = {}
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
        except Exception as e:
            # Debug Code for Creating Database
            print("Content-type:text/html\r\n\r\n")
            print('<html>')
            print('<head>')
            print('<title>Error Console</title>')
            print('</head>')
            print('<body>')
            print('Oh no, something went wrong with SQL<br>')
            print('Printing error below...<br>')
            print('ERROR SELECTING TABLE NAMES')
            print('<p> ------------ </p>')
            print(e)
            print('</body>')
            print('</html>')
        finally:
            self._db_connection.close()

        for all in self._team_numbers:
            if all == 'None':
                self._team_numbers.remove('None')
        for teams in self._team_numbers:
            self._team_dictionary[teams] = DataCalculation.TeamData(teams)
        for populate in self._team_dictionary:
            self._team_dictionary[populate].populate_data()
        for teams in self._team_numbers:
            self._teams_data[teams] = self._team_dictionary[teams].team_data

    def change_form_names(self, rank_option_name='ranking_type'):

        """ Changes the form names general rank options to user specified

            rank_option_name : name associated with the ranking form radio that contains values of
                all possible reporting options """

        self._rank_option_name = str(rank_option_name)

    def register_rank_option(self, field_value, rank_statistic, rank_order, category_options=None):

        """ Registers form radio options and specifies how they should be ranked.

            field_value : HTML From 'value' that should perform the desired calculation
            rank_statistic : form value of given radio_name that is identical to
                a RANK_HEADER name which is desired to be ranked by
            rank_order : how the data should be ranked. Currently the only supported field options are:
                'descending' - Ranking from best to worst
                'ascending' - Ranks from worst to best
                'category' - Ranks given a tuple (category_options)
            category_options : left as None unless rank_order='category'. It should contain
                a tuple of all possible submission data for the supplied rank_statistic category.
                Intended to be used for ranking based on a priority list of text names. """
        items = ()
        if rank_order == 'category':
            if category_options is None:
                print("No category ranking options supplied by: " + rank_statistic)
            else:
                for item in category_options:
                    items += (item,)
                self._rank_option_data.append((field_value, rank_statistic, rank_order, items))
        else:
            self._rank_option_data.append((field_value, rank_statistic, rank_order))

    def _sort_by_first(self, item):

        """ Internal Function Used with the sorted() function as
            a key to sort using the first value of a tuple. """

        return item[0]

    def _sort_by_second(self, item):

        """ Internal Function Used with the sorted() function as
            a key to sort using the second value of a tuple. """

        return item[1]

    def _rank_ascending(self, RANK_HEADER):

        """  Orders teams from worst to best on given report statistic.

            RANK_HEADER : Constant from REPORT_HEADER to rank by
            return : Ordered tuple of team number, score pairs """

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

        """  Orders teams from best to worst on given report statistic.

            RANK_HEADER : Constant from REPORT_HEADER to rank by
            return : Ordered tuple of team number, score pairs"""

        # Potential optimization after testing
        data_list = []
        score = []
        team_numbers = self._teams_data.keys()
        for team in self._teams_data:
            for category in (self._teams_data[team]):
                if category == RANK_HEADER:
                    score.append(self._teams_data[team][category])
        for (teamNumber, value) in zip(team_numbers, score):
            data_list.append((teamNumber, value),)
        return sorted(data_list, key=self._sort_by_second, reverse=True)

    def _rank_category(self, RANK_HEADER, priorities):

        """ Orders teams from best to worst on a set of name priorities.

            RANK_HEADER : Constant from REPORT_HEADER to rank by.
            priorities : tuple of all possible radio values for the statistic
            that are in order in which they should be displayed.

            return : Ordered tuple of team number, statistic pairs. """

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
        for teamNumber in self._team_numbers:
            for category in self._teams_data[teamNumber]:
                if category == RANK_HEADER:
                    priority_dictionary[self._teams_data[teamNumber][category]].append((teamNumber, self._teams_data[teamNumber][category]))
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

        """ Populates and prompts download of csv file contining rank information.

            rank_list : list containing team number, score tuple pairs.
            category_name : ranking name used for conventions and filename. """

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
            print('<a href = "rankings.csv" download="' + category_name + ' hr.min.sec ' +
                  str('{:%H:%M:%S}'.format(COREDependencies.datetime.datetime.now())) + '">Download</a>')

    def generate_table(self):

        """ Displays table of teams in ranked order based on what the form desires. Also generates and
            downloads a CSV file. Table name is dictated by the name of the desired
            ranking statistic. """

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
                self._download_csv(rank_list, item[1])
        print('</body>')
        print('</html>')

form_data = Rankings()
form_data.change_form_names(COREDependencies.COREConstants.RANK_REPORT_FIELD_NAMES['ranking_options'])
for item in COREDependencies.COREConstants.RANK_OPTIONS:
    if item[2] == 'category':
        form_data.register_rank_option(item[0], item[1], item[2], item[3])
    else:
        form_data.register_rank_option(item[0], item[1], item[2])
form_data.generate_table()