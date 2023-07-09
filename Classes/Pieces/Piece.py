from sys import path
from os import getcwd

path.append(getcwd())
path.append(getcwd() + "./Classes/Peices")

import Board
from typing import Any, List

class Piece:
    def __init__(self, i: int, j: int, is_white: bool):
        self.i = i
        self.j = j
        self.is_white = is_white

    def place_on_board(self, board: Board):
        board.place_on_board(self.i, self.j, self)

    def move_to_position(self, board: Board, new_i: int, new_j: int):
        board.empty_square(self.i, self.j)
        self.i = new_i
        self.j = new_j
        board.place_on_board(self.i, self.j, self)

    def capture(self, board : Board, enemy_i : int, enemy_j : int, enemy_piece : 'Piece'):
        board.empty_square(self.i, self.j)
        board.empty_square(enemy_i, enemy_j)

        self.i = enemy_i
        self.j = enemy_j

        board.place_on_board(self.i, self.j, self)

        del enemy_piece 
        

    # This should be overrided in child classes
    def get_moving_poses(self):
        pass

    def __str__(self):
        return f"peice with i:{self.i} j:{self.j} and is_white{self.is_white}"
    
    def __call__(self):
        return f"peice with i:{self.i} j:{self.j} and is_white{self.is_white}"


        