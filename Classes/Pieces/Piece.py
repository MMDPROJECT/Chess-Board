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

    # This method places a piece on the board
    def place_on_board(self, board: Board):
        # Calling board method to place the piece on itself
        board.place_on_board(self.i, self.j, self)

    # This method moves a piece on the chess-board
    def move_to_position(self, board: Board, new_i: int, new_j: int):
        # Calling board method to empty the square in itself
        board.empty_square(self.i, self.j)
        # Renewing the ally position
        self.i = new_i
        self.j = new_j
        # Placing the piece on the new position
        board.place_on_board(self.i, self.j, self)

    # This method capures an enemy piece
    def capture(self, board : Board, enemy_i : int, enemy_j : int, enemy_piece : 'Piece'):
        # Empty both ally square and enemy square first
        board.empty_square(self.i, self.j)
        board.empty_square(enemy_i, enemy_j)
        # Renewing the ally position on the board
        self.i = enemy_i
        self.j = enemy_j
        # Calling board method to place the ally piece on the new position
        board.place_on_board(self.i, self.j, self)
        # Releasing the memory that has been taken by enemy piece 
        del enemy_piece 
        

    # This should be overrided in child classes
    def get_moving_poses(self):
        pass
    
    def __call__(self):
        return f"peice with i:{self.i} j:{self.j} and is_white{self.is_white}"