"""

cotuong.py: verifier and things like that for cờ tướng(xiangqi)

TO DO:
Verification: move, notation(FEN, ...)
ASCII playable chessboard


"""




class Chess(object):
    def __init__(self, fen=""):
        self.WHTIE = 'w' #Represent red side
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

        self.DEFAULT_SETUP = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR"

        self.DEFAULT_FEN_STARTING_SETUP = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR w - - - 1"

        self.BOARD = np.zeros((10, 9), dtype=int)

        self.DEFAULT_POSITIONS = {}

        self.header = {}
        self.history = []

        self.fen = self.fen_string_syntax_verification(fen)

    def fen_string_syntax_verification(self, fen):
        '''
        FEN verification string syntax check:

        FEN string contains either 6 parts (DEFAULT) or 4 parts (*To be included in later):
        1/ Chesspiece arrangement string
        2/ Color of side to make the next move. Default: White (Red) always go first.
        3/ Must be "-" (make redundant in 4-part FEN)
        4/ Must be "-" (make redundant in 4-part FEN)
        5/ Defined later. For now, must be "-"
        6/ Turn (after black piece have made a move)

        Conditions for each part (I - VI):
        I/ Chesspiece arrangement string

        _ Contains 10 rows seperated by a "/" each (1)
        _ Symbols are within self.SYMBOLS(2)
        _ Symbol(s) and number sum up to 9 for each row (3)
        _ The amount of each symbols must not be more than the allocated number of pieces (4)

        II/ Color of side to make the next move
        _ Must be either black(b) or white(w) (5)
        _ On set up is the same as in self.DEFAULT_SETUP, white(w) must always be in this part (6)
        _ Must be lowercase. Fix into lowercase when found (Act as WARNING, do not raise exception)

        III/ Redundant Relics

        IV/  Redundant Relics

        V/ To be later defined. Need to read rules.
        VI/ Turn
        _ Must be integer (7)

        List of exceptions:
        (1)FEN string has more/less than needed parts. \n Must have either 6 or 4 parts
        (2)Number of row is not 10 ( is {counted_row_num})
        (3)Unrecognized symbol ({unrecognized_symbol}) for a chesspiece.\n Must be included in ({self.SYMBOLS})
        (4)Row {row_no} has more/less than 9 items.
        (5){piecename} has more pieces than allowed( {piecename_counted_num} from {piecename_allowed_num}).
        (6)Wrong color encoding for sides. Must either be black(b) or white(w)
        (7)Starting setup detected(all pieces at starting positions), white(red) side must be the next to move.
        (8)Turn must be an positive integer starting from 1.
        '''
        is_starting_position = FALSE

        #poorly written, works nonetheless
        try:
            set_up, turn_color, rr1, rr2, half_piece, turn = fen.split(' ')
        except ValueError:
            try:
                set_up, turn_color, half_piece, turn = fen.split(' ')
            except ValueError:
                print("FEN string does not have ")
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

