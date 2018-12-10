from cotuong_const import ConstBase
from piece import Advisor, Cannon, Elephant, General, Horse, Pawn, Rook

class SideArmyBaseConst(ConstBase):
    def __init__(self):
        self.name = 'base_const'
        super().__init__()

        self.army = {
            self.ADVISOR : {
                1: Advisor, 2: Advisor}, 
            self.CANNON  : {
                1: Cannon,  2: Cannon},
            self.ELEPHANT: {
                1: Elephant, 2: Elephant},
            self.GENERAL : { 1: General},
            self.HORSE   : {
                1: Horse, 2: Horse} ,
            self.PAWN    : {
                1: Pawn, 2: Pawn, 3: Pawn, 4: Pawn, 5: Pawn},
            self.ROOK    : {
                1: Rook, 2: Rook}
        }

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Side Amry Base Constants are loaded.")


class SideArmyBase(SideArmyBaseConst):
    """
    Container for red side and black side pieces
    """

    def __init__(self, setup = ''):
        super().__init__()
        self.name = 'base'

        if setup != '':
            pass #Add setup here

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Side Army Base loaded.")

    def set_side(self, side=''):
        if side!= '' and side in [self.WHITE, self.BLACK]:
            if side == self.WHITE: 
                print("Set side for WHITE")
                for piece_type in self.army: 
                    for order in self.army[piece_type]:
                        if self.army[piece_type][order]().set_side(self.WHITE) != self.WHITE:
                            raise ValueError('Unable to set side to WHITE')                       
            elif side == self.BLACK: 
                print("Set side for BLACK")
                for piece_type in self.army: 
                    for order in self.army[piece_type]:
                        if self.army[piece_type][order]().set_side(self.BLACK) != self.BLACK:
                            raise ValueError('Unable to set side to BLACK.')                   
            else: 
                raise ValueError('Unknown side. Unable to set side to army.')

    def check_side(self): 
        ans = True 
        print("Army side: {}".format(self.name))
        for piece_type in self.army:
            for order in self.army[piece_type]:
                tmp = self.army[piece_type][order]()
                if tmp.side != self.name:
                    print("Piece side: {}. {}".format(tmp.side, tmp.side == ''))
                    ans = False
        return ans 

class RedSide(SideArmyBase): 
    def __init__(self):
        super().__init__()
        self.name = 'w'
        self.set_side(self.name)
        if not self.check_side():
            print(self.army)
            raise ValueError("At least 1 piece is not set to the same side with self.name")

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Red Army Base loaded.")       

class BlackSide(SideArmyBase):
    def __init__(self):
        super().__init__()
        self.name = 'b'
        self.set_side(self.name)
        if not self.check_side():
            raise ValueError("At least 1 piece is not set to the same side with self.name")

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Black Army Base loaded.")
       