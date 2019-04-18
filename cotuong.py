from cotuong_const import board_matrix, start_coords_2
from copy import deepcopy

BOARD_MATRIX = deepcopy(board_matrix)
STARTCOORDS = deepcopy(start_coords_2)


def is_fen(load):
    return load is None


def is_dict(load):
    dict_format = []  # format like start_coords_2
    return isinstance(load, dict) and dict_format is not None


class GameState(object):
    def __init__(self, load=''):
        self.SYMBOLS = 'aceghprACEGHPR'
        self.nex_move = 'w'
        self.turn = 1
        self.board_matrix = deepcopy(BOARD_MATRIX)
        self.__start_coords = deepcopy(STARTCOORDS)
        self.board_setup = []
        self.__load_game(load)
        self.history = []

    def __new_game(self):
        self.board_setup = deepcopy(self.__start_coords)
        self.next_move = 'w'
        self.turn = 1
        return 'New game has been set.'

    def new_game(self):
        return self.__new_game()

    def current_turn(self):
        return self.board_matrix

    @property
    def start_coords(self):
        return self.__start_coords

    def __load_game(self, load):
        if load == '':
            self.__new_game()
        elif is_fen(load):
            pass
        elif is_dict(load):
            pass
        else:
            raise ValueError('Unrecognized string to load')

    def __recieve_new_move(self):
        return None

    def __update_move(self):
        return None

    def __update_history(self):
        self.history.append(self.board_setup)
