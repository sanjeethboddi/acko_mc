from module.persistence import Persistence

import firebase_admin
from firebase_admin import credentials, firestorecred = credentials.Certificate("path/to/serviceAccountKey.json")

class FirebasePersistence(Persistence):
    def __init__(self):
        firebase_admin.initialize_app(cred)

    def save(self, key, value):
        self.data[key] = value

    def get(self, key):
        return self.data[key]
