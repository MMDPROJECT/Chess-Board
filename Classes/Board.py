from sys import path
from os import getcwd

path.append(getcwd() + "./Classes/Peices")

from Pieces import Piece

class Board:
    def __init__(self):
        self.board = [
            # 0 means empty white square
            # 1 means empty black square
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0]
        ]

    def cnstr_board(self):
        self.place_whites()
        self.place_blacks()
        pass

    def place_whites(self):
        # TODO
        pass

    # Define methods to construct white and places (they would be called by place whites and blacks)

    def place_blacks(self):
        # TODO
        pass

    def place_on_board(self, piece_i : int, piece_j : int, piece : Piece):
        self.board[piece_i][piece_j] = piece

    def empty_square(self, piece_i: int, piece_j: int):
        if piece_i + piece_j % 2 == 0:
            self.board[piece_i][piece_j] = 0  # 0 means empty white square
        else :
            self.board[piece_i][piece_j] = 1  # 1 means empty black square