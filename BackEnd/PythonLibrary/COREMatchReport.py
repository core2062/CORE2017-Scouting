#!/usr/bin/python
# Allow Display of elements in HTML

""" Creates a CORE match report, displayed as a table that is to be printed and given to drive team. """

import COREDependencies
import DataCalculation


class MatchReport:

    """ Populates table using TeamData objects for each team. form should supply a match
        number and all the teams to display, but these values should not change because the
        match select interface is modular. """

    def __init__(self):

        """ Setup Dictionary that contains desired teams and generates their data
            for display. Both TEAM_NUMBER_FIELDS and MATCH_NUMBER_FIELD are form keys
            that contain the team numbers to be ranked and the match number they are in.
            These values are hidden from the user and therefore not in COREConstants
            so they should not need to be changed unless COREMatchScheduleDisplay is changed """

        self.TEAM_NUMBER_FIELDS = [
            'RedTeam1',
            'RedTeam2',
            'RedTeam3',
            'BlueTeam1',
            'BlueTeam2',
            'BlueTeam3'
        ]

        self.MATCH_NUMBER_FIELD = 'MatchNumber'
        self._form = COREDependencies.cgi.FieldStorage()
        self._team_dictionary = {}
        self._match_number = self._form.getvalue(self.MATCH_NUMBER_FIELD)
        for teams in self.TEAM_NUMBER_FIELDS:
            self._team_dictionary[teams] = DataCalculation.TeamData(self._form.getvalue(teams))
        for populate in self._team_dictionary:
            self._team_dictionary[populate].populate_data()

    def generate_table(self):

        """ Iterates through each team objects internal dictionary that contains values for each report statistic
            and dynamically generates a table containing statistics for each CoreFiles.Constants.MATCH_HEADER
             CoreFiles.Constants.RANK_AND_MATCH_HEADER """

        COREDependencies.framework_begining()
        print('<link href="css/app.css" rel="stylesheet" type="text/css" />')
        print('<table width="100%">')
        print('<thead>')
        print('<tr>')
        print('<th> CORE MATCH ' + str(self._match_number) +' REPORT </th>')
        count = 0
        for keys in self.TEAM_NUMBER_FIELDS:
            if count < 3:
                print('<th class ="colRed">', self._team_dictionary[keys]._team_number, '</th>')
            else:
                print('<th class ="colBlue">', self._team_dictionary[keys]._team_number, '</th>')
            count += 1
        print('</tr>')
        print('</thead>')
        for dictionary_key in COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS:
            print('<tr>')
            print('<td>', dictionary_key, '</td>')
            for key in self.TEAM_NUMBER_FIELDS:
                print('<td>', self._team_dictionary[key].team_data[dictionary_key], '</td>')
            print('</tr>')
        for dictionary_key in COREDependencies.COREConstants.MATCH_HEADERS:
            print('<tr>')
            print('<td>', dictionary_key, '</td>')
            for key in self.TEAM_NUMBER_FIELDS:
                print('<td>', self._team_dictionary[key].team_data[dictionary_key], '</td>')
            print('</tr>')
        print('</table>')
        COREDependencies.framework_end()

table = MatchReport()
table.generate_table()
