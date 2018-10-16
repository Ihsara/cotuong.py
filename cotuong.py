"""

cotuong.py: verifier and things like that for cờ tướng(xiangqi)

TO DO:
Verification: move, notation(FEN, ...)
ASCII playable chessboard


"""

import numpy as np
import re

class Chess(object):
    def __init__(self, fen=""):
        self.WHITE = 'w' #Represent red side
        self.BLACK = 'b' #Represent blue side

        self.EMPTY = -1

        self.ADVISOR = 'a'
        self.CANNON = 'c'
        self.ELEPHANT = 'e'
        self.GENERAL = 'g'
        self.HORSE = 'h'
        self.PAWN = 'p'
        self.ROOK = 'r'

        self.SYMBOLS = 'aceghprACEGHPR'
        self.SYMBOLS_DIST = [2, 2, 2, 1, 2, 5, 2, 2, 2, 2, 1, 2, 5, 2]

        self.DEFAULT_SETUP = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR"

        self.DEFAULT_FEN_STARTING_SETUP = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR w - - - 1"

        self.DEFAULT_POSITIONS = {}

        self.CHESSPIECE_DISTRIBUTION_NUMBER = dict(zip(self.SYMBOLS, self.SYMBOLS_DIST))

        self.NUMERICAL_BOARD_GRID = [
            [11,12,13,14,15,16,17,18,19],
            [21,22,23,24,25,26,27,28,29],
            [31,32,33,34,35,36,37,38,39],
            [41,42,43,44,45,46,47,48,49],
            [51,52,53,54,55,56,57,58,59],
            [61,62,63,64,65,66,67,68,69],
            [71,72,73,74,75,76,77,78,79],
            [81,82,83,84,85,86,87,88,89],
            [91,92,93,94,95,96,97,98,99],
            [101,102,103,104,105,106,107,108,109]
        ]

        self.IS_FEN_VALIDATED = True

        self.chessPieceSetUp, self.turnColor,self.halfTurn, self.turnInt  = self.fen_string_syntax_verification(fen)
        if self.IS_FEN_VALIDATED:

            self.header = {
                'turn' : self.turnInt,
                'turnColor':self.turnColor,
                'halfTurn': self.halfTurn
            }
            self.history = [self.turnInt]

            if fen == '':
                self.chessPieceSetUp = self.DEFAULT_SETUP
                print("No fen string inserted. Object Chess is initialized to the begning.")
            else:
                print("Chess object now at {}. {} goes next. This game is recorded on turn {}".format(
                    self.chessPieceSetUp,
                    self.turnColor,
                    self.turnInt))
            self.BOARD = self.init_board()
            self.BOARD_NUMERICAL = self.init_board_numerical()
        else:
            print('fen string has problem. Please init Chess object with vilid FEN sring')

    def fen_string_syntax_verification(self, fen):
        '''
        FEN verification string syntax check:
        (number) is the exception message numbered

        FEN string contains either 6 parts (DEFAULT) or 4 parts (*To be included in later)(1):
        1/ Chesspiece arrangement string
        2/ Color of side to make the next move. Default: White (Red) always go first.
        3/ Must be "-" (make redundant in 4-part FEN)
        4/ Must be "-" (make redundant in 4-part FEN)
        5/ Defined later. For now, must be "-"
        6/ Turn (after black piece have made a move)

        Conditions for each part (I - VI):
        I/ Chesspiece arrangement string

        _ Contains 10 rows seperated by a "/" each (2)
        _ Symbols are within self.SYMBOLS(3)
        _ Symbol(s) and number sum up to 9 for each row (4)
        _ The amount of each symbols must not be more than the allocated number of pieces (5)
        _ Numbers must be from 1-9. 0 is not allowed (6)
        _ Each side's general must be presented. Missing {missing_piece} (7)

        II/ Color of side to make the next move
        _ Must be either black(b) or white(w) (8)
        _ On set up is the same as in self.DEFAULT_SETUP, white(w) must always be in this part (9)
        _ Must be lowercase. Fix into lowercase when found (Act as WARNING, do not raise exception)

        III/ Redundant Relics

        IV/  Redundant Relics

        V/ To be later defined. Need to read rules.
        VI/ Turn
        _ Must be integer (10)

        List of exceptions' messages:
        (1)FEN string has more/less than needed parts. \n Must have either 6 or 4 parts
        (2)Number of row is not 10 ( is {counted_row_num})
        (3)Unrecognized symbol ({unrecognized_symbol}) for a chesspiece.\n Must be included in ({self.SYMBOLS})
        (4)Row {row_no} has more/less than 9 items.
        (5){piecename} has more pieces than allowed( {piecename_counted_num} from {piecename_allowed_num}).
        (6)FEN notation cannot contain number 0
        (7)Each side's general must be presented. Missing {missing_piece}.
        (8)Wrong color encoding for sides. Must either be black(b) or white(w)
        (9)Starting setup detected(all pieces at starting positions), white(red) side must be the next to move.
        (10)Turn must be an positive integer starting from 1.
        '''
        is_starting_position = False

        #poorly written, works nonetheless
        #I/ Chesspiece arrangement string
        try:
            set_up, turn_color, rr1, rr2, half_piece, turn = fen.split(' ')
        except ValueError:
            try:
                set_up, turn_color, half_piece, turn = fen.split(' ')
            except ValueError:
                print("FEN validation error: FEN string has more/less than needed parts. \n Must have either 6 or 4 parts")
                self.IS_FEN_VALIDATED = False
        if rr1 != '-' or rr2 != '-':
            print('FEN warning: Need "-", have "{}{}"'.format(
                rr1, rr2
            ) )
        rows = set_up.split('/')
        dist_check = self.CHESSPIECE_DISTRIBUTION_NUMBER
        if len(rows) != 10:
            print("FEN validation error: Number of row is not 10 ( is {})".format(len(rows)))
            self.IS_FEN_VALIDATED = False

        for row in rows:
            if len(row) > 9 or (len(row)== 1 and row[0] != '9'):
                print("FEN validation error:  Row '{}' has more/less than 9 items.".format(row))
                self.IS_FEN_VALIDATED = False
            else:
                items = list(row)
                sum_check = 0
                for item in items:
                    try :
                        if item != '0':
                            sum_check += int(item)
                        else:
                            print("FEN validation error: FEN notation cannot contain number 0")
                            self.IS_FEN_VALIDATED = False
                    except ValueError:
                        if item in self.SYMBOLS:
                            sum_check += 1
                            dist_check[item] -= 1
                        else:
                            print("FEN validation error: Unrecognized symbol ({}) for a chesspiece.\n Must be included in ({})".format(item,self.SYMBOLS))
                            self.IS_FEN_VALIDATED = False
                if sum_check != 9:
                    print("FEN validation error: Row {} has more/less than 9 items.".format(items))
                    self.IS_FEN_VALIDATED = False

                if dist_check[self.GENERAL] == 1 or dist_check[self.GENERAL.upper()] == 1 :
                    print("FEN validation error: Each side's general must be presented with 1 as the quantity({missing_piece}).".format(
                        missing_piece = [mgen for mgen in [self.GENERAL, self.GENERAL.upper()] if dist_check[mgen] ==1]))
                    self.IS_FEN_VALIDATED = False

                for chesspiece in dist_check:
                    if dist_check[chesspiece] < 0 :
                        print("FEN validation error: {piecename} has more pieces than allowed({piecename_counted_num} from {piecename_allowed_num}).".format(
                            piecename=chesspiece,
                             piecename_counted_num = dist_check[chesspiece],
                              piecename_allowed_num = self.CHESSPIECE_DISTRIBUTION_NUMBER[chesspiece]))
                        self.IS_FEN_VALIDATED = False

        #II/ Color of side to make the next move
        if set_up == self.DEFAULT_SETUP :
            is_starting_position = True

        if turn_color in [self.BLACK, self.WHITE]:
            if turn_color.isupper(): turn_color.lower()
            if is_starting_position:
                if turn_color != self.WHITE:
                    print("FEN validation error: Starting setup detected(all pieces at starting positions), white(red) side must be the next to move.")
                    self.IS_FEN_VALIDATED = False
        else:
            print("FEN validation error: Wrong color encoding for sides. Must either be black(b) or white(w).")
            self.IS_FEN_VALIDATED = False
        #V/ To be later defined. Need to read rules about half move
        #VI/ Turn
        try:
            turn_int = int(turn)
        except ValueError:
            print("FEN validation error: Turn must be an positive integer starting from 1.")
            self.IS_FEN_VALIDATED = False

        if turn_int != 1 and is_starting_position:
            print("FEN validation error: Turn must be an positive integer starting from 1.")
            self.IS_FEN_VALIDATED = False
        elif turn_int < 1:
            print("FEN validation error: Turn must be an positive integer starting from 1.")
            self.IS_FEN_VALIDATED = False

        return set_up, turn_color, half_piece, turn_int

    def init_board(self):
        base_array = np.zeros((12, 11), dtype="U25")
        base_array[0] = '*'
        base_array[:,10] = '*'
        base_array[:,0] = '*'
        base_array[11] = '*'
        return base_array

    def init_board_numerical(self):
        base_array       = np.zeros((12, 11), dtype=int)
        base_array[0]    = -1
        base_array[:,10] = -1
        base_array[:,0]  = -1
        base_array[11]   = -1
        return base_array

    def load_game(self):
        pass

    def fen_string_to_board(self):
        '''
        Have FEN string translated into a BOARD array
        '''
        pass

    def board_to_fen_string(self):
        '''
        Have BOARD array compressed into a FEN string
        '''
        pass

    def fen(self):
        return self.board_to_fen_string()


    def ascii(self):
        self.fen_string = self.board_to_fen_string()
        pass


class chessPiece(object):
    def __init__(self, fen_notation_name):
        self.WHITE = 'w' #Represent red side
        self.BLACK = 'b' #Represent blue side

        self.EMPTY = -1
        self.REFERENCE_LIST = {
            'a':'Advisor',
            'c': 'Chariot',
            'e': 'Elephant',
            'g': 'General',
            'h': 'Horse',
            'p': 'Pawn',
            'r': 'Rook'
        }

        self.id = fen_notation_name
        self.name = self.identify ()
        self.history = []

    def identify(self):
        side = ''
        if self.id.isupper():
            side = self.BLACK
        else: side = self.WHITE
        return {'type': self.REFERENCE_LIST[self.id],'side': side}

    def add_move(self, move):
        self.history.append(move)

    def undo_move(self):
        self.history.pop()


