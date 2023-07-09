import sys
import os

from typing import List

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

    def place_whites():
        # TODO
        pass
    
    @staticmethod
    def cnstr_whites() -> List[List]:
        pass

    def place_blacks(self):
        # TODO
        pass

    def place_on_board(self, piece_i : int, piece_j : int, piece):
        self.board[piece_i][piece_j] = piece

    def empty_square(self, piece_i: int, piece_j: int):
        if piece_i + piece_j % 2 == 0:
            self.board[piece_i][piece_j] = 0  # 0 means empty white square
        else :
            self.board[piece_i][piece_j] = 1  # 1 means empty black square

    def get_peice_at_pos(self, piece_i: int, piece_j: int):
        return self[piece_i][piece_j]
    
    def is_piece_at_pos(self, pos_i: int, pos_j: int):
        return isinstance(self.board[pos_i][pos_j], __import__("piece").Piece)
    
