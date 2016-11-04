import BrowserInputHandling

data_names = []
inputForm = BrowserInputHandling.HtmlInput()
inputForm.get_db_connection()
inputForm.define_team_number('teamNumber')

#Checkboxes:
inputForm.add_checkbox('hasAuto')
if data_names.count('hasAuto') == 0:
    data_names.append('hasAuto')
#radios:
inputForm.add_radio('defenceType')
if data_names.count('defenceType') == 0:
    data_names.append('defenceType')

inputForm.add_radio('hasDefender')
if data_names.count('hasDefender') == 0:
if data_names.count('hasDefender') == 0:
    data_names.append('hasDefender')
#numbers:
inputForm.add_number('numhighgoals')
if data_names.count('numhighgoals') == 0:
    data_names.append('numhighgoals')

inputForm.add_number('numlowgoals')
if data_names.count('numlowgoals') == 0:
    data_names.append('numlowgoals')
#texts:
inputForm.add_text("comments")
if data_names.count('comments') == 0:
    data_names.append('comments')

inputForm.execute_SQL()
inputForm.display_receipt()

def data_list():
    return data_names






