import sqlite3
import os
import json


class Query:
    connection = None

    def __init__(self):
        # Establishing connection to the database
        Query.connection = sqlite3.connect(os.getcwd() + "/Database/Chess-Board.db")
        print(os.getcwd() + "/Database/Chess-Board.db")
        print("Connection to database has been established")

    def ins_score(self, json_str):
        # Parsing json
        white_player = json_str["white_player"]
        black_player = json_str["black_player"]
        duration = json_str["duration"]
        winner = json_str["winner"]
        crs = Query.connection.cursor()
        crs.execute("INSERT INTO Scores VALUE (?,?,?,?)").fetchall()

    def get_all_scores(self):
        crs = Query.connection.cursor()
        rows = crs.execute("SELECT * FROM Scores")
        return json.dump(rows)
