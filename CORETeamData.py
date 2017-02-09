# Import modules for CGI handling & database connection
import COREDependencies


class Team:

    """"""

    def __init__(self, team_number):

        """ team_data is what gets manipulated with output data
            _all_data stores all information from the database in a 2 dimensional array
            _category_dictionary: key = category heading, value = tuple of user inputs """

        self.team_data = {}

        # Create and setup SQL #

        self.db_connection = COREDependencies.pymysql.connect(host=COREDependencies.COREDatabaseCredentials.DB_HOST,
                                                              user=COREDependencies.COREDatabaseCredentials.DB_USER,
                                                              password=COREDependencies.COREDatabaseCredentials.DB_PASS,
                                                              db=COREDependencies.COREDatabaseCredentials.DB_NAME,
                                                              charset='utf8mb4',
                                                              cursorclass=COREDependencies.pymysql.cursors.DictCursor)
        self._team_number = int(team_number)
        self._radio_values = COREDependencies.COREConstants.RADIO_VALUES
        self._data_list = COREDependencies.COREConstants.ALL_NAMES
        self._all_data = []
        self._category_dictionary = {}
        try:
            with self.db_connection.cursor() as cursor:
                cursor.execute(("SELECT * FROM `" + str(self._team_number) + "` ORDER BY `match_id`"))
                count = 0
                id = cursor.fetchone()
                while id is not None:
                    keys = id.keys()
                    values = id.values()
                    if count == 0:
                        for (key, value) in zip(keys, values):
                            self._category_dictionary[key] = (value,)
                        count = 1
                    else:
                        for (key, value) in zip(keys, values):
                            self._category_dictionary[key] += (value,)
                    id = cursor.fetchone()
        finally:
            self.db_connection.close()

    def team_number(self):

        """ Returns given team number """

        return self._team_number

    def _verify_category(self, category):

        """ Verifies the category exists
            Otherwise 'something bad happens' """

        verified = 0
        for item in self._data_list:
            if item == category:
                verified = 1
        return verified

    def _get_data(self, category):

        """ Returns category data in a tuple """

        if self._verify_category(category) == 1:
            for key in self._category_dictionary:
                if str(key) == str(category):
                    return self._category_dictionary[key]

    def sum_data(self, category, category2='none'):

        """ Number specific function which given one or two
            categories adds all the values together """

        if self._verify_category(category) == 1:
            total = 0
            for data in self._get_data(category):
                total += data
            if category2 != 'none':
                for itr in self._get_data(category2):
                    total += itr
            return total

    def num_data_entries(self, category):

        """ Returns number of times there is data in a category """

        if self._verify_category(category) == 1:
            return len(self._get_data(category))

    def avg_data(self, category):

        """ Finds the mean of a category number set """

        if self._verify_category(category) == 1:
            if self.num_data_entries(category) != 0:
                return self.sum_data(category)/self.num_data_entries(category)
            else:
                return 0

    def max_in_data(self, category):

        """ Finds the max in the category number set """

        if self._verify_category(category) == 1:
            count = 0
            max = 0
            for data in self._get_data(category):
                if count == 0:
                    max = data
                    count = 1
                if data > max:
                    max = data
            return max

    def min_in_data(self, category):

        """ Finds the min in the category number set """

        if self._verify_category(category) == 1:
            count = 0
            min = 0
            for data in self._get_data(category):
                if count == 0:
                    min = data
                    count = 1
                if data < min:
                    min = data
            return min

    def return_best(self, category, rank_order):

        """ Radio specific function which displays best option
            rankOrder = Tuple of all radio options available in that category
            ranked from worst to best """

        if self._verify_category(category) == 1:
            highest = 'N/A'
            for item in rank_order:
                for data in self._get_data(category):
                    if item == data:
                        highest = data
            return highest

    def list_all_results(self, category):

        """ Outputs a string that contains all results separated by ;
            *primarily used for comments* """

        output = ''
        if self._verify_category(category) == 1:
            for data in self._get_data(category):
                output += str(data) + '; '
        return output
