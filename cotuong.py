from cotuong_const import board_matrix, start_coords_2, INVALID_POS
from copy import deepcopy
from verify import Advisor, Cannon, Elephant, General, Horse, Pawn, Rock

BOARD_MATRIX = deepcopy(board_matrix)
STARTCOORDS = deepcopy(start_coords_2)

notation_to_object = {
    'a': Advisor, 
    'c': Cannon, 
    'e': Elephant, 
    'g': General,
    'h': Horse,
    'p': Pawn,
    'r': Rock
}

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
        self.piece_list = []
        self.__load_game(load)
        self.history = []

    def __generate_piece_list_from_position_list(self, piece_name):
        return [notation_to_object[piece_name.lower()](name=piece_name, pos_id=id) for id in range(len(self.__start_coords[piece_name]))]

    def __generate_piece_list(self):
        return [piece for piece_name in self.SYMBOLS for piece in self.__generate_piece_list_from_position_list(piece_name)]

    def __generate_simple_current_turn_state(self):
        return [piece.current_state for piece in self.piece_list]

    def __new_game(self):
        self.next_move = 'w'
        self.turn = 1
        self.piece_list = self.__generate_piece_list()
        return 'New game has been set.'

    def is_occupied(self,piece, next_pos): 
        blocked_destination = False 
        blocked_enroute     = False 
        opposite_side_destination = False
        pos_list = set([pos for rule in piece.blocking_rules for pos in rule(curr_pos=piece.position, target_pos=next_pos)])

        another_piece = self.get_piece_with_position(next_pos)
        if another_piece is not None: 
            blocked_destination = True 
            opposite_side_destination = not ((piece.name.isupper() and another_piece.name.isupper) and (piece.name.islower() and another_piece.name.islower()))
        pos_list.remove(next_pos)

        for pos in pos_list: 
            another_piece = self.get_piece_with_position(pos)
            if  another_piece is not None:
                blocked_enroute = True 
                break 

        return blocked_destination, blocked_enroute, opposite_side_destination

    def get_piece_with_position(self, value):
        return next((x for x in self.piece_list if x.position == value), None)

    def get_piece_with_id(self, value):
        return next((x for x in self.piece_list if x.id == value), None)

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

    def __update_piece_list(self):
        return 

    def __update_history(self):
        self.history.append(self.__generate_simple_current_turn_state())

    def update_move(self, piece_id, next_pos):
        is_updated = False 
        try: 
            piece = self.get_piece_with_id(piece_id)        
            if piece.valid_move(next_pos):
                is_destination_blocked, is_enroute_blocked, is_edible = self.is_occupied(piece=piece, next_pos=next_pos)
                if not is_enroute_blocked:
                    if is_destination_blocked and is_edible:
                        eatee_piece = self.get_piece_with_position(next_pos)
                        eatee_piece.position = -eatee_piece.position
                        piece.position = next_pos 
                        is_updated = True
                    elif not is_destination_blocked:
                        piece.position = next_pos 
                        is_updated = True                     
        except AttributeError: 
            print('No piece with this id')

        return is_updated

    def turn_mananger(self, move={'piece_id': '', 'next_pos': INVALID_POS}):
        if self.update_move(piece_id=move['piece_id'], next_pos=move['next_pos']):
            self.__update_history() 
            if move['piece_id'][0].islower(): 
                self.next_move = 'w'
            else: 
                self.next_move = 'b'
                self.turn += 1 

if __name__ == "__main__": 
    from pprint import PrettyPrinter as pp 
    newgame = GameState() 
    newgame.new_game() 
    pp().pprint(Pawn('P', 2).valid_move(65))
    pp().pprint(newgame.is_occupied(newgame.get_piece_with_id('P2'), 65))
    pp().pprint(newgame.update_move('P2', 65))
    pp().pprint(newgame.piece_list)