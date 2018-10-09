"""

cotuong.py: verifier and things like that for cờ tướng(xiangqi)

TO DO:
Verification: move, notation(FEN, ...)
ASCII playable chessboard


"""


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

        self.BOARD = np.zeros((10, 9), dtype=int)

        self.DEFAULT_POSITIONS = {}

        self.CHESSPIECE_DISTRIBUTION_NUMBER = dict(zip(self.SYMBOLS, self.SYMBOLS_DIST))

        self.header = {}
        self.history = []

        self.fen = self.fen_string_syntax_verification(fen)

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
        is_starting_position = FALSE

        #poorly written, works nonetheless
        #I/ Chesspiece arrangement string
        try:
            set_up, turn_color, rr1, rr2, half_piece, turn = fen.split(' ')
        except ValueError:
            try:
                set_up, turn_color, half_piece, turn = fen.split(' ')
            except ValueError:
                print("FEN validation error: FEN string has more/less than needed parts. \n Must have either 6 or 4 parts")
                raise

        rows = set_up.split('/')
        dist_check = self.CHESSPIECE_DISTRIBUTION_NUMBER
        if len(rows) != 10:
            print("FEN validation error: Number of row is not 10 ( is {})".format(len(rows)))
            raise

        for row in rows:
            if len(row) > 9 or (len(row)== 1 and row[0] != '9'):
                print("FEN validation error:  Row '{}' has more/less than 9 items.".format(row))
                raise
            else:
                items = list(row)
                sum_check = 0
                for item in items:
                    try :
                        if item != '0':
                            sum_check += int(item)
                        else:
                            print("FEN validation error: FEN notation cannot contain number 0")
                            raise
                    except ValueError:
                        if item is in self.SYMBOLS:
                            sum_check += 1
                            dist_check[item] -= 1
                        else:
                            print("FEN validation error: Unrecognized symbol ({}) for a chesspiece.\n Must be included in ({})".format(item,self.SYMBOLS))
                            raise
                if sum_check != 9:
                    print("FEN validation error: Row {} has more/less than 9 items.".format(items))
                    raise

                if dist_check[self.GENERAL] == 1 or dist_check[self.GENERAL.upper()] == 1 :
                    print("FEN validation error: Each side's general must be presented with 1 as the quantity({missing_piece}).".format(
                        missing_piece = [mgen for mgen in [self.GENERAL, self.GENERAL.upper()] if dist_check[mgen] ==1])
                    raise

                for chesspiece in dist_check:
                    if dist_check[chesspiece] < 0 :
                        print("FEN validation error: {piecename} has more pieces than allowed({piecename_counted_num} from {piecename_allowed_num}).".format(
                            piecename=chesspiece,
                             piecename_counted_num = dist_check[chesspiece],
                              piecename_allowed_num = self.CHESSPIECE_DISTRIBUTION_NUMBER[chesspiece])
                        raise

        #II/ Color of side to make the next move
        if set_up == self.DEFAULT_SETUP :
            is_starting_position = True

        if turn_color in [self.BLACK, self.WHITE]:
            if turn_color.isupper(): turn_color.lower()
            if is_starting_position:
                if turn_color != self.WHITE:
                    print("FEN validation error: Starting setup detected(all pieces at starting positions), white(red) side must be the next to move.")
                    raise
        else:
            print("FEN validation error: Wrong color encoding for sides. Must either be black(b) or white(w).")
            raise
        #V/ To be later defined. Need to read rules about half move
        #VI/ Turn
        try:
            turn_int = int(turn)
        except ValueError:
            print("FEN validation error: Turn must be an positive integer starting from 1.")
            raise

        if turn_int != 1 and is_starting_position:
            print("FEN validation error: Turn must be an positive integer starting from 1.")
            raise
        elif turn_int < 1:
            print("FEN validation error: Turn must be an positive integer starting from 1.")
            raise








    def fen_string_to_board(self);
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

