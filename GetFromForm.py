import SendToDatabase
import CoreFiles

inputForm = SendToDatabase.HtmlInput()
inputForm.define_team_number('teamNumber')

# Populate the database #

for names in CoreFiles.Constants.CHECKBOX_NAMES:
    inputForm.add_checkbox(names)
for names in CoreFiles.Constants.RADIO_NAMES:
    inputForm.add_radio(names)
for names in CoreFiles.Constants.NUMBER_NAMES:
    inputForm.add_number(names)
for names in CoreFiles.Constants.TEXT_NAMES:
    inputForm.add_text(names)

# Execute SQL #

inputForm.execute_SQL()
inputForm.display_receipt()
