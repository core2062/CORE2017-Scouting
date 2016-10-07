#!C:\Python34\python.exe -u

# Import modules for CGI handling & database connection
import DatabaseCredentials
import mysql.connector
from mysql.connector import errorcode
import cgi


class HtmlInput:

    def __init__(self):
        self.dbConnection = -1
        self.cursor = -1
        # Initializes lists to store values posted
        self.checkboxList = []
        self.radioList = []
        self.numberList = []
        self.textList = []
        self.checkboxListValues = []
        self.radioListValues = []
        self.numberListValues = []
        self.textListValues = []
        # Create instance of FieldStorage to get elements from the browser
        self.form = cgi.FieldStorage()
        # Initializes SQL Statement
        self.createTableSQL = ""
        self.insertSQL = ""
        self.insetSQLValues = "VALUES ("
        self.insertData = ()
        self.teamNumber = -1

    def get_db_connection(self):
        try:
            self.dbConnection = mysql.connector.connect(user=DatabaseCredentials.DB_USER,
                                             password=DatabaseCredentials.DB_PASS,
                                             host=DatabaseCredentials.DB_HOST,
                                             database=DatabaseCredentials.DB_NAME)
        except mysql.connector.Error as err:
            if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)
        self.cursor = self.dbConnection.cursor()

    def define_team_number(self, number):
        self.teamNumber = self.form.getvalue(number)

    def add_checkbox(self, inputname):
        self.checkboxList.append(inputname)
        if self.form.getvalue(inputname):
            self.checkboxListValues.append("ON")
        else:
            self.checkboxListValues.append("OFF")

    def add_radio(self, inputname):
        self.radioList.append(inputname)
        if self.form.getvalue(inputname):
            self.radioListValues.append(self.form.getvalue(inputname))
        else:
            self.radioListValues.append("Not set")

    def add_number(self, inputname):
        self.numberList.append(inputname)
        if self.form.getvalue(inputname):
            self.numberListValues.append(self.form.getvalue(inputname))
        else:
            self.numberListValues.append("Not set")

    def add_text(self, inputname):
        self.textList.append(inputname)
        if self.form.getvalue(inputname):
            self.textListValues.append(self.form.getvalue(inputname))
        else:
            self.textListValues.append("Not set")

    def execute_SQL(self):
        first = 0
        self.createTableSQL += "CREATE TABLE IF NOT EXISTS `Team"
        self.createTableSQL += str(self.teamNumber)
        self.createTableSQL += "` (`match_id` int(11) NOT NULL AUTO_INCREMENT,"
        self.insertSQL += "INSERT INTO Team"
        self.insertSQL += str(self.teamNumber)
        self.insertSQL += " ("
        for checkboxName, checkboxValue in zip(self.checkboxList, self.checkboxListValues):
            self.createTableSQL += "`"
            self.createTableSQL += str(checkboxName)
            self.createTableSQL += "` varchar(4) NOT NULL,"
            self.insertData = self.insertData + (checkboxValue,)
        for radioName, radioValue in zip(self.radioList, self.radioListValues):
            self.createTableSQL += "`"
            self.createTableSQL += str(radioName)
            self.createTableSQL += "` varchar(20) NOT NULL,"
            self.insertData = self.insertData + (radioValue,)
        for numberName, numberValue in zip(self.numberList, self.numberListValues):
            self.createTableSQL += "`"
            self.createTableSQL += str(numberName)
            self.createTableSQL += "` int(11) NOT NULL,"
            self.insertData = self.insertData + (numberValue,)
        for textName, textValue in zip(self.textList, self.textListValues):
            self.createTableSQL += "`"
            self.createTableSQL += str(textName)
            self.createTableSQL += "` varchar(20) NOT NULL,"
            self.insertData = self.insertData + (textValue,)
        self.createTableSQL += "PRIMARY KEY (`match_id`),UNIQUE KEY `match_id` (`match_id`),KEY `"
        for checkboxNames in self.checkboxList:
            if first == 0:
                self.createTableSQL += str(checkboxNames)
                self.createTableSQL += "` (`"
                self.createTableSQL += str(checkboxNames)
                self.createTableSQL += "`"
                self.insertSQL += str(checkboxNames)
                self.insetSQLValues += "%s"
                first = 1
            else:
                self.createTableSQL += ",`"
                self.createTableSQL += str(checkboxNames)
                self.createTableSQL += "`"
                self.insertSQL += ", "
                self.insertSQL += str(checkboxNames)
                self.insetSQLValues += ", %s"
        for radioNames in self.radioList:
            self.createTableSQL += ",`"
            self.createTableSQL += str(radioNames)
            self.createTableSQL += "`"
            self.insertSQL += ", "
            self.insertSQL += str(radioNames)
            self.insetSQLValues += ", %s"
        for numberNames in self.numberList:
            self.createTableSQL += ",`"
            self.createTableSQL += str(numberNames)
            self.createTableSQL += "`"
            self.insertSQL += ", "
            self.insertSQL += str(numberNames)
            self.insetSQLValues += ", %i"
        for textNames in self.textList:
            self.createTableSQL += ",`"
            self.createTableSQL += str(textNames)
            self.createTableSQL += "`"
            self.insertSQL += ", "
            self.insertSQL += str(textNames)
            self.insetSQLValues += ", %s"
        self.createTableSQL += ")) ENGINE=InnoDB  DEFAULT CHARSET=latin1 AUTO_INCREMENT=3 ;"
        self.insertSQL += ") "
        self.insetSQLValues += ")"
        insertSQLstmt = (
            self.createTableSQL,
            self.insetSQLValues
        )

        #print(self.createTableSQL)
        #print(self.createInsertSQL)

        try:
            self.cursor.execute(self.createTableSQL)
        except mysql.connector.Error as error:
            print(error.msg)
        self.cursor.execute(insertSQLstmt, self.insertData)
        self.dbConnection.commit()
        self.cursor.close()
        self.dbConnection.close()

    def display_receipt(self):
        print("Content-type:text/html\r\n\r\n")
        print('<html>')
        print('<head>')
        print('<title>CGI receipt</title>')
        print('</head>')
        print('<body>')
        print('<h2>You entered the following:</h2>')
        for textName, textValue in zip(self.textList, self.textListValues):
            print('<p>', textName, '-', textValue, '</p>')
        for numberName, numberValue in zip(self.numberList, self.numberListValues):
            print('<p>', numberName, '-', numberValue, '</p>')
        for radioName, radioValue in zip(self.radioList, self.radioListValues):
            print('<p>', radioName, '-', radioValue, '</p>')
        for checkboxName, checkboxValue in zip(self.checkboxList, self.checkboxListValues):
            print('<p>', checkboxName, '-', checkboxValue, '</p>')
        print('</body>')
        print('</html>')