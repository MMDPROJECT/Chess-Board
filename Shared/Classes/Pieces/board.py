from __future__ import annotations

import sys
import os
import pygame

import piece
import pawn
import rook
import knight
import bishop
import queen
import king
import team

# Size of each square
square_size = 64
# White, Black, Yellow and Red colors
colors = [(192, 192, 164), (96, 64, 32), (252, 173, 3), (255, 0, 0), (7, 3, 252)] 
# Width and Height of the board
width, height = 512,512
window = pygame.display.set_mode((width, height))

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
        self.white_team = team.Team(player_name= "Jafar", is_white= True)
        self.black_team = team.Team(player_name= "Mamad", is_white= False)
        self.is_white_turn = True
        self.is_finished = False
        self.cnstr_board()

    # --------------------------------------------------- METHODS RELATED TO CONSTRUCTING, PLACING & PICKING UP ---------------------------------------------------
    # This method constructs the board
    def cnstr_board(self) -> None:
        # Constructing all the pieces and placing them...
        self.place_pieces(self.white_team.cnstr_pieces())
        self.place_pieces(self.black_team.cnstr_pieces())

    # This method places all the pieces on the chess-board
    def place_pieces(self, pieces: list[piece.Piece]) -> None:
        for piece in pieces:
            piece.place_on_board(self)

    # This methods places a piece on the board
    def place_on_board(self, piece_i: int, piece_j: int, piece: piece.Piece) -> None:
        self.board[piece_i][piece_j] = piece
                
    # This methods empties the square that has been taken by a piece
    def empty_square(self, piece_i: int, piece_j: int) -> None:
        # Check to see that should be white or black
        if (piece_i + piece_j) % 2 == 0:
            self.board[piece_i][piece_j] = 0  # 0 means empty white square
        else :
            self.board[piece_i][piece_j] = 1  # 1 means empty black square
        
    # This method return the current piece that's on the specifed position, otherwise it return 1 or 0 which means empty squares
    def get_peice_at_pos(self, piece_i: int, piece_j: int) -> piece.Piece:
        return self.board[piece_i][piece_j]
    
    # This methods finds king of an specific team 
    def find_king(self, is_king_white: bool) -> king.King:
        for row in self.board:
            for square in row:
                # Check if it's a king
                if isinstance(square, king.King):
                    # Check if it's color is the same thing
                    if square.is_white == is_king_white:
                        return square
    
    # --------------------------------------------------- METHODS RELATED TO CHECKING ---------------------------------------------------
    # This method checks to see if there is any piece on the specifed square
    def is_piece_at_pos(self, pos_i: int, pos_j: int) -> bool:
        return isinstance(self.board[pos_i][pos_j], piece.Piece)

    # This method checks to see if there is an enemy piece at the specified square 
    def is_enemy_piece_at_pos(self, pos_i: int, pos_j: int, is_attacker_white: bool) -> bool:
        obj_at_pos = self.board[pos_i][pos_j]
        if isinstance(obj_at_pos, piece.Piece) and obj_at_pos.is_white != is_attacker_white:
            return True
        return False
    
    # This method checks to see if there is an team piece at the specifed square
    def is_team_piece_at_pos(self, pos_i: int, pos_j: int, is_white: bool) -> bool:
        obj_at_pos = self.board[pos_i][pos_j]
        if isinstance(obj_at_pos, piece.Piece) and obj_at_pos.is_white == is_white:
            return True
        return False

    # This method checks if a square is already targeted
    def is_square_targeted(self, is_attacker_white: bool, square_i: int, square_j: int) -> bool:
        # A list that contains all the possible moves of the attacker team
        allowed_moves_and_captures = []
        # Loop to get all the rows of the board
        for row in self.board:
            # Loop to get all the square of a row
            for square in row:
                # Check to see if there is a piece on the square
                if isinstance(square, piece.Piece) and not isinstance(square, king.King):
                    # Check to see if the found piece is in the attacker team
                    if square.is_white == is_attacker_white:
                        # Adding all the possible moves of the piece to the list
                        allowed_moves_and_captures.extend(square.get_allowed_poses(self))
                        allowed_moves_and_captures.extend(square.get_allowed_captures(self))
        # Check to see if the square is under the attack
        if [square_i, square_j] in allowed_moves_and_captures:
            return True
        else:
            return False
        
    # --------------------------------------------------- METHODS RELATED TO DRAWING ---------------------------------------------------
    # This method draws the raw-empty board on the screen
    def draw_empty_board(self) -> None:
        for i in range(8):
            for j in range(8):
                if (i + j) % 2 == 0:
                   color = colors[1]
                else:
                   color = colors[0]
                
                square_rect = pygame.Rect(j * square_size, i * square_size, square_size, square_size)
                pygame.draw.rect(window, color, square_rect)

    # This method draws all the pieces on the empty board
    def draw_pieces_on_board(self) -> None: 
        for i in range(8):
            for j in range(8):
                current_piece = self.board[i][j]
                
                # Checking if it's piece
                if isinstance(current_piece, piece.Piece):
                    window.blit(current_piece.image, pygame.Rect(j * square_size, i * square_size, square_size, square_size))

    def draw_allowed_moves(self, allowed_moves: list[list]) -> None:
        for l in allowed_moves:
            i, j = l[0], l[1]
            square_rect = pygame.Rect(j * square_size, i * square_size, square_size, square_size)
            pygame.draw.rect(window, colors[2], square_rect, 5)
            pygame.display.update()

    def draw_allowed_captures(self, allowed_captures: list[list]) -> None:
        for l in allowed_captures:
            i, j = l[0], l[1]
            square_rect = pygame.Rect(j * square_size, i * square_size, square_size, square_size)
            pygame.draw.rect(window, colors[3], square_rect, 5)
            pygame.display.update()

    def draw_allowed_castle_moves(self, allowed_castle_moves: list[list]) -> None:
        for l in allowed_castle_moves:
            i, j = l[0], l[1]
            square_rect = pygame.Rect(j * square_size, i * square_size, square_size, square_size)
            pygame.draw.rect(window, colors[4], square_rect, 5)
            pygame.display.update()
    

    
    # --------------------------------------------------- METHODS RELATED TO PROCESSING THE GAME ---------------------------------------------------             
    def switch_turn(self):
        if self.is_white_turn:
            self.is_white_turn = False
        else:
            self.is_white_turn = True
        
    def process_player_choice(self, find_mouse) -> None:
        
        i = find_mouse[1] // 64 #it requires for row part
        j = find_mouse[0] // 64 #it requires for column part    or (i,j)
        
        # Getting the selected square
        selected_piece = self.get_peice_at_pos(i, j)
       
        # Check if it's a piece
        if isinstance(selected_piece, piece.Piece):
            playing_team = None
            if selected_piece.is_white:
                playing_team = self.white_team
            else:
                playing_team = self.black_team

            # Check if it has premission to move the piece
            if self.is_white_turn == selected_piece.is_white:
                # Check if white is checked and intend to move a move other than it's king
                if self.is_white_turn and self.white_team.is_checked and not isinstance(selected_piece, king.King):
                    return
                # Check if black is checked and intend to move a move other than it's king
                elif not self.is_white_turn and self.black_team.is_checked and not isinstance(selected_piece, king.King):
                    return
                
                # Otherwise run this section down below 

                # Calculating all the possible moves and captures
                allowed_poses = selected_piece.get_allowed_poses(self)
                allowed_captures = selected_piece.get_allowed_captures(self)
                allowed_castle_moves = []

                if isinstance(selected_piece, king.King):
                    allowed_castle_moves = playing_team.get_available_castle_moves(self)

                # Checking if it's not empty
                if allowed_captures != [] or allowed_poses != [] or allowed_castle_moves != []:            
                    # Drawing all the possible moves for the piece
                    self.draw_allowed_moves(allowed_poses)
                    # Drawing all the possible captures for the piece
                    self.draw_allowed_captures(allowed_captures)
                    # Drawing all the possible castle moves for the king (if and only if it's selected)
                    self.draw_allowed_castle_moves(allowed_castle_moves)
                    
                    has_selected_any_square = False

                    while not has_selected_any_square:
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                select_mouse = pygame.mouse.get_pos()

                                new_i = select_mouse[1] // 64
                                new_j = select_mouse[0] // 64
                                
                                if selected_piece.is_allowed_pos(self, new_i, new_j):
                                    selected_piece.move_to_position(self, new_i, new_j)
                                    has_selected_any_square = True      
                                elif selected_piece.is_allowed_capture(self, new_i, new_j):
                                    selected_piece.capture(self, new_i, new_j, self.get_peice_at_pos(new_i, new_j))
                                    has_selected_any_square = True
                                elif [new_i, new_j] in allowed_castle_moves:
                                    if new_j >= playing_team.king.j:
                                        playing_team.do_castle_move(True, self)
                                    else:
                                        playing_team.do_castle_move(False, self)
                                    has_selected_any_square = True

                    # Check if the white king is targeted
                    if self.white_team.is_king_checked(self):
                        self.white_team.set_check_status(is_checked= True)
                        if self.white_team.is_king_check_mated(self):
                            self.white_team.check_mate()
                            self.is_finished = True
                    
                    # Check if the black king is targeted
                    if self.black_team.is_king_checked(self):
                        self.black_team.set_check_status(is_checked= True)
                        if self.black_team.is_king_check_mated(self):
                            self.black_team.check_mate()
                            self.is_finished = True
                    
                    # Switch turns
                    self.switch_turn()
