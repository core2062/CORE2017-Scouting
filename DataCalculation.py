import Team
import CoreFiles


class TeamData(Team.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from REPORT_HEADER when defining keys for team_data """

        self.team_data[CoreFiles.Constants.REPORT_HEADER[0]] = 76
        self.team_data[CoreFiles.Constants.REPORT_HEADER[1]] = self.sum_data(CoreFiles.Constants.NUMBER_NAMES[0])
