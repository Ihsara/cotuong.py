import numpy as np 
import fire

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

        self.PIECES_FROM_SYMBOLS_TO_OBJECTS = {
            self.ADVISOR : Advisor, 
            self.CANNON  : Cannon,
            self.ELEPHANT: Elephant,
            self.GENERAL : General,
            self.HORSE   : Horse, 
            self.PAWN    : Pawn,
            self.ROOK    : Rook
        }
        self.is_starter = True
        self.turn = 0

        if set_up != '':
            self.red_side, self.black_side, self.units_dict = self._init_starting_units_with_setup(set_up)
        else: 
            self.red_side, self.black_side, self.units_dict = self._init_starting_units_without_setup()

    def translate_to_board_array(self):
        """
            Use the self.units_dict to translate into an array similar to self.NUMERICAL_BOARD_GRID 
        """
        self.red_side   = RedSide() 
        self.black_side = BlackSide() 

        board_array = []



        return board_array

    def _init_starting_units_without_setup(self): 
        red_side   = RedSide()
        black_side = BlackSide()

        units_dict = {
            red_side.name: red_side.army,
            black_side.name: black_side.army
        }

        return red_side, black_side, units_dict 

    def _init_starting_units_with_setup(self, setup): 
        red_side   = RedSide()
        black_side = BlackSide()

        units_dict = {}

        return red_side, black_side, units_dict


    def set_board_array(self, set_up):
        return [] 


    def cli_view(self):
        board_array = np.zeros_like(a=self.NUMERICAL_BOARD_GRID, dtype=str).tolist()
        # board_array = np.zeros_like(a=self.NUMERICAL_BOARD_GRID, dtype=int).tolist()
        # board_array = np.zeros(dtype=int,shape=(12, 11)).tolist()
        if self.is_starter: 
            coords_mapping = self.STARTING_COORDS
            self.is_starter = False
        else: 
            coords_mapping = self.coords_mapping

        for piece in coords_mapping: 
            coords = coords_mapping[piece]
            for side in coords:
                for pos in coords[side]:
                    x = pos%self.NUMERICAL_DIVIDER_SERPERATING_X_AND_Y
                    y = pos//self.NUMERICAL_DIVIDER_SERPERATING_X_AND_Y
                    tmp = self.PIECES_FROM_SYMBOLS_TO_OBJECTS[piece]()
                    tmp.set_side(side)
                    board_array[y][x] = tmp.encoded_name

        for yy in range(12): 
            for xx in range(11):
                if board_array[yy][xx] == '':
                    board_array[yy][xx] = ' '

        return board_array

    
if __name__ == '__main__':
  fire.Fire(Game)