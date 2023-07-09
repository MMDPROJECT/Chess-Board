import sys
import os

sys.path.append(os.getcwd() + "/Classes")

import Classes.Pieces.piece as piece
import Classes.board as board

from typing import List

class Pawn(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool):
        super().__init__(i, j, is_white)
        self.has_moved = False

    # Override
    def move_to_position(self, board: board.Board, new_i: int, new_j: int):
        super().move_to_position(board, new_i, new_j)
        self.has_moved = True
    
    # Override
    def get_allowed_poses(self, board: board.Board) -> List[List]:
        allowed_moves = []
        # For Whites (Top oriented team)
        if self.is_white:
            # First possiblity (if it's the first move, and there is not blocking piece on opposite, it can move two squares)
            if not self.has_moved and not board.is_piece_at_pos(self.i + 1, self.j):
                allowed_moves.append([self.i + 2, self.j])
                        
            # Second possiblity (if there is no blocking piece on opposite)
            if not board.is_piece_at_pos(self.i + 1, self.j):
                allowed_moves.append([self.i + 1, self.j])

            # Third possiblity (if there is a piece on left bottom diagonal)
            if not board.is_piece_at_pos(self.i + 1, self.j - 1):
                allowed_moves.append([self.i + 1, self.j - 1])

            # Fourth possiblity (if there is a piece on right bottom diagonal)
            if not board.is_piece_at_pos(self.i + 1, self.j + 1):
                allowed_moves.append([self.i + 1, self.j + 1])                
 
        # For Blacks (Bottom oriented team)    
        else:
            # First possiblity (if it's the first move, and there is not blocking piece on opposite, it can move two squares)
            if not self.has_moved and not board.is_piece_at_pos(self.i - 1, self.j):
                allowed_moves.append([self.i - 2, self.j])
                        
            # Second possiblity (if there is no blocking piece on opposite)
            if not board.is_piece_at_pos(self.i - 1, self.j):
                allowed_moves.append([self.i - 1, self.j])

            # Third possiblity (if there is a piece on left top diagonal)
            if not board.is_piece_at_pos(self.i - 1, self.j - 1):
                allowed_moves.append([self.i - 1, self.j - 1])

            # Fourth possiblity (if there is a piece on right top diagonal)
            if not board.is_piece_at_pos(self.i - 1, self.j + 1):
                allowed_moves.append([self.i - 1, self.j + 1])     