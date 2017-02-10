#!/usr/bin/python
# Allow Display of elements in HTML

import DataCalculation
import COREDependencies


class MatchReport:

    """ Creates a CORE match report, displayed as a table to be printed and given to drive team.
        Needs external form to supply match teams to display. Form key names are supplied in
        CoreFile.Constants.TEAM_NUMBER_FIELDS """

    def __init__(self):

        """ Setup Dictionary that contains desired teams and generates their data
            for display """

        self._form = COREDependencies.cgi.FieldStorage()
        self._team_dictionary = {}

        for teams in COREDependencies.COREConstants.TEAM_NUMBER_FIELDS:
            # Populates _team_dictionary with : key = alliance color, value = team object
            self._team_dictionary[teams] = DataCalculation.TeamData(self._form.getvalue(teams))
        for populate in self._team_dictionary:
            self._team_dictionary[populate].populate_data()
        #self._alliance_keys = list(self._team_dictionary.keys())

        # Populates _data_keys with all of the report statistic categories accessed from one of the team objects
        # self._data_keys = self._team_dictionary[self._alliance_keys[1]].team_data.keys()

    def generate_table(self):

        """ Iterates through each team objects internal dictionary that contains values for each report statistic
            and dynamically generates a table containing statistics for CoreFiles.Constants.REPORT_HEADER """

        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<title>Team 2062s Scouting Match Table Report</title>')
        print('</head>')
        print('<body>')
        print('<link href="COREStyle_matchreport.css" rel="stylesheet" type="text/css" />')
        print('<table>')
        print('<tr>')
        # Set's up top left corner piece
        print('<td> CORE MATCH REPORT </td>')
        count = 0
        for keys in COREDependencies.COREConstants.TEAM_NUMBER_FIELDS:
            # Set's up the column headers for the table
            if count < 3:
                # Red Teams
                print('<td class ="colRed">', self._team_dictionary[keys]._team_number, '</td>')
            else:
                # Blue Teams
                print('<td class ="colBlue">', self._team_dictionary[keys]._team_number, '</td>')
            count += 1
        print('</tr>')
        for dictionary_key in COREDependencies.COREConstants.REPORT_HEADER:
            print('<tr>')
            # Set's up the number of rows
            # Populates the first item in the row with the row header
            print('<td>', dictionary_key, '</td>')
            for key in COREDependencies.COREConstants.TEAM_NUMBER_FIELDS:
                # Fills the rest of the row with data from each of the team
                print('<td>', self._team_dictionary[key].team_data[dictionary_key], '</td>')
            print('</tr>')
        print('</table>')
        print('</body>')
        print('</html>')

# Creates and generates table
table = MatchReport()
table.generate_table()


