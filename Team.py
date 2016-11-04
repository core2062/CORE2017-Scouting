# Import modules for CGI handling & database connection
import DatabaseCredentials
import mysql.connector
from mysql.connector import errorcode
import cgi
from web_input import data_list

class Team(teamNumber):
    def __init__(self, teamNumber):
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
        self.teamNumber = teamNumber
        self.dataList = data_list()
        self.allData = []
        self.categoryDictionary = {}

        self.cursor.execute("SELECT * FROM Team" + str(self.teamNumber) + " ORDER BY match_id")
        self.allData = self.cursor.fetchall()
        for (data, count) in zip(self.dataList, self.dataList.count()):
            self.categoryDictionary[data] = self.allData[count]

    def get_data(self, category):

        for key in self.categoryDictionary:
            if str(key) == str(category):
                return self.categoryDictionary[key]
            else:
                return 0
