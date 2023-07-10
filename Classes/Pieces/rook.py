from typing import List
import piece

class Rook(piece.Piece):
    def __init__(self, i: int, j: int, is_white: bool):
        super().__init__(i, j, is_white)
    
    # Override
    def get_allowed_poses(self) -> List[List]:
        allowed_moves = []
        
        # First options are to move up
        i = self.i - 1
        j = self.j
        while 0 <= i <= 8:
            allowed_moves.append([i, j])
            i -= 1
        
        # Second options are to move down
        i = self.i + 1
        j = self.j
        while 0 <= i <= 8:
            allowed_moves.append([i, j])
            i += 1

        # First options are to move right
        i = self.i
        j = self.j + 1
        while 0 <= j <= 8:
            allowed_moves.append([i, j])
            j += 1
        
        # First options are to move up
        i = self.i
        j = self.j - 1
        while 0 <= j <= 8:
            allowed_moves.append([i, j])
            j -= 1

        return allowed_moves
        