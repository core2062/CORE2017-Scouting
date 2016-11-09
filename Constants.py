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

for checkbox in checkbox_names:
    allNames.append(checkbox)
for radio in radio_names:
    allNames.append(radio)
for number in number_names:
    allNames.append(number)
for text in text_names:
    allNames.append(text)

radio_values = {
    'defenceType': ('Moat', 'Rockwall', 'RoughTerrain'),
    'hasDefender': ('Yes', 'No')
}