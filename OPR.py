import DataCalculation
import CoreFiles


class CoreRankings:

    """ Process for looking at each teams statistics and ranking them accordingly
        for further analysis """

    def __init__(self):

        """ Creates 2D dictionary: _teams_data
            Key = Team Number; Value = Team's team_data dictionary
                team_data: Key = Report Category; Value = Value / Score """

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
                # Potential Problem SQL, Needs Testing
                # _team_numbers needs to be in list format!
                cursor.execute("SELECT table_name FROM all_tables")
                self._team_numbers = cursor.fetchall()
        finally:
            self._db_connection.close()

        for teams in self._team_numbers:
            self._team_dictionary[teams] = DataCalculation.TeamData(teams)
        for populate in self._team_dictionary:
            populate.populatedata()
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
            score.append(team[RANK_HEADER])
        for (teamNumber, value) in zip(self._team_numbers, score):
            data_list.append((teamNumber, value),)
        sorted_data_list = sorted(data_list, key=self._sort_by_second)
        for item in sorted_data_list:
            sorted_teams.append(item[0])
        return sorted_teams

    def rank_decdending(self, RANK_HEADER):

        """  Orders teams from best to worst on given report statistic
            - Pass Constant from REPORT_HEADER to rank by
            - Returns Ordered list of team numbers """

        # Potential optimization after testing
        data_list = []
        score = []
        sorted_teams = []
        for team in self._teams_data:
            score.append(team[RANK_HEADER])
        for (teamNumber, value) in zip(self._team_numbers, score):
            data_list.append((teamNumber, value), )
        sorted_data_list = sorted(data_list, key=self._sort_by_second, reverse=True)
        for item in sorted_data_list:
            sorted_teams.append(item[0])
        return sorted_teams
