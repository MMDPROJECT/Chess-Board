import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece

class Knight(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)

    # This method annonces all the possible moves
    def get_allowed_poses(self, board) -> list[list]:
        allowed_moves = []
        
        # First option is to move two squares up and then one square left
        i = self.i - 2
        j = self.j - 1
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
        
        # Second option is to move two squares up and then one square right
        i = self.i - 2
        j = self.j + 1
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        # Third option is to move two square right and then one square up
        i = self.i - 1
        j = self.j + 2
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        # Fourth option is to move two square right and then one square down
        i = self.i + 1
        j = self.j + 2
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        # Fifth option is to move two square down and then one square right
        i = self.i + 2
        j = self.j + 1 
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        # Sixth option is to move two square down and then one square left
        i = self.i + 2
        j = self.j - 1
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        # Seventh option is to move two square left and then one square down
        i = self.i + 1
        j = self.j - 2
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        # Eighth option is to move two square left and then one square up
        i = self.i - 1
        j = self.j - 2
        if 0 <= i <= 7 and 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])

        return allowed_moves


    def __str__(self):
        return "knight"


