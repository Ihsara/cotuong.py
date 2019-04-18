import numpy as np

from cotuong_const import start_coords_2, INVALID_POS
from cotuong_const import BLACK_PALACE_BOUNDARY, WHITE_PALACE_BOUNDARY

'''
TBD: blocking and eating function => Move to GameState 
'''


class Piece(object):
    def __init__(self, name):
        self.name = name
        self.position = start_coords_2[name]
        self.INVALID_POS = INVALID_POS

    def is_inboard(self, next_pos=INVALID_POS):
        if next_pos != INVALID_POS and 109 >= next_pos >= 11 and next_pos % 10 != 0:
            return True
        elif 109 >= self.position >= 11 and self.position % 10 != 0:
            return True
        else:
            return False

    def is_in_black_territory(self):
        if 59 >= self.position >= 11 and self.position % 10 != 0:
            return True
        else:
            return False

    def is_in_white_territory(self):
        if 109 >= self.position >= 61 and self.position % 10 != 0:
            return True
        else:
            return False

    def is_in_black_palace(self):
        if self.position in BLACK_PALACE_BOUNDARY:
            return True
        else:
            return False

    def is_in_white_palace(self):
        if self.position in WHITE_PALACE_BOUNDARY:
            return True
        else:
            return False

    def valid_move(self, next_pos=INVALID_POS):
        self.position = next_pos
        return self.is_inboard()

    def set_move(self, next_pos):
        return next_pos if self.valid_move(next_pos) else self.position


class Advisor(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        if name == 'a':
            self.pos_limit = [14, 16, 25, 34, 36]
        elif name == 'A':
            self.pos_limit = [104, 106, 95, 84, 86]
        else:
            raise ValueError('Advisor only takes "a" or "A" for name.')
        self.position = self.position[pos_id]
        self.id = name+str(pos_id)

    def valid_move(self, next_pos=INVALID_POS):
        if next_pos in self.pos_limit and self.position in self.pos_limit and (self.position + 9 == next_pos or self.position - 9 == next_pos or self.position - 11 == next_pos or self.position + 11 == next_pos):
            return True
        else:
            return False


class Cannon(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        self.position = self.position[pos_id]
        self.id = name + str(pos_id)

    def valid_move(self, next_pos=INVALID_POS):
        if self.is_inboard(self.position) and self.is_inboard(next_pos) and ((abs(next_pos - self.position) <= 8 and (next_pos//10 - self.position//10) == 0) or (abs(next_pos - self.position) >= 10 and abs(next_pos - self.position) % 10 == 0)):
            return True
        else:
            return False


class Elephant(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        self.position = self.position[pos_id]
        self.id = name + str(pos_id)
        if name == 'e':
            self.pos_limit = [13, 17, 31, 35, 39, 53, 57]
        elif name == 'E':
            self.pos_limit = [63, 67, 81, 85, 89, 103, 107]
        else:
            raise ValueError("Elephant only takes 'e' or 'E' for name")

    def valid_move(self, next_pos=INVALID_POS):
        if next_pos in self.pos_limit and self.position in self.pos_limit and (self.position + 18 == next_pos or self.position - 18 == next_pos or self.position + 22 == next_pos or self.position - 22 == next_pos):
            return True
        else:
            return False


class General(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        if name == 'g':
            self.pos_limit = BLACK_PALACE_BOUNDARY
        elif name == 'G':
            self.pos_limit = WHITE_PALACE_BOUNDARY
        else:
            raise ValueError('General only takes "g" or "G" for name.')
        self.position = self.position[pos_id]
        self.id = name + str(pos_id)

    def valid_move(self, next_pos=INVALID_POS):
        if next_pos in self.pos_limit and self.position in self.pos_limit and (self.position + 1 == next_pos or self.position - 1 == next_pos or self.position + 10 == next_pos or self.position - 10 == next_pos):
            return True
        else:
            return False


class Horse(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        self.position = self.position[pos_id]
        self.id = name + str(pos_id)

    def valid_move(self, next_pos=INVALID_POS):
        pass


class Pawn(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        self.position = self.position[pos_id]
        self.id = name + str(pos_id)

    def valid_move(self, next_pos=INVALID_POS):
        pass


class Rock(Piece):
    def __init__(self, name, pos_id=0):
        super().__init__(name)
        self.position = self.position[pos_id]
        self.id = name + str(pos_id)

    def valid_move(self, next_pos=INVALID_POS):
        if self.is_inboard(self.position) and self.is_inboard(next_pos) and ((abs(next_pos - self.position) <= 8 and (next_pos//10 - self.position//10) == 0) or (abs(next_pos - self.position) >= 10 and abs(next_pos - self.position) % 10 == 0)):
            return True
        else:
            return False
