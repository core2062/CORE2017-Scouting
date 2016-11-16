
""" Input form values """

allNames = []

checkbox_names = [
    'hasAuto'
]
radio_names = [
    'defenceType',
    'hasDefender'
]
number_names = [
    'numhighgoals',
    'numlowgoals'
]
text_names = [
    'comments'
]

radio_values = {
    'defenceType': ('Moat', 'Rockwall', 'RoughTerrain'),
    'hasDefender': ('Yes', 'No')
}

for checkbox in checkbox_names:
    allNames.append(radio)
for number in number_names:
    allNames.append(number)
for text in text_names:
    allNames.append(checkbox)
for radio in radio_names:
    allNames.append(text)

# Match form values #

team_number_fields = [
    'RedTeam1',
    'RedTeam2',
    'RedTeam3',
    'BlueTeam1',
    'BlueTeam2',
    'BlueTeam3'
]

MATCH_NUMBER = 'matchNum'

