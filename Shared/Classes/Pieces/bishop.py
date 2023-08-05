from __future__ import annotations

import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
<<<<<<< HEAD
=======
import board
>>>>>>> fix/UI

class Bishop(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)

    # This method annonces all the possible moves
<<<<<<< HEAD
    def get_allowed_poses(self, board) -> list[list]:
=======
    def get_allowed_poses(self, board: board.Board) -> list[list]:
>>>>>>> fix/UI
        allowed_moves = []
        
        # First option is to move to right top diagonal
        i = self.i - 1
        j = self.j + 1
        while 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
            j += 1
        
        # Second option is to move to right bottom diagonal
        i = self.i + 1
        j = self.j + 1
        while 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1
            j += 1

        # Third option is to move to left bottom diagonal
        i = self.i + 1
        j = self.j - 1
        while 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1
            j -= 1
        
        # Fourth option is to move to left top diagonal
        i = self.i - 1
        j = self.j - 1
        while 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
            j -= 1

        return allowed_moves
    
    def __str__(self):
        return "bishop"



