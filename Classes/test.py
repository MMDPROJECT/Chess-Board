import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.append(os.getcwd())

from board import Board
from piece import Piece
from pawn import Pawn

board = Board()

def print_board():
    txt = "{0},{1},{2},{3},{4},{5},{6},{7}"
    for row in board.board:
        print(txt.format(*row))

piece_0 = board.get_peice_at_pos(7, 1)
piece_0.move_to_position(board, 5, 0)
print_board()

