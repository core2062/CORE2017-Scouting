
""" Various constants used throughout the program that are intended primarily to map form fields,
    but also for key names

        form dependency : Needs to be the same names as those given by the html form.
            It is important that these names appear EXACTLY the same as those supplied by the front end!
        no dependency : Names that will be visually displayed on output tables.
            Should be named in accordance of which they are displaying, but the name is not dependant on any
            other input or variable names"""

"""===========================================
General Team Info (no dependency)
-------------------------------------------"""

TEAM_NUMBER = 2062

COMPETITION_NAME = 'testdata'

"""===========================================
Scout HTML input field names (form dependency)
-------------------------------------------"""

#  form value name that contains the match and team number. (change second name)
TEAM_FIELD_NUMBER = {'team_number': 'TeamNumber'}
MATCH_NUMBER = {'match_number': 'MatchNumber'}

CHECKBOX_NAMES = [
    'CrossedBaselineAuto',
    'GearFloorPickup',
    'FuelPickupHopper',
    'FuelPickupFloor',
    'ActiveDefense'
]
NUMBER_NAMES = [
    MATCH_NUMBER['match_number'],
    'PressureAuto',
    'FuelCycleCountTele',
    'GearsDeliveredTele',
    'GearsDroppedTele',
    'GearsDroppedTransitTele',
    'GearsDroppedFeederTele',
    'HighAlliancePressure',
]
TEXT_NAMES = [
    'ScoutName',
    'comments'
]
RADIO_NAMES = [
    'DeliverGearAuto',
    'FuelAuto',
    'GearFloorPickupType',
    'ShooterType',
    'HighFrequency',
    'HighAccuracy',
    'LowGoalFrequency',
    'Climb'
]
RADIO_VALUES = {
    'DeliverGearAuto': ('LeftGearAuto', 'MiddleGearAuto', 'RightGearAuto', 'None'),
    'FuelAuto': ('FuelLowAuto', 'FuelHighAuto', 'FuelNoneAuto'),
    'GearFloorPickupType': ('Active', 'Passive', 'None'),
    'ShooterType': ('High', 'Low', 'None'),
    'HighFrequency': ('Slow', 'Medium', 'Fast'),
    'HighAccuracy': ('25', '50', '75'),
    'LowGoalFrequency': ('SlowLow', 'FastLow'),
    'Climb': ('DidClimb', 'NoClimb', 'ClimbFail')
}

ALL_NAMES = []

for checkbox in CHECKBOX_NAMES:
    ALL_NAMES.append(checkbox)
for number in NUMBER_NAMES:
    ALL_NAMES.append(number)
for text in TEXT_NAMES:
    ALL_NAMES.append(text)
for radio in RADIO_NAMES:
    ALL_NAMES.append(radio)

"""=====================================
Match Report Row Headers (no dependency)
-------------------------------------"""

REPORT_HEADER = [
    'Avg Fuel Cycles',
    'Avg Gears Tele',
    'Avg Gears Auto',
    'Avg Gear Lost Transit',
    'Avg Gear Lost at Peg',
    'Avg Gear Lost at Feeder',
    'Shooter Type',
    'Shooter Rate and Accuracy'
]



"""=============================================
Match Report input field names (form dependency)
---------------------------------------------"""

RANK_REPORT_FIELD_NAMES = {
    'ranking_options': 'ranking_type'
}

""" The following describes how to use RANK_OPTIONS to map form values to rank statistics.
    it should be a list of tuples that have the following data in them (IN ORDER).

        1. Form value name of RANK_REPORT_FIELD_NAMES['ranking_options'] that you wish to
            correspond the ranking to. (The ranking report form value)
        2. Name of statistic to rank by from REPORT_HEADER
        3. Order in which teams should be ranked. The following are accepted
                'descending' - Ranking from best to worst
                'ascending' - Ranks from worst to best
                'category' - Ranks based on multiple strings given a 3'd argument.
        (4). (ORDER SPECIFIC ARGUMENT) Should only be supplied if order is 'category'.
            A tuple of all possible submission data for the supplied rank_statistic
            category corresponding to the statistic's RADIO_VALUES values in order of
            which should be displayed last, worst -> best.
            Intended to be used for ranking based on a priority of strings.
    EX: 'High Goal Accuracy': ('highGoals', 'high Goal Accuracy', 'descending')
    EX: 'Highest Auto Type': ('highest_auto_type', 'Highest Auto', 'category', ('breach', 'reach', 'no_interaction')) """

RANK_OPTIONS = [
    ('FuelCycles', 'Avg Fuel Cycles', 'descending'),
    ('AvgGearsTele', 'Avg Gears Tele', 'descending'),
    ('AvgGearsAuto', 'Avg Gears Auto', 'descending'),
    ('AvgGearsLostTrans', 'Avg Gear Lost Transit', 'descending'),
    ('AvgGearsLostPeg', 'Avg Gear Lost at Peg', 'descending'),
    ('AvgGearsLostFeed', 'Avg Gear Lost at Feeder', 'descending'),
    ('ShooterType', 'Shooter Type', 'category', ('None', 'Low', 'High')),
    ('ShootRateAccuracy', 'Shooter Rate and Accuracy', 'category', ('SlowLow', 'FastLow', 'Slow 25', 'Slow 50', 'Slow 75', 'Medium 25', 'Medium 50', 'Medium 75', 'Fast 25', 'Fast 50', 'Fast 75'))
]
"""('highGoals', 'High Goal Accuracy', 'descending'),
    ('Autotype', 'Auto Type', 'category', ('Moat', 'Rockwall', 'RoughTerrain'))"""