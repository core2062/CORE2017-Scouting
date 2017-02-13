#!/usr/bin/python
# Allow Display of elements in HTML

# Import modules for CGI handling & database connection

import COREDependencies


class HtmlInput:

    def __init__(self):

        """ Initalizes SQL Lists and CGI """

        self._checkbox_list = []
        self._radio_list = []
        self._number_list = []
        self._text_list = []
        self._checkbox_list_values = []
        self._radio_list_values = []
        self._number_list_values = []
        self._text_list_values = []
        self._create_table_SQL = ""
        self._insert_SQL = ""
        self._insert_SQL_values = "VALUES ("
        self._insert_data = ()
        self.team_number = -1

        self._form = COREDependencies.cgi.FieldStorage()

        try:
            self._dbConnection = COREDependencies.pymysql.connect(host=COREDependencies.COREDatabaseCredentials.DB_HOST,
                                                           user=COREDependencies.COREDatabaseCredentials.DB_USER,
                                                           password=COREDependencies.COREDatabaseCredentials.DB_PASS,
                                                           database=COREDependencies.COREDatabaseCredentials.DB_NAME,
                                                           charset='utf8mb4',
                                                           cursorclass=COREDependencies.pymysql.cursors.DictCursor)
        except:
            print("Database Connection Error!")

    def define_team_number(self, number):

        """ Gives the team number to the SQL """

        self.team_number = self._form.getvalue(number)

    def add_checkbox(self, input_name):

        """ Binds input_name to a form checkbox name and adds it to the SQL """

        self._checkbox_list.append(str(input_name))
        if self._form.getvalue(str(input_name)):
            self._checkbox_list_values.append("ON")
        else:
            self._checkbox_list_values.append("OFF")

    def add_radio(self, input_name):

        """ Binds input_name to a form radio name and adds it to the SQL """

        self._radio_list.append(str(str(input_name)))
        if self._form.getvalue(str(str(input_name))):
            self._radio_list_values.append(self._form.getvalue(str(str(input_name))))
        else:
            self._radio_list_values.append("Not set")

    def add_number(self, input_name):

        """ Binds input_name to a form number name and adds it to the SQL """

        self._number_list.append(str(input_name))
        if self._form.getvalue(str(input_name)):
            self._number_list_values.append(self._form.getvalue(str(input_name)))
        else:
            self._number_list_values.append("Not set")

    def add_text(self, input_name):

        """ Binds input_name to a form text name and adds it to the SQL """

        self._text_list.append(str(input_name))
        if self._form.getvalue(str(input_name)):
            self._text_list_values.append(self._form.getvalue(str(input_name)))
        else:
            self._text_list_values.append("Not set")

    def execute_SQL(self):

        """ Generates Table and Insert SQL statements given what fields were added """

        first = 0
        all_list = self._checkbox_list + self._radio_list + self._number_list + self._text_list
        self._create_table_SQL += ("CREATE TABLE IF NOT EXISTS `" + str(self.team_number) +
                                   "` (`match_id` int(11) NOT NULL AUTO_INCREMENT,")
        self._insert_SQL += ("INSERT INTO `" + str(self.team_number) + "` (`")
        for checkboxName, checkboxValue in zip(self._checkbox_list, self._checkbox_list_values):
            self._create_table_SQL += ("`" + str(checkboxName) + "` varchar(255) COLLATE utf8_bin NOT NULL,")
            self._insert_data += (checkboxValue,)
        for radioName, radioValue in zip(self._radio_list, self._radio_list_values):
            self._create_table_SQL += ("`" + str(radioName) + "` varchar(255) COLLATE utf8_bin NOT NULL,")
            self._insert_data += (radioValue,)
        for numberName, numberValue in zip(self._number_list, self._number_list_values):
            self._create_table_SQL += ("`" + str(numberName) + "` int(11) NOT NULL,")
            self._insert_data += (numberValue,)
        for textName, textValue in zip(self._text_list, self._text_list_values):
            self._create_table_SQL += ("`" + str(textName) + "` varchar(255) COLLATE utf8_bin NOT NULL,")
            self._insert_data += (textValue,)
        self._create_table_SQL += "PRIMARY KEY (`match_id`),UNIQUE KEY `match_id` (`match_id`),KEY `"
        for names in all_list:
            if first == 0:
                self._create_table_SQL += (str(names) + "` (`" + str(names) + "`")
                self._insert_SQL += (str(names) + "`")
                self._insert_SQL_values += "%s"
                first = 1
            else:
                self._create_table_SQL += (",`" + str(names) + "`")
                self._insert_SQL += (", `" + str(names) + "`")
                self._insert_SQL_values += ", %s"
        self._create_table_SQL += ")) ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin AUTO_INCREMENT=1 ;"
        self._insert_SQL += ") "
        self._insert_SQL_values += ")"
        _insert_SQLstmt = self._insert_SQL + self._insert_SQL_values

        try:
            with self._dbConnection.cursor() as cursor:
                cursor.execute("SET sql_notes = 0;")
                cursor.execute(self._create_table_SQL)
                cursor.execute("SET sql_notes = 1;")
                cursor.execute(_insert_SQLstmt, self._insert_data)
            self._dbConnection.commit()
        finally:
            self._dbConnection.close()

    def display_receipt(self):

        """ Prints a client Receipt to the browser on what was submitted """

        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<title>CGI receipt</title>')
        print('</head>')
        print('<body>')
        print('<h2>You entered the following:</h2>')
        print('<p>Team Number - ' + str(self.team_number) + '</p>')
        for textName, textValue in zip(self._text_list, self._text_list_values):
            print('<p>', textName, '-', textValue, '</p>')
        for numberName, numberValue in zip(self._number_list, self._number_list_values):
            print('<p>', numberName, '-', numberValue, '</p>')
        for radioName, radioValue in zip(self._radio_list, self._radio_list_values):
            print('<p>', radioName, '-', radioValue, '</p>')
        for checkboxName, checkboxValue in zip(self._checkbox_list, self._checkbox_list_values):
            print('<p>', checkboxName, '-', checkboxValue, '</p>')
        print('</body>')
        print('</html>')

# Create object #

inputForm = HtmlInput()
inputForm.define_team_number('teamNumber')

# Populate the database #

for names in COREDependencies.COREConstants.CHECKBOX_NAMES:
    inputForm.add_checkbox(names)
for names in COREDependencies.COREConstants.RADIO_NAMES:
    inputForm.add_radio(names)
for names in COREDependencies.COREConstants.NUMBER_NAMES:
    inputForm.add_number(names)
for names in COREDependencies.COREConstants.TEXT_NAMES:
    inputForm.add_text(names)

# Execute SQL #

inputForm.execute_SQL()
inputForm.display_receipt()