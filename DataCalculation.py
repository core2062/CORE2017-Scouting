import CORETeamData
import COREDependencies


class TeamData(CORETeamData.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from REPORT_HEADER when defining keys for team_data """

        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = 76
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.sum_data(COREDependencies.COREConstants.NUMBER_NAMES[0])
