import DataCalculation
import CoreFiles


class MatchReport:

    def __init__(self):

        """ Setup Dictionaries for display """

        self._form = CoreFiles.cgi.FieldStorage()
        self._team_dictionary = {}

        for teams in CoreFiles.Constants.TEAM_NUMBER_FIELDS:
            # Populates _team_dictionary with : key = alliance color, value = team object
            self._team_dictionary[teams] = DataCalculation.TeamData(self._form.getvalue(teams))
        for populate in self._team_dictionary:
            populate.populatedata()

        self._alliance_keys = list(self._team_dictionary.keys())
        # Populates _data_keys with all of the report statistic categories accessed from one of the team objects
        self._data_keys = self._team_dictionary[self._alliance_keys[1]].team_data.keys()

    def generate_table(self):

        """ Iterates through each team objects internal dictionary that contains values for each report statistic """

        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<title>Team 2062s Scouting Match Table Report</title>')
        print('</head>')
        print('<table>')
        print('<tr>')
        # Set's up top left corner piece
        print('<td> CORE MATCH REPORT <td/>')
        for keys in self._alliance_keys:
            # Set's up the column headers for the table
            print('<td>', keys, '<td/>')
        print('</tr>')
        for dictionary_key in self._data_keys:
            print('<tr>')
            # Set's up the number of rows
            # Populates the first item in the row with the row header
            print('<td>', dictionary_key, '</td>')
            for key in self._team_dictionary:
                # Fills the rest of the row with data from each of the team
                print('<td>', self._team_dictionary[key].team_data[dictionary_key], '<td/>')
            print('</tr>')
        print('</table>')
        print('</body>')
        print('</html>')

table = MatchReport()
table.generate_table()
