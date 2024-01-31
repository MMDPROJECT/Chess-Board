from __future__ import annotations

import sys
import os
# Adding the path of parent directory (Classes) to the paths
sys.path.append(os.path.abspath(os.path.join(os.getcwd(), os.pardir)))

import piece
import board
import rook
import knight
import bishop
import queen
import team

import threading

class Pawn(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool, image):
        super().__init__(i, j, is_white, image)
        self.has_moved = False
        self.mashit = ""

    def give_em(self) -> str:
        self.mashit = input()

    # This method moves a pawn to a new position
    def move_to_position(self, board: board.Board, new_i: int, new_j: int) -> None:
        super().move_to_position(board, new_i, new_j)
        self.has_moved = True

        if (self.is_white == True and self.i == 7) or (self.is_white == False and self.i == 0):
            # print("""Please choose one of these options:
            #           1. Rook
            #           2. Knight
            #           3. Queen
            #           4. Bishop""")
            piece_to_promote_to = "queen" # This should be prompt you know? :)
            self.promote(piece_to_promote_to, board)

    
    
    
    # This method annonces all the possible moves
    def get_allowed_poses(self, board: board.Board) -> list[list]:        
        allowed_moves = []
        # For Whites (Top oriented team)
        if self.is_white:
            # First possiblity (if it's the first move, and there is not blocking piece on opposite, it can move two squares)
            if 0 <= self.i + 2 <= 7 and 0 <= self.j <= 7 and not self.has_moved and not board.is_piece_at_pos(self.i + 2, self.j):
                allowed_moves.append([self.i + 2, self.j])
                        
            # Second possiblity (if there is no blocking piece on opposite)
            if 0 <= self.i + 1 <= 7 and 0 <= self.j <= 7 and not board.is_piece_at_pos(self.i + 1, self.j):
                allowed_moves.append([self.i + 1, self.j])            
 
        # For Blacks (Bottom oriented team)    
        else:
            # First possiblity (if it's the first move, and there is not blocking piece on opposite, it can move two squares)
            if 0 <= self.i - 2 <= 7 and 0 <= self.j <= 7 and not self.has_moved and not board.is_piece_at_pos(self.i - 2, self.j):
                allowed_moves.append([self.i - 2, self.j])
                        
            # Second possiblity (if there is no blocking piece on opposite)
            if 0 <= self.i - 1 <= 7 and 0 <= self.j <= 7 and not board.is_piece_at_pos(self.i - 1, self.j):
                allowed_moves.append([self.i - 1, self.j])

        
        return allowed_moves
    
    def get_allowed_captures(self, board: board.Board) -> list[list]:
        allowed_captures = []
        # For Whites (Top oriented team)
        if self.is_white:
            # First possiblity (if there is a piece on left bottom diagonal)
            if 0 <= self.i + 1 <= 7 and 0 <= self.j - 1 <= 7 and board.is_enemy_piece_at_pos(self.i + 1, self.j - 1, self.is_white):
                allowed_captures.append([self.i + 1, self.j - 1])

            # Second possiblity (if there is a piece on right bottom diagonal)
            if 0 <= self.i + 1 <= 7 and 0 <= self.j + 1 <= 7 and board.is_enemy_piece_at_pos(self.i + 1, self.j + 1, self.is_white):
                allowed_captures.append([self.i + 1, self.j + 1])                
 
        # For Blacks (Bottom oriented team)    
        else:
            # First possiblity (if there is a piece on left top diagonal)
            if 0 <= self.i - 1 <= 7 and 0 <= self.j - 1 <= 7 and board.is_enemy_piece_at_pos(self.i - 1, self.j - 1, self.is_white):
                allowed_captures.append([self.i - 1, self.j - 1])

            # Second possiblity (if there is a piece on right top diagonal)
            if 0 <= self.i - 1 <= 7 and 0 <= self.j + 1 <= 7 and board.is_enemy_piece_at_pos(self.i - 1, self.j + 1, self.is_white):
                allowed_captures.append([self.i - 1, self.j + 1])  
        
        return allowed_captures
    
    def promote(self, piece_to_promote_to: str, board: board.Board):
        match piece_to_promote_to:
            case "rook":
                if self.is_white:
                    self = rook.Rook(self.i, self.j, self.is_white, team.dict_images["white_rook"])
                else:
                    self = rook.Rook(self.i, self.j, self.is_white, team.dict_images["black_rook"])

            case "knight":
                if self.is_white:
                    self = knight.Knight(self.i, self.j, self.is_white, team.dict_images["white_knight"])
                else:
                    self = knight.Knight(self.i, self.j, self.is_white, team.dict_images["black_knight"])

            case "bishop":
                if self.is_white:
                    self = bishop.Bishop(self.i, self.j, self.is_white, team.dict_images["white_bishop"])
                else:
                    self = bishop.Bishop(self.i, self.j, self.is_white, team.dict_images["black_bishop"])

            case "queen":
                if self.is_white:
                    self = queen.Queen(self.i, self.j, self.is_white, team.dict_images["white_queen"])
                else:
                    self = queen.Queen(self.i, self.j, self.is_white, team.dict_images["black_queen"])

            case _:
                raise Exception("Am i joke to you?")
            
        board.place_on_board(self.i, self.j, self)

    def __str__(self):
        return "pawn"