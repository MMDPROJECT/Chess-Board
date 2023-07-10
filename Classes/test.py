import unittest
from unittest.mock import MagicMock
import sys
import os

sys.path.append(os.getcwd())

from board import Board
from piece import Piece
from pawn import Pawn

board = Board()

txt = "{0},{1},{2},{3},{4},{5},{6},{7}"
for row in board.board:
    print(txt.format(*row))

pawn_0 = board.get_peice_at_pos(1, 0)

print(pawn_0.get_allowed_poses(board))

