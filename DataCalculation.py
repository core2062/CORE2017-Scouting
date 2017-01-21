import Team


class TeamData(Team.Team):

    """ use populate_data() to fill team_data with:
        Key - row name
        Value - calculation """

    def populate_data(self):
        self.team_data['cate1'] = Team.sum_data("numhighgoals","numlowgoals")
        self.team_data['cate2'] = 76
        self.team_data['cate5'] = 74
