from __future__ import annotations

import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
import board

class King(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)
        self.has_moved = False
        self.is_checked = False
        self.is_check_mated = False

    def move_to_position(self, board: board.Board, new_i: int, new_j: int) -> None:
        super().move_to_position(board, new_i, new_j)
        self.has_moved = True

    # This method annonces all the possible moves
    def get_allowed_poses(self, board: board.Board) -> list[list]:
        allowed_moves = []
        
        # First option is to move to left top diagonal
        if 0 <= self.i - 1 <= 7 and 0 <= self.j - 1 <= 7 and not board.is_piece_at_pos(self.i - 1, self.j - 1) and not board.is_square_targeted(not self.is_white, self.i - 1, self.j - 1):
            allowed_moves.append([self.i - 1, self.j - 1])
        
        # Second option is to move up
        if 0 <= self.i - 1 <= 7 and 0 <= self.j <= 7 and not board.is_piece_at_pos(self.i - 1, self.j) and not board.is_square_targeted(not self.is_white, self.i - 1, self.j):
            allowed_moves.append([self.i - 1, self.j])

        # Third option is to move to right top diagonal
        if 0 <= self.i - 1 <= 7 and 0 <= self.j + 1 <= 7 and not board.is_piece_at_pos(self.i - 1, self.j + 1) and not board.is_square_targeted(not self.is_white, self.i - 1, self.j + 1):
            allowed_moves.append([self.i - 1, self.j + 1])
        
        # Fourth option is to move right
        if 0 <= self.i <= 7 and 0 <= self.j + 1 <= 7 and not board.is_piece_at_pos(self.i, self.j + 1) and not board.is_square_targeted(not self.is_white, self.i, self.j + 1):
            allowed_moves.append([self.i, self.j + 1])

        # Fifth option is to move to right bottom diagonal
        if 0 <= self.i + 1 <= 7 and 0 <= self.j + 1 <= 7 and not board.is_piece_at_pos(self.i + 1, self.j + 1) and not board.is_square_targeted(not self.is_white, self.i + 1, self.j + 1):
            allowed_moves.append([self.i + 1, self.j + 1])
        
        # Sixth option is to move down
        if 0 <= self.i + 1 <= 7 and 0 <= self.j <= 7 and not board.is_piece_at_pos(self.i + 1, self.j) and not board.is_square_targeted(not self.is_white, self.i + 1, self.j):
            allowed_moves.append([self.i + 1, self.j])

        # Seventh option is to move to left bottom diagonal
        if 0 <= self.i + 1 <= 7 and 0 <= self.j - 1 <= 7 and not board.is_piece_at_pos(self.i + 1, self.j - 1) and not board.is_square_targeted(not self.is_white, self.i + 1, self.j - 1):
            allowed_moves.append([self.i + 1, self.j - 1])
        
        # Eighth option is to move left
        if 0 <= self.i <= 7 and 0 <= self.j - 1 <= 7 and not board.is_piece_at_pos(self.i, self.j - 1) and not board.is_square_targeted(not self.is_white, self.i, self.j - 1):
            allowed_moves.append([self.i, self.j - 1])

        return allowed_moves
    
    # This method annonces all the possible captures
    def get_allowed_captures(self, board: board.Board) -> list[list]:
        allowed_captures = []
        
        # First option is to move to left top diagonal
        if 0 <= self.i - 1 <= 7 and 0 <= self.j - 1 <= 7 and board.is_enemy_piece_at_pos(self.i - 1, self.j - 1, self.is_white) and not board.is_square_targeted(not self.is_white, self.i - 1, self.j - 1):
            allowed_captures.append([self.i - 1, self.j - 1])
        
        # Second option is to move up
        if 0 <= self.i - 1 <= 7 and 0 <= self.j <= 7 and board.is_enemy_piece_at_pos(self.i - 1, self.j, self.is_white) and not board.is_square_targeted(not self.is_white, self.i - 1, self.j):
            allowed_captures.append([self.i - 1, self.j])

        # Third option is to move to right top diagonal
        if 0 <= self.i - 1 <= 7 and 0 <= self.j + 1 <= 7 and board.is_enemy_piece_at_pos(self.i - 1, self.j + 1, self.is_white) and not board.is_square_targeted(not self.is_white, self.i - 1, self.j + 1):
            allowed_captures.append([self.i - 1, self.j + 1])
        
        # Fourth option is to move right
        if 0 <= self.i <= 7 and 0 <= self.j + 1 <= 7 and board.is_enemy_piece_at_pos(self.i, self.j + 1, self.is_white) and not board.is_square_targeted(not self.is_white, self.i, self.j + 1):
            allowed_captures.append([self.i, self.j + 1])

        # Fifth option is to move to right bottom diagonal
        if 0 <= self.i + 1 <= 7 and 0 <= self.j + 1 <= 7 and board.is_enemy_piece_at_pos(self.i + 1, self.j + 1, self.is_white) and not board.is_square_targeted(not self.is_white, self.i + 1, self.j + 1):
            allowed_captures.append([self.i + 1, self.j + 1])
        
        # Sixth option is to move down
        if 0 <= self.i + 1 <= 7 and 0 <= self.j <= 7 and board.is_enemy_piece_at_pos(self.i + 1, self.j, self.is_white) and not board.is_square_targeted(not self.is_white, self.i + 1, self.j):
            allowed_captures.append([self.i + 1, self.j])

        # Seventh option is to move to left bottom diagonal
        if 0 <= self.i + 1 <= 7 and 0 <= self.j - 1 <= 7 and board.is_enemy_piece_at_pos(self.i + 1, self.j - 1, self.is_white) and not board.is_square_targeted(not self.is_white, self.i + 1, self.j - 1):
            allowed_captures.append([self.i + 1, self.j - 1])
        
        # Eighth option is to move left
        if 0 <= self.i <= 7 and 0 <= self.j - 1 <= 7 and board.is_enemy_piece_at_pos(self.i, self.j - 1, self.is_white) and not board.is_square_targeted(not self.is_white, self.i, self.j - 1):
            allowed_captures.append([self.i, self.j - 1])

        return allowed_captures
    
    def __str__(self):
        return "king"
    
    # # This will change 'is_checked' state of the king 
    # def set_check_status(self, is_checked: bool):
    #     self.is_checked = is_checked

    # # This will check mate the king
    # def check_mate(self):
    #     self.is_check_mated = True



