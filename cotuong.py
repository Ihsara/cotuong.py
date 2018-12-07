import numpy as np

from side_army import RedSide, BlackSide
from piece import Advisor, Cannon, Elephant, General, Horse, Pawn, Rook
from cotuong_const import ConstBase

class Match(object):
    """
    This is to deal with game match. FEN files and what not
    """

    def __init__(self):
        pass

    def load_match(self, match_file):
        pass

class Game(ConstBase): 
    def __init__(self, set_up = ''):
        super().__init__()

        self.PIECE_FROM_SYMBOLS_TO_OBJECT = {
            self.ADVISOR : Advisor, 
            self.CANNON  : Cannon,
            self.ELEPHANT: Elephant,
            self.GENERAL : General,
            self.HORSE   : Horse, 
            self.PAWN    : Pawn,
            self.ROOK    : Rook
        }

        if set_up != '':
            self.board_array = self.set_board_array(set_up)
        else: 
            self.board_array = self.init_board_array()

    def init_board_array(self):
        board_array = np.zeros_like(a=self.NUMERICAL_BOARD_GRID, dtype=str).tolist()
        # board_array = np.zeros(dtype=int,shape=(12, 11)).tolist()
        for piece in self.STARTING_COORDS: 
            coords = self.STARTING_COORDS[piece]
            for side in coords:
                for pos in coords[side]:
                    x = pos%self.NUMERICAL_DIVIDER_SERPERATING_X_AND_Y
                    y = pos//self.NUMERICAL_DIVIDER_SERPERATING_X_AND_Y
                    board_array[y][x] = piece

        for yy in range(12): 
            for xx in range(11):
                if board_array[yy][xx] == '':
                    board_array[yy][xx] = ' '

        return board_array 

    def set_board_array(self, set_up):
        return [] 
