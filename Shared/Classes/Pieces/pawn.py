from __future__ import annotations

import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
import board

class Pawn(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)
        self.has_moved = False

    # This method moves a pawn to a new position
    def move_to_position(self, board: board.Board, new_i: int, new_j: int) -> None:
        super().move_to_position(board, new_i, new_j)
        self.has_moved = True
    
    # This method annonces all the possible moves
    def get_allowed_poses(self, board: board.Board) -> list[list]:        
        allowed_moves = []
        # For Whites (Top oriented team)
        if self.is_white:
            # First possiblity (if it's the first move, and there is not blocking piece on opposite, it can move two squares)
            if not self.has_moved and not board.is_piece_at_pos(self.i + 1, self.j):
                allowed_moves.append([self.i + 2, self.j])
                        
            # Second possiblity (if there is no blocking piece on opposite)
            if not board.is_piece_at_pos(self.i + 1, self.j):
                allowed_moves.append([self.i + 1, self.j])

            # # Third possiblity (if there is a piece on left bottom diagonal)
            # if board.is_piece_at_pos(self.i + 1, self.j - 1):
            #     allowed_moves.append([self.i + 1, self.j - 1])

            # # Fourth possiblity (if there is a piece on right bottom diagonal)
            # if board.is_piece_at_pos(self.i + 1, self.j + 1):
            #     allowed_moves.append([self.i + 1, self.j + 1])                
 
        # For Blacks (Bottom oriented team)    
        else:
            # First possiblity (if it's the first move, and there is not blocking piece on opposite, it can move two squares)
            if not self.has_moved and not board.is_piece_at_pos(self.i - 1, self.j):
                allowed_moves.append([self.i - 2, self.j])
                        
            # Second possiblity (if there is no blocking piece on opposite)
            if not board.is_piece_at_pos(self.i - 1, self.j):
                allowed_moves.append([self.i - 1, self.j])

            # Third possiblity (if there is a piece on left top diagonal)
            # if board.is_piece_at_pos(self.i - 1, self.j - 1):
            #     allowed_moves.append([self.i - 1, self.j - 1])

            # # Fourth possiblity (if there is a piece on right top diagonal)
            # if board.is_piece_at_pos(self.i - 1, self.j + 1):
            #     allowed_moves.append([self.i - 1, self.j + 1])  
        
        return allowed_moves
    
    def get_allowed_captures(self, board: board.Board) -> list[list]:
        allowed_captures = []
        # For Whites (Top oriented team)
        if self.is_white:
            # First possiblity (if there is a piece on left bottom diagonal)
            if board.is_enemy_piece_at_pos(self.i + 1, self.j - 1, self.is_white):
                allowed_captures.append([self.i + 1, self.j - 1])

            # Second possiblity (if there is a piece on right bottom diagonal)
            if board.is_enemy_piece_at_pos(self.i + 1, self.j + 1, self.is_white):
                allowed_captures.append([self.i + 1, self.j + 1])                
 
        # For Blacks (Bottom oriented team)    
        else:
            # First possiblity (if there is a piece on left top diagonal)
            if board.is_enemy_piece_at_pos(self.i - 1, self.j - 1, self.is_white):
                allowed_captures.append([self.i - 1, self.j - 1])

            # Second possiblity (if there is a piece on right top diagonal)
            if board.is_enemy_piece_at_pos(self.i - 1, self.j + 1, self.is_white):
                allowed_captures.append([self.i - 1, self.j + 1])  
        
        return allowed_captures

    def __str__(self):
        return "pawn"