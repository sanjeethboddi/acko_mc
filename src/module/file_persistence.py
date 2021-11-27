from module.persistence import Persistence
import pickle as pk

import pickle


class FilePersistence(Persistence):
    def __init__(self, name):
        self.filename = name
        teams = []
        with open(name, 'a+') as handle:
            pickle.dump(teams, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def save(self, team):
        teams = []
        with open(self.filename, 'rb') as handle:
            teams = pickle.load(handle)
        teams.append(team)
        print(teams)
        with open(self.filename, 'wb') as handle:
            pickle.dump(teams, handle, protocol=pickle.HIGHEST_PROTOCOL)

    def get_team(self, teamId):
        teams = []
        with open(self.filename, 'rb') as handle:
            teams = pickle.load(handle)
        for team in teams:
            if team["team"]["id"] == teamId:
                return team
