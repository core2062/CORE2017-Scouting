import DataCalculation

DataCalculation.TeamData()
class MatchReport:

    def __init__(self):
        self.form = DataCalculation.cgi.FieldStorage()
        self.teamDictionary = {}
        for teams in DataCalculation.Constants.team_number_fields:
            self.teamDictionary[teams] = DataCalculation.TeamData(self.form.getvalue(teams))
            # Populates teamDictionary with : key = alliance color, value = team object
        for populate in self.teamDictionary:
            populate.populatedata()
        self.allianceKeys = self.teamDictionary.keys()
        self.dataKeys = self.teamDictionary[self.allianceKeys[1]].teamData.keys()
        # Populates dataKeys with all of the report statistic categories accessed from one of the team objects

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
        for keys in self.allianceKeys:
            # Set's up the column headers for the table
            print('<td>', keys, '<td/>')
        print('</tr>')
        for dictionaryKey in self.dataKeys:
            print('<tr>')
            # Set's up the number of rows
            # Populates the first item in the row with the row header
            print('<td>', dictionaryKey, '</td>')
            for key in self.teamDictionary:
                # Fills the rest of the row with data from each of the team
                print('<td>', self.teamDictionary[key].teamData[dictionaryKey], '<td/>')
            print('</tr>')
        print('</table>')
        print('</body>')
        print('</html>')


