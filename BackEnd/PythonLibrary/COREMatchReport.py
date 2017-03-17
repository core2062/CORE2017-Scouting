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

        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<meta charset="utf-8">')
        print('<link rel="shortcut icon" href="favicon.ico" />')
        print('<meta name="description" content="CORE 2062 Scouting">')
        print('<meta name="author" content="CORE2062">')
        print('<meta name="robots" content="noindex, nofollow">')
        print('<meta name="theme-color" content="#ff731c" />')
        print(
            '<meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no" />')
        print('<title>CORE 2062 Scouting | Match Display</title>')
        print(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/normalize/5.0.0/normalize.min.css" ' +
            'integrity="sha256-t2/7smZfgrST4FS1DT0bs/KotCM74XlcqZN5Vu7xlrw=" crossorigin="anonymous" />')
        print(
            '<link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/css/foundation.min.css" ' +
            'integrity="sha256-NTds7atVCDeolLUzbcl45lx4gJYO+hNXCaX1wC2HQHc=" crossorigin="anonymous" />')
        print('<link rel="stylesheet" href="css/app.css">')
        print('<script src="https://cdnjs.cloudflare.com/ajax/libs/modernizr/2.8.3/modernizr.min.js" integrity="' +
              'sha256-0rguYS0qgS6L4qVzANq4kjxPLtvnp5nn2nB5G1lWRv4=" crossorigin="anonymous"></script>')
        print('</head>')
        print('<body>')
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
        for dictionary_key in COREDependencies.COREConstants.MATCH_HEADERS:
            print('<tr>')
            print('<td>', dictionary_key, '</td>')
            for key in self.TEAM_NUMBER_FIELDS:
                print('<td>', self._team_dictionary[key].team_data[dictionary_key], '</td>')
            print('</tr>')
        for dictionary_key in COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS:
            print('<tr>')
            print('<td>', dictionary_key, '</td>')
            for key in self.TEAM_NUMBER_FIELDS:
                print('<td>', self._team_dictionary[key].team_data[dictionary_key], '</td>')
            print('</tr>')
        print('</table>')
        print('<script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.1.1/jquery.min.js" integrity="' +
              'sha256-hVVnYaiADRTO2PzUGmuLJr8BLUSjGIZsDYGmIJLv2b8=" crossorigin="anonymous"></script>')
        print('<script src="https://cdnjs.cloudflare.com/ajax/libs/foundation/5.5.3/js/foundation.min.js" integrity=' +
              '"sha256-KXypdIy75PPHsbEaVkrhBvlQg8XTQy8NvalzrIxMrco=" crossorigin="anonymous"></script>')
        print('<script>')
        print('$(document).foundation();')
        print('</script>')
        print('</body>')
        print('</html>')

table = MatchReport()
table.generate_table()
