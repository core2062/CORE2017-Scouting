
import PythonLibrary.COREDependencies as COREDependencies
import PythonLibrary.CORETeamData as CORETeamData


class TeamData(CORETeamData.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):

        """ Use Constants from RANK_AND_MATCH_HEADERS, MATCH_HEADERS, and RANK_ONLY_HEADERS when defining keys for team_data """

        """self.team_data[COREDependencies.COREConstants.REPORT_HEADER[0]] = 76
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[0])
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[2]] = self.return_best(COREDependencies.COREConstants.RADIO_NAMES[0], ('Moat', 'Rockwall', 'RoughTerrain'))
        self.team_data[COREDependencies.COREConstants.REPORT_HEADER[3]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[0])"""
        #Determines Amount of Times Gears Are Delivered to Each Peg in Auto
        AllGearsTele = self.sum_data(COREDependencies.COREConstants.NUMBER_NAMES[3])
        AllLeftGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][0])
        AllMiddleGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][1])
        AllRightGearsAuto = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[0], COREDependencies.COREConstants.RADIO_VALUES['DeliverGearAuto'][2])
        AllGearsAuto = AllLeftGearsAuto + AllMiddleGearsAuto + AllRightGearsAuto
        #Determines Total Number of Matches Played
        MatchesPlayed = self.num_data_entries('MatchNumber')
        #Average Gears in Auto
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[0]] = str(AllGearsAuto) + ' : ' + str(MatchesPlayed)
        #Average Gears Dropped in Transit
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[0]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[5])
        #Average Gears Dropped at Peg
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[4])
        #Average Gears Dropped at Feeder
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[2]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[6])
        #Shooter Type
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[3]] = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[3])
        #Shooter Rate and Accuracy
        if self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[3]) == 'High':
            ShooterRateAccuracy = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[4]) + ' ' + str(self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[5]))
        elif self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[3]) == 'Low':
            ShooterRateAccuracy = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[6])
        else:
            ShooterRateAccuracy = ('Not Applicable')
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[4]] = ShooterRateAccuracy
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
        if (FuelHopper + FuelFloor) == '':
            self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[1]] = 'None'
        else:
            self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[1]] = (FuelHopper + FuelFloor)
        #Which Gears in Auto
        """if AllLeftGearsAuto > 0:
            AutoLeftGear = 'Boiler,'
        else:
            AutoLeftGear = ''
        if AllRightGearsAuto > 0:
            AutoRightGear = 'Feeder'
        else:
            AutoRightGear = ''
        if AllMiddleGearsAuto > 0:
            AutoMiddleGear = 'Middle,'
        else:
            AutoMiddleGear = ''
        if (AutoLeftGear + AutoMiddleGear + AutoRightGear) == '':
            self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = 'None'
        else:
            self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = (AutoLeftGear + AutoMiddleGear + AutoRightGear)"""
        SuccessOrFail = self._list_of_all_results(COREDependencies.COREConstants.RADIO_NAMES[9])
        Gears = self._list_of_all_results(COREDependencies.COREConstants.RADIO_NAMES[1])

        BoilerSuccess = 0
        MiddleSuccess = 0
        FeederSuccess = 0
        Failures = 0
        AutoBoilerGear = ''
        AutoMiddleGear = ''
        AutoFeederGear = ''
        AutoFailGear = ''
        for (GearPeg, SuccessesOrFails) in zip(Gears, SuccessOrFail):
            if GearPeg == 'BoilerGearAuto' and SuccessesOrFails == 'Success':
                BoilerSuccess += 1
            elif GearPeg == 'MiddleGearAuto' and SuccessesOrFails == 'Success':
                MiddleSuccess += 1
            elif GearPeg == 'FeederGearAuto' and SuccessesOrFails == 'Success':
                FeederSuccess += 1
            else:
                Failures += 1
            AutoFailGear = str(Failures)
            if BoilerSuccess > 0:
                AutoBoilerGear = 'Boiler,'
            else:
                AutoBoilerGear = ''
            if MiddleSuccess > 0:
                AutoMiddleGear = 'Middle,'
            else:
                AutoMiddleGear = ''
            if FeederSuccess > 0:
                AutoFeederGear = 'Feeder'
            else:
                AutoFeederGear = ''
        if (BoilerSuccess + MiddleSuccess + FeederSuccess) == 0:
            self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = ('None' + 'Fails:' + AutoFailGear)
        else:
            self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[2]] = (AutoBoilerGear + AutoMiddleGear + AutoFeederGear + 'Fails:' + AutoFailGear)
        #Climb Ratio. Success:Fail:No Attempt
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[3]] = str(self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[7],'DidClimb')) + ':' + str(self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[7],'ClimbFail')) + ':' + str(self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[7],'NoClimb'))
        ClimbRatio = self.times_key_exists_in_category(COREDependencies.COREConstants.RADIO_NAMES[7],'DidClimb') / MatchesPlayed
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[0]] = ClimbRatio
        #Comments
        self.team_data[COREDependencies.COREConstants.MATCH_HEADERS[4]] = self.list_all_results(COREDependencies.COREConstants.TEXT_NAMES[1])
        #Avg Auto & Tele Kpa
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[1]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[1])
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[2]] = self.avg_data(COREDependencies.COREConstants.NUMBER_NAMES[7])
        # Draven Auto & Tele Kpa

        """times_auto_high = self.times_key_exists_in_category('FuelAuto', 'FuelHighAuto')
        times_auto_low = self.times_key_exists_in_category('FuelAuto', 'FuelLowAuto')
        all_auto_kpas = self._list_of_all_results('PressureAuto')
        auto_kap_sum = 0
        auto_kap_counter = 0
        if times_auto_high > 0 or times_auto_low > 0:
            for entry in all_auto_kpas:
                if entry != 0 or None:
                    auto_kap_counter += 1
                    auto_kap_sum += entry
            if auto_kap_counter != 0:
                self.team_data['Avg Auto Kpa'] = (auto_kap_sum/auto_kap_counter)
            else:
                self.team_data['Avg Auto Kpa'] = 0
        else:
            self.team_data['Avg Auto Kpa'] = 0

        times_tele_high = self.times_key_exists_in_category('ShooterType', 'High')
        times_tele_low = self.times_key_exists_in_category('ShooterType', 'Low')
        all_tele_kaps = self._list_of_all_results('HighAlliancePressure')
        tele_kap_sum = 0
        tele_kap_counter = 0
        if times_tele_high > 0 or times_tele_low > 0:
            for entry in all_tele_kaps:
                if entry != 0 or None:
                    tele_kap_counter += 1
                    tele_kap_sum += entry
            if tele_kap_counter != 0:
                self.team_data['Avg Tele Kpa'] = ((tele_kap_sum / tele_kap_counter) - self.team_data['Avg Auto Kpa'])
            else:
                self.team_data['Avg Tele Kpa'] = 0
        else:
            self.team_data['Avg Tele Kpa'] = 0"""

        # Draven OPR

        baseline_crosses = self.times_key_exists_in_category('CrossedBaselineAuto', 'ON')
        if MatchesPlayed != 0:
            self.team_data['CORE-PR'] = (round((self.team_data['Avg Tele Kpa']) + (self.team_data['Avg Auto Kpa']) +
                                               ((AllGearsTele / MatchesPlayed * 11.43) + ((AllGearsAuto / MatchesPlayed) * 17.14) + (ClimbRatio * 50) + ((baseline_crosses / MatchesPlayed) * 5)), 2))
        else:
            self.team_data['CORE-PR'] = 0

        # Active V. Passive
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[6]] = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[2])
        # Total Kpa
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[7]] = round(((self.sum_data(COREDependencies.COREConstants.NUMBER_NAMES[1]) + self.sum_data(COREDependencies.COREConstants.NUMBER_NAMES[7])) / MatchesPlayed), 2)
        #Total Gears
        TotalAutoGears = self.times_key_exists_in_category('DeliverGearAuto', 'BoilerGearAuto') + self.times_key_exists_in_category('DeliverGearAuto', 'MiddleGearAuto') + self.times_key_exists_in_category('DeliverGearAuto', 'FeederGearAuto')
        self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[8]] = round(((self.sum_data(COREDependencies.COREConstants.NUMBER_NAMES[3]) + TotalAutoGears) / MatchesPlayed), 2)
        # Gear Floor Pickup
        PercentageOfEnteries = self.times_key_exists_in_category('GearFloorPickup', 'ON') / MatchesPlayed
        if PercentageOfEnteries > 0.5:
            self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[9]] = 'Gear Floor Pickup'
        else:
            self.team_data[COREDependencies.COREConstants.RANK_AND_MATCH_HEADERS[9]] = 'No Gear Floor Pickup'
        #Defense Rating
        self.team_data[COREDependencies.COREConstants.RANK_ONLY_HEADERS[3]] = self.avg_category(COREDependencies.COREConstants.RADIO_NAMES[8])