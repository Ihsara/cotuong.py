from cotuong_const import ConstBase

class PieceConst(ConstBase):
    def __init__(self):
        super().__init__()
        self.FAILED_TO_ASSIGN_SIDE = 'f'

        self.PIECE_TYPE = { 
            'PieceBaseClass': 'pbc',
            'Advisor': self.ADVISOR,
            'Cannon': self.CANNON,
            'Elephant': self.ELEPHANT,
            'General': self.GENERAL,
            'Horse': self.HORSE, 
            'Pawn': self.PAWN,
            'Rook': self.ROOK
        }

class PieceBase(PieceConst):
    """ 
    Base Piece class for chesspieces.
    """ 

    def __init__(self):
        super().__init__()
        self.name = 'PieceBaseClass'
        self.description = "Piece base class"
        self.moves = []
        self.encoded_name = ''
        self.type = self.PIECE_TYPE[self.name]
        self.side = ''

    def update_history(self, new_move):
        self.moves.append(new_move)

    def get_hostory(self):
        return self.moves

    def set_side(self, side):
        self.side = side 
        if side == 'w':
            self.encoded_name = self.name[0].lower() 
        elif side == 'b':
            self.encoded_name = self.name[0].upper() 
        else: 
            self.encoded_name = self.FAILED_TO_ASSIGN_SIDE
            ans = False

        return self.side

    def __str__(self):
        return "{} - {}".format(self.name, self.description)

    def __repr__(self): 
        if len( self.moves)> 0: 
            return "{} - {} - Position: {}".format(self.name, self.description, self.moves[-1])
        else: 
            return "{} - {}".format(self.name, self.description)


class Advisor(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'Advisor'
        self.description = 'Advisor'
        
class Cannon(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'Cannon'

class Elephant(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'Elephant'

class General(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'General'

class Horse(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'Horse'

class Pawn(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'Pawn'

class Rook(PieceBase):
    def __init__(self):
        super().__init__()
        self.name = 'Rook'





        
        