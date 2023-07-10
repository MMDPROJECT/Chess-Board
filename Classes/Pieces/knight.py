import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
import board

from typing import List

class Knight(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool):
        super().__init__(i, j, is_white)

    # Override
    def get_allowed_poses(self, board: board.Board) -> List[List]:
        allowed_moves = []
        
        # First option is to move two squares up and then one square left
        i = self.i - 2
        j = self.j - 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 2
            j -= 1
        
        # Second option is to move two squares up and then one square right
        i = self.i - 2
        j = self.j + 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 2
            j += 1

        # Third option is to move two square right and then one square up
        i = self.i - 1
        j = self.j + 2
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
            j += 2

        # Fourth option is to move two square right and then one square down
        i = self.i + 1
        j = self.j + 2
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1
            j += 2

        # Fifth option is to move two square down and then one square right
        i = self.i + 2
        j = self.j + 1 
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 2
            j += 1

        # Sixth option is to move two square down and then one square left
        i = self.i + 2
        j = self.j - 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 2
            j -= 1

        # Seventh option is to move two square left and then one square down
        i = self.i + 1
        j = self.j - 2
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1
            j -= 2

        # Eighth option is to move two square left and then one square up
        i = self.i - 1
        j = self.j - 2
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
            j -= 2



        return allowed_moves



