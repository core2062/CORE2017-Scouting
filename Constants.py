
""" It is important that these names appear EXACTLY the same as those supplied by the front end! """

#                   #
# Input form values #
#                   #

CHECKBOX_NAMES = [
    'hasAuto'
]
RADIO_NAMES = [
    'defenceType',
    'hasDefender'
]
NUMBER_NAMES = [
    'numhighgoals',
    'numlowgoals'
]
TEXT_NAMES = [
    'comments'
]

RADIO_VALUES = {
    'defenceType': ('Moat', 'Rockwall', 'RoughTerrain'),
    'hasDefender': ('Yes', 'No')
}

#                             #
#     Match form values       #
# Use Same Names On Front End #
#                             #

TEAM_NUMBER_FIELDS = [
    'RedTeam1',
    'RedTeam2',
    'RedTeam3',
    'BlueTeam1',
    'BlueTeam2',
    'BlueTeam3'
]

MATCH_NUMBER = 'matchNum'

#                          #
#   Report Heading Names   #
#                          #

REPORT_HEADER = [
    'high goal accuracy',
    'auto pts'
]

# Populates ALL_Names #

ALL_NAMES = []

for checkbox in CHECKBOX_NAMES:
    ALL_NAMES.append(checkbox)
for number in NUMBER_NAMES:
    ALL_NAMES.append(number)
for text in TEXT_NAMES:
    ALL_NAMES.append(text)
for radio in RADIO_NAMES:
    ALL_NAMES.append(radio)



