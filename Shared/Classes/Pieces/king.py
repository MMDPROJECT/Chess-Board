import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece

class King(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)
        self.is_checked = False
        self.is_check_mated = False

    # This method annonces all the possible moves
    def get_allowed_poses(self, board) -> list[list]:
        allowed_moves = []
        
        # First option is to move to left top diagonal
        if not board.is_piece_at_pos(self.i - 1, self.j - 1):
            allowed_moves.append([self.i - 1, self.j - 1])
        
        # Second option is to move up
        if not board.is_piece_at_pos(self.i - 1, self.j):
            allowed_moves.append([self.i - 1, self.j])

        # Third option is to move to right top diagonal
        if not board.is_piece_at_pos(self.i - 1, self.j + 1):
            allowed_moves.append([self.i - 1, self.j + 1])
        
        # Fourth option is to move right
        if not board.is_piece_at_pos(self.i, self.j + 1):
            allowed_moves.append([self.i, self.j + 1])

        # Fifth option is to move to right bottom diagonal
        if not board.is_piece_at_pos(self.i + 1, self.j + 1):
            allowed_moves.append([self.i + 1, self.j + 1])
        
        # Sixth option is to move down
        if not board.is_piece_at_pos(self.i + 1, self.j):
            allowed_moves.append([self.i + 1, self.j])

        # Seventh option is to move to left bottom diagonal
        if not board.is_piece_at_pos(self.i + 1, self.j - 1):
            allowed_moves.append([self.i + 1, self.j - 1])
        
        # Eighth option is to move left
        if not board.is_piece_at_pos(self.i, self.j - 1):
            allowed_moves.append([self.i, self.j - 1])

        return allowed_moves
    
    def __str__(self):
        return "king"
    
    # This will change 'is_checked' state of the king 
    def set_check(self, is_checked: bool):
        self.is_checked = is_checked

    # This will check mate the king
    def check_mate(self):
        self.is_check_mated = True



