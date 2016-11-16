import SendToDatabase
import CoreFiles

inputForm = SendToDatabase.HtmlInput
inputForm.get_db_connection()
inputForm.define_team_number('teamNumber')

for names in CoreFiles.Constants.checkbox_names:
    inputForm.add_checkbox(names)
for names in CoreFiles.Constants.radio_names:
    inputForm.add_radio(names)
for names in CoreFiles.Constants.number_names:
    inputForm.add_number(names)
for names in CoreFiles.Constants.text_names:
    inputForm.add_text(names)

inputForm.execute_SQL()
inputForm.display_receipt()
