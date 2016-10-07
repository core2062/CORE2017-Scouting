import BrowserInputHandling




inputForm = BrowserInputHandling.HtmlInput()
inputForm.get_db_connection()
inputForm.define_team_number('teamNumber')
inputForm.add_number('numhighgoals')
inputForm.add_number('numlowgoals')
inputForm.add_checkbox('hasAuto')
inputForm.add_radio('defenceType')
inputForm.add_radio('hasDefender')
inputForm.add_text("comments")
inputForm.execute_SQL()
inputForm.display_receipt()






