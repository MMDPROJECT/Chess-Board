from __future__ import annotations

import pygame
import os

import pawn
import rook
import knight
import bishop
import queen
import king
import board

dict_images = {
  "black_pawn": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_pdt60.png')),
  "black_rook": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_rdt60.png')),
  "black_king":  pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_kdt60.png')),
  "black_knight":  pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_ndt60.png')),
  "black_queen":  pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_qdt60.png')),
  "black_bishop":  pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_bdt60.png')),
  
  "white_pawn": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_plt60.png')),
  "white_rook": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_rlt60.png')),
  "white_king": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_klt60.png')),
  "white_knight": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_nlt60.png')),
  "white_queen": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_qlt60.png')),
  "white_bishop": pygame.image.load(os.path.join(os.getcwd() + '/Shared/Classes/Image/Chess_blt60.png'))
}

class Team:
    def __init__(self, player_name: str, is_white: bool) -> None:
        self.player_name = player_name
        self.is_white = is_white
        self.is_checked = False
        self.is_check_mated = False

    # --------------------------------------------------- METHODS RELATED TO CONSTRUCTING ---------------------------------------------------
    # Constructs all the pieces of the team and return them
    def cnstr_pieces(self) -> list:
        pieces = []
        if self.is_white:
            # Pawns
            pawn_white_0 = pawn.Pawn(1, 0, True, dict_images["white_pawn"])
            pawn_white_1 = pawn.Pawn(1, 1, True, dict_images["white_pawn"])
            pawn_white_2 = pawn.Pawn(1, 2, True, dict_images["white_pawn"])
            pawn_white_3 = pawn.Pawn(1, 3, True, dict_images["white_pawn"])
            pawn_white_4 = pawn.Pawn(1, 4, True, dict_images["white_pawn"])
            pawn_white_5 = pawn.Pawn(1, 5, True, dict_images["white_pawn"])
            pawn_white_6 = pawn.Pawn(1, 6, True, dict_images["white_pawn"])
            pawn_white_7 = pawn.Pawn(1, 7, True, dict_images["white_pawn"])
            # Rooks
            rook_white_0 = rook.Rook(0, 0, True, dict_images["white_rook"])
            rook_white_1 = rook.Rook(0, 7, True, dict_images["white_rook"])
            # Knights
            knight_white_0 = knight.Knight(0, 1, True, dict_images["white_knight"])
            knight_white_1 = knight.Knight(0, 6, True, dict_images["white_knight"])
            # Bishops
            bishop_white_0 = bishop.Bishop(0, 2, True, dict_images["white_bishop"])
            bishop_white_1 = bishop.Bishop(0, 5, True, dict_images["white_bishop"])
            # Royal familiy
            queen_white = queen.Queen(0, 3, True, dict_images["white_queen"])
            king_white = king.King(0, 4, True, dict_images["white_king"])

            # Setting some special pieces 
            self.king = king_white
            ''' Here right rook is assume to be the rook that is on the right hand side of the king,
            when the king is looking towards the center of the chess from based on how it's team is oriented on the board, the same is true for the left rook '''
            self.r_rook = rook_white_0
            self.l_rook = rook_white_1

            pieces.append(pawn_white_0)
            pieces.append(pawn_white_1)
            pieces.append(pawn_white_2)
            pieces.append(pawn_white_3)
            pieces.append(pawn_white_4)
            pieces.append(pawn_white_5)
            pieces.append(pawn_white_6)
            pieces.append(pawn_white_7)

            pieces.append(rook_white_0)
            pieces.append(rook_white_1)

            pieces.append(knight_white_0)
            pieces.append(knight_white_1)

            pieces.append(bishop_white_0)
            pieces.append(bishop_white_1)

            pieces.append(queen_white)
            pieces.append(king_white)

        else:
            # Pawns
            pawn_black_0 = pawn.Pawn(6, 0, False, dict_images["black_pawn"])
            pawn_black_1 = pawn.Pawn(6, 1, False, dict_images["black_pawn"])
            pawn_black_2 = pawn.Pawn(6, 2, False, dict_images["black_pawn"])
            pawn_black_3 = pawn.Pawn(6, 3, False, dict_images["black_pawn"])
            pawn_black_4 = pawn.Pawn(6, 4, False, dict_images["black_pawn"])
            pawn_black_5 = pawn.Pawn(6, 5, False, dict_images["black_pawn"])
            pawn_black_6 = pawn.Pawn(6, 6, False, dict_images["black_pawn"])
            pawn_black_7 = pawn.Pawn(6, 7, False, dict_images["black_pawn"])
            # Rooks
            rook_black_0 = rook.Rook(7, 0, False, dict_images["black_rook"])
            rook_black_1 = rook.Rook(7, 7, False, dict_images["black_rook"])
            # Knights
            knight_black_0 = knight.Knight(7, 1, False, dict_images["black_knight"])
            knight_black_1 = knight.Knight(7, 6, False, dict_images["black_knight"])
            # Bishops
            bishop_black_0 = bishop.Bishop(7, 2, False, dict_images["black_bishop"])
            bishop_black_1 = bishop.Bishop(7, 5, False, dict_images["black_bishop"])
            # Royal familiy
            queen_black = queen.Queen(7, 3, False, dict_images["black_queen"])
            king_black = king.King(7, 4, False, dict_images["black_king"])

            # Setting the some special pieces 
            self.king = king_black
            ''' Here right rook is assume to be the rook that is on the right hand side of the king,
            when the king is looking towards the center of the chess from based on how it's team is oriented on the board, the same is true for the left rook '''
            self.r_rook = rook_black_1
            self.l_rook = rook_black_0

            pieces.append(pawn_black_0)
            pieces.append(pawn_black_1)
            pieces.append(pawn_black_2)
            pieces.append(pawn_black_3)
            pieces.append(pawn_black_4)
            pieces.append(pawn_black_5)
            pieces.append(pawn_black_6)
            pieces.append(pawn_black_7)

            pieces.append(rook_black_0)
            pieces.append(rook_black_1)

            pieces.append(knight_black_0)
            pieces.append(knight_black_1)

            pieces.append(bishop_black_0)
            pieces.append(bishop_black_1)

            pieces.append(queen_black)
            pieces.append(king_black)

        return pieces 
    
    # --------------------------------------------------- METHODS RELATED TO CHECKING ---------------------------------------------------
    def is_king_checked(self, board: board.Board) -> bool:
        return board.is_square_targeted(not self.is_white, self.king.i, self.king.j)
    
    def is_king_check_mated(self, board: board.Board) -> bool:
        # Checking all 8 directions (top left, top, top right, right, bottom right, bottom, bottom left, left)
        # Top left
        if 0 <= self.king.i - 1 <= 7 and 0 <= self.king.j - 1 <= 7 and not board.is_piece_at_pos(self.king.i - 1, self.king.j - 1) and not board.is_square_targeted(not self.is_white, self.king.i - 1, self.king.j - 1):
            return False
        
        # Top
        elif 0 <= self.king.i - 1 <= 7 and 0 <= self.king.j <= 7 and not board.is_piece_at_pos(self.king.i - 1, self.king.j) and not board.is_square_targeted(not self.is_white, self.king.i - 1, self.king.j):
            return False
        
        # Top right
        elif 0 <= self.king.i - 1 <= 7 and 0 <= self.king.j + 1 <= 7 and not board.is_piece_at_pos(self.king.i - 1, self.king.j + 1) and not board.is_square_targeted(not self.is_white, self.king.i - 1, self.king.j + 1):
            return False
        
        # Right
        elif 0 <= self.king.i <= 7 and 0 <= self.king.j + 1 <= 7 and not board.is_piece_at_pos(self.king.i, self.king.j + 1) and not board.is_square_targeted(not self.is_white, self.king.i, self.king.j + 1):
            return False
        
        # Bottom right
        elif 0 <= self.king.i + 1 <= 7 and 0 <= self.king.j + 1 <= 7 and not board.is_piece_at_pos(self.king.i + 1, self.king.j + 1) and not board.is_square_targeted(not self.is_white, self.king.i + 1, self.king.j + 1):
            return False
        
        # Bottom
        elif 0 <= self.king.i + 1 <= 7 and 0 <= self.king.j <= 7 and not board.is_piece_at_pos(self.king.i + 1, self.king.j) and not board.is_square_targeted(not self.is_white, self.king.i + 1, self.king.j):
            return False
        
        # Bottom left
        elif 0 <= self.king.i + 1 <= 7 and 0 <= self.king.j - 1 <= 7 and not board.is_piece_at_pos(self.king.i + 1, self.king.j - 1) and not board.is_square_targeted(not self.is_white, self.king.i + 1, self.king.j - 1):
            return False

        # Left
        elif 0 <= self.king.i <= 7 and 0 <= self.king.j - 1 <= 7 and not board.is_piece_at_pos(self.king.i, self.king.j - 1) and not board.is_square_targeted(not self.is_white, self.king.i, self.king.j - 1):
            return False
        
        return True

    def get_available_castle_moves(self, board: board.Board) -> list[list]:
        available_castle_moves = []

        # Checking for right castle move
        if not self.r_rook.has_moved and not self.king.has_moved:
            # If it's the white team doing the castle move:
            if self.is_white:
                # Checking to make sure all the squares are empty in between
                if not board.is_piece_at_pos(self.king.i, self.king.j - 1) and not board.is_piece_at_pos(self.king.i, self.king.j - 2) and not board.is_piece_at_pos(self.king.i, self.king.j - 3):
                    # Checking to see if the king is checked
                    if not self.is_checked:
                        # Check to make sure none of the squares is targeted by enemy pieces
                        if not board.is_square_targeted(not self.is_white, self.king.i, self.king.j - 1) and not board.is_square_targeted(not self.is_white, self.king.i, self.king.j - 2):
                            available_castle_moves.append([self.king.i, self.king.j - 2])

            # Otherwise it's the black team doing the castle move:
            else:
                # Checking to make sure all the squares are empty in between
                if not board.is_piece_at_pos(self.king.i, self.king.j + 1) and not board.is_piece_at_pos(self.king.i, self.king.j + 2):
                    # Checking to see if the king is checked
                    if not self.is_checked:
                        # Check to make sure none of the squares is targeted by enemy pieces
                        if not board.is_square_targeted(not self.is_white, self.king.i, self.king.j + 1) and not board.is_square_targeted(not self.is_white, self.king.i, self.king.j + 2):
                            available_castle_moves.append([self.king.i, self.king.j + 2])

        # Checking for left castle move
        if not self.l_rook.has_moved and not self.king.has_moved:
            # If it's the white team doing the castle move:
            if self.is_white:
                # Checking to make sure all the squares are empty in between
                if not board.is_piece_at_pos(self.king.i, self.king.j + 1) and not board.is_piece_at_pos(self.king.i, self.king.j + 2):
                    # Checking to see if the king is checked
                    if not self.is_checked:
                        # Check to make sure none of the squares is targeted by enemy pieces
                        if not board.is_square_targeted(not self.is_white, self.king.i, self.king.j + 1) and not board.is_square_targeted(not self.is_white, self.king.i, self.king.j + 2):
                            available_castle_moves.append([self.king.i, self.king.j + 2])

            # Otherwise it's the black team doing the castle move:
            else:
                # Checking to make sure all the squares are empty in between
                if not board.is_piece_at_pos(self.king.i, self.king.j - 1) and not board.is_piece_at_pos(self.king.i, self.king.j - 2) and not board.is_piece_at_pos(self.king.i, self.king.j - 3):
                    # Checking to see if the king is checked
                    if not self.is_checked:
                        # Check to make sure none of the squares is targeted by enemy pieces
                        if not board.is_square_targeted(not self.is_white, self.king.i, self.king.j - 1) and not board.is_square_targeted(not self.is_white, self.king.i, self.king.j - 2):
                            available_castle_moves.append([self.king.i, self.king.j - 2])

        return available_castle_moves

    def do_castle_move(self, is_right_castle_move: bool, board: board.Board):
        # if it's a right castle move
        if is_right_castle_move:
            print("right castle ", end= "")
            # if the moving team is white
            if self.is_white:
                print("for the white team")
                self.king.move_to_position(board, self.king.i, self.king.j - 2)
                self.r_rook.move_to_position(board, self.r_rook.i, self.r_rook.j + 3)
            # otherwise the moving team is black
            else:
                print("for the black team")
                self.king.move_to_position(board, self.king.i, self.king.j + 2)
                self.r_rook.move_to_position(board, self.r_rook.i, self.r_rook.j - 2)
        # otherwise it's a left castle move
        else:
            print("left castle ", end= "")
            # if the moving team is white
            if self.is_white:
                print("for the white team")
                print(f"initial poses {(self.king.i)}, {(self.king.j)}, {(self.l_rook.i)}, {(self.l_rook.j)}, {(self.r_rook.i)}, {(self.r_rook.j)}")
                self.king.move_to_position(board, self.king.i, self.king.j + 2)
                self.l_rook.move_to_position(board, self.l_rook.i, self.l_rook.j - 2)
                print(f"final poses {(self.king.i)}, {(self.king.j)}, {(self.l_rook.i)}, {(self.l_rook.j)}, {(self.r_rook.i)}, {(self.r_rook.j)}")
            # otherwise the moving team is black
            else:
                print("for the black team")
                self.king.move_to_position(board, self.king.i, self.king.j - 2)
                self.l_rook.move_to_position(board, self.l_rook.i, self.l_rook.j + 3)

    # This will change 'is_checked' state of the team
    def set_check_status(self, is_checked: bool) -> None:
        self.is_checked = is_checked

    # This will check mate the king
    def check_mate(self):
        self.is_check_mated = True