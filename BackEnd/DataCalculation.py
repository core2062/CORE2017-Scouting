
import PythonLibrary.COREDependencies as COREDependencies
import PythonLibrary.CORETeamData as CORETeamData


class TeamData(CORETeamData.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from REPORT_HEADER when defining keys for team_data """

        """self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = 76
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[0])
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[2]] = self.return_best(COREDependencies.COREConstants.RADIO_NAMES[0], ('Moat', 'Rockwall', 'RoughTerrain'))
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[3]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[0])"""
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[1])
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[2])
        AllLeftGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][0])
        AllMiddleGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][1])
        AllRightGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][2])
        AllGearsAuto = AllLeftGearsAuto + AllMiddleGearsAuto + AllRightGearsAuto
        MatchesPlayed = self.num_data_entries('match-id')
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[2]]= str(AllGearsAuto) + ' : ' + str(MatchesPlayed)

