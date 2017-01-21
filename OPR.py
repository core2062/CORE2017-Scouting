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

        self.db_connection = CoreFiles.pymysql.connect(host=CoreFiles.DatabaseCredentials.DB_HOST,
                                                       user=CoreFiles.DatabaseCredentials.DB_USER,
                                                       password=CoreFiles.DatabaseCredentials.DB_PASS,
                                                       db=CoreFiles.DatabaseCredentials.DB_NAME,
                                                       charset='utf8mb4',
                                                       cursorclass=CoreFiles.pymysql.cursors.DictCursor)
        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute("SELECT table_name FROM all_tables")
                self._team_numbers = cursor.fetchall()
        finally:
            self.db_connection.close()

        for teams in self._team_numbers:
            self._team_dictionary[teams] = DataCalculation.TeamData(teams)
        for populate in self._team_dictionary:
            populate.populatedata()
        for teams in self._team_numbers:
            self._teams_data[teams] = self._team_dictionary[teams].team_data

    def rank_ascending(self):

        """ Creates dictionary that orders teams from worst to best on given report statistic
            - Pass Constant from REPORT_HEADER to rank by """
        # stuff

    def rank_decdending(self):

        """ Creates dictionary that orders teams from best to worst on given report statistic
            - Pass Constant from REPORT_HEADER to rank by """
        # stuff
