import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
import board

from typing import List

class Queen(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool):
        super().__init__(i, j, is_white)

    # Override
    def get_allowed_poses(self, board: board.Board) -> List[List]:
        allowed_moves = []
        
        # Bishop-like moves
        # First option is to move to right top diagonal
        i = self.i - 1
        j = self.j + 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
            j += 1
        
        # Second option is to move to right bottom diagonal
        i = self.i + 1
        j = self.j + 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1
            j += 1

        # Third option is to move to left bottom diagonal
        i = self.i + 1
        j = self.j - 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1
            j -= 1
        
        # Fourth option is to move to left top diagonal
        i = self.i - 1
        j = self.j - 1
        while 0 <= i <= 8 and 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
            j -= 1


        # Rook-like moves
        # Fifth option is to move up
        i = self.i - 1
        j = self.j
        while 0 <= i <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
        
        # Sixth option is to move down
        i = self.i + 1
        j = self.j
        while 0 <= i <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1

        # Seventh option is to move right
        i = self.i
        j = self.j + 1
        while 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            j += 1
        
        # Eighth option is to move up
        i = self.i
        j = self.j - 1
        while 0 <= j <= 8 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            j -= 1

        return allowed_moves