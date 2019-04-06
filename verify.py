from cotuong_const import start_coords_2
from cotuong_const import BLACK_PALACE_BOUNDARY, WHITE_PALACE_BOUNDARY

class Piece(object):
    def __init__(self, name):
        self.name = name 
        self.position = start_coords_2[name][0]

    def _is_inboard(self):
        if  109 >= self.position >= 11 and self.position%10 != 0: 
            return True 
        else: 
            print(self.position)
            return False
    
    def _is_in_black_territory(self):
        if 59>= self.position >= 11 and self.position%10 != 0: 
            return True 
        else: 
            return False 
 
    def _is_in_white_territory(self):
        if 109>= self.position >= 61 and self.position%10 != 0:
            return True
        else:
            return False 

    def _is_in_black_palace(self):
        if self.position in BLACK_PALACE_BOUNDARY: 
            return True 
        else: 
            return False 

    def _is_in_white_palace(self):
        if self.position in WHITE_PALACE_BOUNDARY: 
            return True 
        else: 
            return False
    
    def _valid_move(self):
        pass 

class Advisor(Piece):
    def __init__(self, name, pos):
        super().__init__(self, name=name)
        self.position = pos

    def _valid_move(self):
        return True