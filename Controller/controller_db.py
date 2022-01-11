from Model.dbconnect import db

class dbController:
    def __init__(self):
        database = db()
        database.dbConnect()
