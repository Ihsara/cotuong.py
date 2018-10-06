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

        self.DEFAULT_POSITIONS = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR w - - - 1"

        self.BOARD = np.zeros((10, 9), dtype=int)

        self.header = {}
        self.history = []

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
