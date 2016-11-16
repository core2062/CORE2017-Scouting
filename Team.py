# Import modules for CGI handling & database connection
import CoreFiles


class Team:
    def __init__(self, teamNumber):
        """ teamData is what gets manipulated with output data """
        self.teamData = {}

        try:
            self.dbConnection = CoreFiles.mysql.connector.connect(user=CoreFiles.DatabaseCredentials.DB_USER,
                                             password=CoreFiles.DatabaseCredentials.DB_PASS,
                                             host=CoreFiles.DatabaseCredentials.DB_HOST,
                                             database=CoreFiles.DatabaseCredentials.DB_NAME)
        except CoreFiles.mysql.connector.Error as err:
            if err.errno == CoreFiles.errorcode.ER_ACCESS_DENIED_ERROR:
                print("Something is wrong with your user name or password")
            elif err.errno == CoreFiles.errorcode.ER_BAD_DB_ERROR:
                print("Database does not exist")
            else:
                print(err)

        self.radio_values = CoreFiles.Constants.radio_values
        self.cursor = self.dbConnection.cursor()
        self.teamNumber = teamNumber
        self.dataList = CoreFiles.Constants.allNames
        self.allData = []
        self.categoryDictionary = {}
        self.cursor.execute("SELECT * FROM Team" + str(self.teamNumber) + " ORDER BY match_id")
        self.allData = self.cursor.fetchall()
        for (data, count) in zip(self.dataList, self.dataList.count()):
            self.categoryDictionary[data] = self.allData[count]

    def team_number(self):
        return self.teamNumber

    def verify_category(self, category):

        """ Verifies the category exists
            Otherwise  ____ """
        verified = 0
        for item in self.dataList:
            if item == category:
                verified = 1
        return verified

    def get_data(self, category):

        """Returns category data in a tuple
           -Internal function-"""

        if self.verify_category(category) == 1:
            for key in self.categoryDictionary:
                if str(key) == str(category):
                    return self.categoryDictionary[key]

    def sum_data(self, category, category2='none'):

        """ Number specific function which given one or two
            categories adds all the values together """

        if self.verify_category(category) == 1:
            sum = 0
            for data in self.get_data(category):
                sum += data
            if category2 != 'none':
                for itr in self.get_data(category2):
                    sum += itr
            return sum

    def num_data_entries(self, category):

        """ Returns number of times there is data in a category """

        if self.verify_category(category) == 1:
            count = 0
            for data in self.get_data(category):
                count += count+1
            return count

    def avg_data(self, category):

        """ Finds the mean of a category number set """

        if self.verify_category(category) == 1:
            return self.sum_data(category)/self.num_data_entries(category)

    def max_in_data(self, category):

        """ Finds the max in the category number set """

        if self.verify_category(category) == 1:
            count = 0
            for data in self.get_data(category):
                if count == 0:
                    max = data
                    count = 1
                if data > max:
                    max = data
            return max

    def min_in_data(self, category):

        """ Finds the min in the category number set """

        if self.verify_category(category) == 1:
            count = 0
            for data in self.get_data(category):
                if count == 0:
                    min = data
                    count = 1
                if data < min:
                    min = data
            return min

    def return_best(self, category, rankOrder):

        """ Radio specific function which displays best option
            rankOrder = Tuple of all radio options available in that category
            ranked from worst to best """

        if self.verify_category(category) == 1:
            highest = 'N/A'
            for item in rankOrder:
                for data in self.get_data(category):
                    if item == data:
                        highest = data
            return highest