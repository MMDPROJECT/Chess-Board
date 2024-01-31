from __future__ import annotations

import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
import board

class Rook(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)
        self.has_moved = False

    def move_to_position(self, board: board.Board, new_i: int, new_j: int) -> None:
        super().move_to_position(board, new_i, new_j)
        self.has_moved = True
    
    # This method annonces all the possible moves
    def get_allowed_poses(self, board: board.Board) -> list[list]:
        allowed_moves = []
        
        # First option is to move up
        i = self.i - 1
        j = self.j
        while 0 <= i <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i -= 1
        
        # Second option is to move down
        i = self.i + 1
        j = self.j
        while 0 <= i <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            i += 1

        # Third option is to move right
        i = self.i
        j = self.j + 1
        while 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            j += 1
        
        # Fourth option is to move up
        i = self.i
        j = self.j - 1
        while 0 <= j <= 7 and not board.is_piece_at_pos(i, j):
            allowed_moves.append([i, j])
            j -= 1

        return allowed_moves
    
    # This method annonces all the possible captures
    def get_allowed_captures(self, board: board.Board) -> list[list]:
        allowed_captures = []
        
        # First option is to move up
        i = self.i - 1
        j = self.j
        while 0 <= i <= 7:
            if board.is_enemy_piece_at_pos(i, j, self.is_white):
                allowed_captures.append([i, j])
                break
            if board.is_team_piece_at_pos(i, j, self.is_white):
                break
            i -= 1
        
        # Second option is to move down
        i = self.i + 1
        j = self.j
        while 0 <= i <= 7:
            if board.is_enemy_piece_at_pos(i, j, self.is_white):
                allowed_captures.append([i, j])
                break
            if board.is_team_piece_at_pos(i, j, self.is_white):
                break
            i += 1
            
        # Third option is to move right
        i = self.i
        j = self.j + 1
        while 0 <= j <= 7:
            if board.is_enemy_piece_at_pos(i, j, self.is_white):
                allowed_captures.append([i, j])
                break
            if board.is_team_piece_at_pos(i, j, self.is_white):
                break
            j += 1
        
        # Fourth option is to move up
        i = self.i
        j = self.j - 1
        while 0 <= j <= 7:
            if board.is_enemy_piece_at_pos(i, j, self.is_white):
                allowed_captures.append([i, j])
                break
            if board.is_team_piece_at_pos(i, j, self.is_white):
                break
            j -= 1

        return allowed_captures

    def __str__(self):
        return "rook"
        