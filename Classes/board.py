import sys
import os

sys.path.append(os.getcwd() + "/Pieces")

import piece
import pawn
import rook
import knight
import bishop
import queen
import king

from typing import List

class Board:
    def __init__(self):
        self.board = [
            # 0 means empty white square
            # 1 means empty black square
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0],
            [0,1,0,1,0,1,0,1],
            [1,0,1,0,1,0,1,0]
        ]
        self.cnstr_board()

    def cnstr_board(self):
        self.place_whites(Board.cnstr_whites())
        self.place_blacks(Board.cnstr_blacks())

    def place_whites(self, white_pieces):
        for piece in white_pieces:
            piece.place_on_board(self)
    
    @staticmethod
    def cnstr_whites() -> List:
        white_pieces = []
        # Pawns
        pawn_white_0 = pawn.Pawn(1, 0, True)
        pawn_white_1 = pawn.Pawn(1, 1, True)
        pawn_white_2 = pawn.Pawn(1, 2, True)
        pawn_white_3 = pawn.Pawn(1, 3, True)
        pawn_white_4 = pawn.Pawn(1, 4, True)
        pawn_white_5 = pawn.Pawn(1, 5, True)
        pawn_white_6 = pawn.Pawn(1, 6, True)
        pawn_white_7 = pawn.Pawn(1, 7, True)
        # Rooks
        rook_white_0 = rook.Rook(0, 0, True)
        rook_white_1 = rook.Rook(0, 7, True)
        # Knights
        knight_white_0 = knight.Knight(0, 1, True)
        knight_white_1 = knight.Knight(0, 6, True)
        # Bishops
        bishop_white_0 = bishop.Bishop(0, 2, True)
        bishop_white_1 = bishop.Bishop(0, 5, True)
        # Royal familiy
        queen_white = queen.Queen(0, 3, True)
        king_white = king.King(0, 4, True)

        white_pieces.append(pawn_white_0)
        white_pieces.append(pawn_white_1)
        white_pieces.append(pawn_white_2)
        white_pieces.append(pawn_white_3)
        white_pieces.append(pawn_white_4)
        white_pieces.append(pawn_white_5)
        white_pieces.append(pawn_white_6)
        white_pieces.append(pawn_white_7)

        white_pieces.append(rook_white_0)
        white_pieces.append(rook_white_1)

        white_pieces.append(knight_white_0)
        white_pieces.append(knight_white_1)

        white_pieces.append(bishop_white_0)
        white_pieces.append(bishop_white_1)

        white_pieces.append(queen_white)
        white_pieces.append(king_white)

        return white_pieces

    def place_blacks(self, black_pieces):
        for piece in black_pieces:
            piece.place_on_board(self)

    @staticmethod
    def cnstr_blacks() -> List:
        black_pieces = []
        # Pawns
        pawn_black_0 = pawn.Pawn(6, 0, False)
        pawn_black_1 = pawn.Pawn(6, 1, False)
        pawn_black_2 = pawn.Pawn(6, 2, False)
        pawn_black_3 = pawn.Pawn(6, 3, False)
        pawn_black_4 = pawn.Pawn(6, 4, False)
        pawn_black_5 = pawn.Pawn(6, 5, False)
        pawn_black_6 = pawn.Pawn(6, 6, False)
        pawn_black_7 = pawn.Pawn(6, 7, False)
        # Rooks
        rook_black_0 = rook.Rook(7, 0, False)
        rook_black_1 = rook.Rook(7, 7, False)
        # Knights
        knight_black_0 = knight.Knight(7, 1, False)
        knight_black_1 = knight.Knight(7, 6, False)
        # Bishops
        bishop_black_0 = bishop.Bishop(7, 2, False)
        bishop_black_1 = bishop.Bishop(7, 5, False)
        # Royal familiy
        queen_black = queen.Queen(7, 3, False)
        king_black = king.King(7, 4, False)

        black_pieces.append(pawn_black_0)
        black_pieces.append(pawn_black_1)
        black_pieces.append(pawn_black_2)
        black_pieces.append(pawn_black_3)
        black_pieces.append(pawn_black_4)
        black_pieces.append(pawn_black_5)
        black_pieces.append(pawn_black_6)
        black_pieces.append(pawn_black_7)

        black_pieces.append(rook_black_0)
        black_pieces.append(rook_black_1)

        black_pieces.append(knight_black_0)
        black_pieces.append(knight_black_1)

        black_pieces.append(bishop_black_0)
        black_pieces.append(bishop_black_1)

        black_pieces.append(queen_black)
        black_pieces.append(king_black)

        return black_pieces

    # This methods places a piece on the board
    def place_on_board(self, piece_i : int, piece_j : int, piece):
        self.board[piece_i][piece_j] = piece
    
    # This methods empties the square that has been taken by a piece
    def empty_square(self, piece_i: int, piece_j: int):
        # Check to see that should be white or black
        if piece_i + piece_j % 2 == 0:
            self.board[piece_i][piece_j] = 0  # 0 means empty white square
        else :
            self.board[piece_i][piece_j] = 1  # 1 means empty black square

    # This method return the current piece that's on the specifed position, otherwise it return 1 or 0 which means empty squares
    def get_peice_at_pos(self, piece_i: int, piece_j: int):
        return self.board[piece_i][piece_j]
    
    # This method checks to see if there is any piece on the specifed square
    def is_piece_at_pos(self, pos_i: int, pos_j: int):
        try:
            return isinstance(self.board[pos_i][pos_j], __import__("piece").Piece)
        except IndexError:
            return True
    
