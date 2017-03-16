
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
        #Determines Amount of Times Gears Are Delivered to Each Peg in Auto
        AllLeftGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][0])
        AllMiddleGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][1])
        AllRightGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][2])
        AllGearsAuto = AllLeftGearsAuto + AllMiddleGearsAuto + AllRightGearsAuto
        #Determines Total Number of Matches Played
        MatchesPlayed = self.num_data_entries('MatchNumber')
        #Average Gears in Tele
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[0]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[3])
        #Average Gears in Auto
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = str(AllGearsAuto) + ' : ' + str(MatchesPlayed)
        #Average Gears Dropped in Transit
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[5])
        #Average Gears Dropped at Peg
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[2]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[4])
        #Average Gears Dropped at Feeder
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[3]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[6])
        #Shooter Type
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[4]] = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[3])
        #Shooter Rate and Accuracy
        if self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[3]) == 'High':
            ShooterRateAccuracy = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[4]) + ' ' + str(self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[5]))
        elif self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[3]) == 'Low':
            ShooterRateAccuracy = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[6])
        else:
            ShooterRateAccuracy = ('Not Applicable')
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[5]] = ShooterRateAccuracy
        #Fuel Pickup Type
        FuelHopperON = self.times_key_exists_in_category(COREDependencies.COREConstants.CHECKBOX_NAMES[2],'ON')
        if FuelHopperON > MatchesPlayed/2:
            FuelHopper = 'Hopper, '
        else:
            FuelHopper = ''
        FuelFloorON = self.times_key_exists_in_category(COREDependencies.COREConstants.CHECKBOX_NAMES[3],'ON')
        if FuelFloorON > MatchesPlayed/2:
            FuelFloor = 'Floor'
        else:
            FuelFloor = ''
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[1]] = (FuelHopper + FuelFloor)
        #Which Gears in Auto
        if AllLeftGearsAuto > 0:
            AutoLeftGear = 'Left,'
        else:
            AutoLeftGear = ''
        if AllRightGearsAuto > 0:
            AutoRightGear = 'Right'
        else:
            AutoRightGear = ''
        if AllMiddleGearsAuto > 0:
            AutoMiddleGear = 'Middle,'
        else:
            AutoMiddleGear = ''
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = (AutoLeftGear +  AutoMiddleGear + AutoRightGear)


