#!/usr/bin/python
# Allow Display of elements in HTML

import COREMatchSchedule
import COREDependencies


class ColorCode:

    def __init__(self):
        self._schedule = COREMatchSchedule.SCHEDULE
        self._teams_in_db = []
        self._team_matches_in_db = {}

        self._db_connection = COREDependencies.pymysql.connect(host=COREDependencies.COREDatabaseCredentials.DB_HOST,
                                                               user=COREDependencies.COREDatabaseCredentials.DB_USER,
                                                               password=COREDependencies.COREDatabaseCredentials.DB_PASS,
                                                               db=COREDependencies.COREDatabaseCredentials.DB_NAME,
                                                               charset='utf8mb4',
                                                               cursorclass=COREDependencies.pymysql.cursors.DictCursor)

        try:
            with self._db_connection.cursor() as cursor:
                cursor.execute("SELECT TABLE_NAME FROM INFORMATION_SCHEMA.TABLES WHERE" +
                               " TABLE_TYPE = 'BASE TABLE' AND TABLE_SCHEMA='example'")
                table_name = cursor.fetchone()
                while table_name is not None:
                    self._teams_in_db.append(table_name['TABLE_NAME'])
                    table_name = cursor.fetchone()

                count = 0
                for team in self._teams_in_db:
                    cursor.execute(("SELECT " + COREDependencies.COREConstants.MATCH_NUMBER['match_number'] +
                                    " FROM `" + str(team) + "` ORDER BY `match_id`"))
                    matches = cursor.fetchone()

                    while matches is not None:
                        values = matches.values()
                        if count == 0:
                            for value in values:
                                self._team_matches_in_db[team] = value
                            count = 1
                        else:
                            for value in values:
                                self._team_matches_in_db[team] += value
                        matches = cursor.fetchone()
                    # Goal is to create dictionary with key team number and value: tuple of all match submitions
        finally:
            self._db_connection.close()

    def find_color(self, team_number, match_number):

        """
        Grey - Not Submited post match
        Blue - Submited data
        Green - Ready to Generate Report
        Red - Not Ready to Generate Report
        """

        for team in self._team_matches_in_db:
            if team == team_number:
                for matches in self._team_matches_in_db[team]:
                    if matches == match_number:
                        return 'blue'
                if max(self._team_matches_in_db[team]) > match_number:
                    return 'grey'
