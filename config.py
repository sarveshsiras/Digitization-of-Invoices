import urllib.parse

class DB_connection:

    def __init__(self):
        self.user_name = urllib.parse.quote_plus('your_username')
        self.password = urllib.parse.quote_plus('your_pass')
        self.database_name = "your_databasename"
        self.collection_Name = "your_collectionname"
