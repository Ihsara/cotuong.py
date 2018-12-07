from cotuong_const import ConstBase

class SideArmyBaseConst(ConstBase):
    def __init__(self):
        self.name = 'base_const'
        super().__init__()

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Side Amry Base Constants are loaded.")

class SideArmyBase(SideArmyBaseConst):
    """
    Container for red side and black side pieces
    """

    def __init__(self):
        super().__init__()
        self.name = 'base'

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Side Army Base loaded.")

class RedSide(SideArmyBase): 
    def __init__(self):
        super().__init__()
        self.name = 'w'

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Red Army Base loaded.")       

class BlackSide(SideArmyBase):
    def __init__(self):
        super().__init__()
        self.name = 'b'

    def __str__(self):
        return "{}\n{}".format(super().__str__(), "Black Army Base loaded.")
       