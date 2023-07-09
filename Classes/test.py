import sys
import os

sys.path.append(os.getcwd() + "/Classes")
sys.path.append(os.getcwd() + "/Classes/Pieces")

import Board
import Piece

# Create a new board
board = Board.Board()
# Print the updated board
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")

# Create some pieces
piece1 = Piece.Piece(2, 3, is_white=True)
piece2 = Piece.Piece(5, 6, is_white=False)

# Place pieces on the board
piece1.place_on_board(board)
# Print the updated board
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")


piece2.place_on_board(board)
# Print the updated board
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")

# Move a piece to a new position
piece1.move_to_position(board, 4, 4)
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")

# Capture an enemy piece
enemy_piece = Piece.Piece(4, 5, is_white=False)
board.place_on_board(enemy_piece.i, enemy_piece.j, enemy_piece)
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")
piece1.capture(board, 4, 5, enemy_piece)
# Print the updated board
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")

# Print the updated board
txt = "{0}              , {1}              , {2}              , {3}              , {4}              , {5}              , {6}              , {7}              \n"
for row in board.board:
    print(txt.format(*row))
print("nigga\n")
