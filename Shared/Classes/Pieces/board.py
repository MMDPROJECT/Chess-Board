import sys
import os
import pygame
sys.path.append(os.getcwd() + "/Pieces")

import piece
import pawn
import rook
import knight
import bishop
import queen
import king

from typing import List


#window = pygame.

square_size = 64
colors = [(192, 192, 164),(96, 64, 32)] 
width, height = 512,512
window = pygame.display.set_mode((width, height))

#set up image of pieces

dict_images = {
    
  "black_pawn": pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_pdt60.png')),
  "black_rook": pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_rdt60.png')),
  "black_king":  pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_qdt60.png')),
  "black_knight":  pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_ndt60.png')),
  "black_queen":  pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_kdt60.png')),
  "black_bishop":  pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_bdt60.png')),
  
  "white_pawn" : pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_plt60.png')),
  "white_rook" : pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_rlt60.png')),
  "white_king" : pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_qlt60.png')),
  "white_knight" : pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_nlt60.png')),
  "white_queen" : pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_klt60.png')),
  "white_bishop" : pygame.image.load(os.path.join('/Users/macbookpro/Chess-Board/Shared/Classes/Image/Chess_blt60.png')),

  
}


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

    # This method constructs the board
    def cnstr_board(self):
        # Constructing all the pieces and placing them...
        self.place_pieces(Board.cnstr_whites())
        self.place_pieces(Board.cnstr_blacks())

    # This method places all the pieces on the chess-board
    def place_pieces(self, pieces):
        for piece in pieces:
            piece.place_on_board(self)
    
    # This method constructs all the white pieces
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

    # This method constructs all the black pieces
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
        #print(piece)
        window.blit(dict_images[f"white_{piece}"],pygame.Rect( piece_j * square_size , piece_i * square_size , square_size , square_size))
    
                
    # This methods empties the square that has been taken by a piece
    def empty_square(self, piece_i: int, piece_j: int):
        # Check to see that should be white or black
        if (piece_i + piece_j) % 2 == 0:
            self.board[piece_i][piece_j] = 0  # 0 means empty white square
            pygame.draw.rect(window, colors[0], pygame.Rect(piece_j * square_size , piece_i* square_size , square_size , square_size))
        else :
            self.board[piece_i][piece_j] = 1  # 1 means empty black square
            pygame.draw.rect(window, colors[1], pygame.Rect(piece_j * square_size , piece_i * square_size , square_size , square_size))
            
    # This method return the current piece that's on the specifed position, otherwise it return 1 or 0 which means empty squares
    def get_peice_at_pos(self, piece_i: int, piece_j: int):
        return self.board[piece_i][piece_j]
    
    # This method checks to see if there is any piece on the specifed square
    def is_piece_at_pos(self, pos_i: int, pos_j: int):
        try:
            return isinstance(self.board[pos_i][pos_j], __import__("piece").Piece)
        except IndexError:
            return True
    
    # This method check if a square is already targeted
    def is_square_targeted(self, is_attacker_white: bool, square_i: int, square_j: int):
        # A list that contains all the possible moves of the attacker team
        allowed_moves = []
        # Loop to get all the rows of the board
        for row in self.board:
            # Loop to get all the square of a row
            for square in row:
                # Check to see if there is a piece on the square
                if isinstance(square, piece.Piece):
                    # Check to see if the found piece is in the attacker team
                    if square.is_white == is_attacker_white:
                        # Adding all the possible moves of the piece to the list
                        allowed_moves.extend(square.get_allowed_poses())
        # Check to see if the square is under the attack
        if [square_i, square_j] in allowed_moves:
            return True
        
    # This method color each square
    def draw_color(self):

        for square_w in range(8):
            for square_b in range(8):
                if (square_w + square_b)% 2 == 0:
                   color = colors[1]
                else:
                   color = colors[0]
                
                square_rect = pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size)
                pygame.draw.rect(window, color, square_rect)
        
    # This method initiall the peices     
    def set_pieces(self):
        for square_w in range(8):
            for square_b in range(8):
                
                # white
                if self.board[square_w][square_b] == self.board[0][0] or self.board[square_w][square_b] == self.board[0][7]:
                    window.blit(dict_images["white_rook"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                    
                elif self.board[square_w][square_b] == self.board[0][1] or self.board[square_w][square_b] == self.board[0][6]:
                     window.blit(dict_images["white_knight"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                     
                elif self.board[square_w][square_b] == self.board[0][2] or self.board[square_w][square_b] == self.board[0][5]:
                    window.blit(dict_images["white_bishop"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                    
                elif self.board[square_w][square_b] == self.board[0][3]:
                     window.blit(dict_images["white_queen"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                     
                elif self.board[square_w][square_b] == self.board[0][4]:
                    window.blit(dict_images["white_king"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                    
                elif square_w == 1:
                     window.blit(dict_images["white_pawn"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                
                
                # black    
                elif self.board[square_w][square_b] == self.board[7][0] or self.board[square_w][square_b] == self.board[7][7]:
                     window.blit(dict_images["black_rook"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                     
                elif self.board[square_w][square_b] == self.board[7][1] or self.board[square_w][square_b] == self.board[7][6]:
                     window.blit(dict_images["black_knight"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                     
                elif self.board[square_w][square_b] == self.board[7][2] or self.board[square_w][square_b] == self.board[7][5]:
                    window.blit(dict_images["black_bishop"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                    
                elif self.board[square_w][square_b] == self.board[7][3]:
                     window.blit(dict_images["black_queen"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                     
                elif self.board[square_w][square_b] == self.board[7][4]:
                    window.blit(dict_images["black_king"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
                    
                elif square_w == 6:
                    window.blit(dict_images["black_pawn"],pygame.Rect(square_b * square_size , square_w * square_size , square_size , square_size))
        
    def find_piece(self,find_mouse):
        
        i = find_mouse[1] //64 #it requires for row part
        j = find_mouse[0] // 64 #it requires for column part    or (i,j)

        display_game = piece.Piece(i,j,True)
        
        select_mouse = pygame.mouse.get_pos()
        
        new_i = select_mouse[1] // 64
        new_j = select_mouse[0] // 64
        
        display_game.move_to_position(self, new_i , new_j)
        display_game.move_to_position(self, new_i , new_j)
        
        #if self.is_square_targeted():
            
        
        
        
        
