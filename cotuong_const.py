

class ConstBase(object):
    def __init__(self): 
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
        self.RED_SYMBOLS = 'ACEGHPR'
        self.BLACK_SYMBOLS = 'aceghpr'
        self.SYMBOLS_DIST = [2, 2, 2, 1, 2, 5, 2, 2, 2, 2, 1, 2, 5, 2]

        self.DEFAULT_SETUP = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR"

        self.DEFAULT_FEN_STARTING_SETUP = "rheagaehr/9/1c5c1/p1p1p1p1p/9/9/P1P1P1P1P/1C5C1/9/RHEAGAEHR w - - - 1"

        self.DEFAULT_POSITIONS = {}

        self.CHESSPIECE_DISTRIBUTION_NUMBER = dict(zip(self.SYMBOLS, self.SYMBOLS_DIST))

        self.NUMERICAL_DIVIDER_SERPERATING_X_AND_Y = 10
        self.NUMERICAL_BOARD_GRID = [
            [  0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10],
            [ 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 110],
            [ 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 210],
            [ 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 310],
            [ 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 410],
            [ 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 510],
            [ 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 610],
            [ 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 710],
            [ 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 810],
            [ 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 910],
            [100,101,102,103,104,105,106,107,108,109,1010],
            [110,111,112,113,114,115,116,117,118,119,1110]
        ]

        self.STARTING_COORDS = {
            self.ADVISOR: {
                self.WHITE: [104,106],
                self.BLACK: [14,16]
            },

            self.CANNON: {
                self.WHITE: [82,88],
                self.BLACK: [32,38]
            },

            self.ELEPHANT: {
                self.WHITE: [103,107],
                self.BLACK: [13,17]
            },

            self.GENERAL: {
                self.WHITE: [105],
                self.BLACK: [15]
            },

            self.HORSE: {
                self.WHITE: [102,108],
                self.BLACK: [12,18]
            },

            self.PAWN: {
                self.WHITE: [71,73,75,77,79],
                self.BLACK: [41,43,45,47,49]
            },

            self.ROOK: {
                self.WHITE: [101,109],
                self.BLACK: [11,19]
            },

        }


    def __str__(self):
        return "Constants are loaded."