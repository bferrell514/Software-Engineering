import pickle
from os.path import exists

from users import User


class Database:
    @staticmethod
    def load():
        return pickle.load(open(".database.p", "rb"))

    def save(self):
        pickle.dump(self.users, open(".database.p", "wb"))

    def add_user(self, username, password, major):
        if username in self.users:
            raise ValueError("This username was already in the database")
        else:
            self.users[username] = User(username, password, major)
            self.save()

    def login_user(self, username, password):
        user = self.users[username]

        login_status = user.authenticate(password)

        if login_status is True:
            return self.users[username]
        else:
            return None

    def __init__(self):
        if exists(".database.p"):
            self.users = self.load()
        else:
            self.users = dict()
