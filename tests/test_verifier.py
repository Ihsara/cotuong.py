from unittest import TestCase 

from cotuong_const import BLACK_PALACE_BOUNDARY, WHITE_PALACE_BOUNDARY
from verify import Piece, Advisor 

class TestPieceVerifier(TestCase):
    def setUp(self):
        self.pos_inboard_upperbound = [11 + i for i in range(9)]
        self.pos_inboard_leftbound = [11 + i for i in range(0, 100, 10)] 
        self.pos_inboard_rightbound = [19 + i for i in range(0, 100, 10)]
        self.pos_inboard_lowerbound = [101 + i for i in range(9)]
        self.piece = Piece('a')

    def test_is_inboard(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0,100, 10): 
                self.piece.position = pos + col_incre
                self.assertTrue(self.piece._is_inboard())

    def test_in_black_ter(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0, 50, 10): 
                self.piece.position = pos + col_incre
                self.assertTrue(self.piece._is_in_black_territory())

        for pos in self.pos_inboard_lowerbound: 
            for col_incre in range(0, 50, -10): 
                self.piece.position = pos + col_incre
                self.assertFalse(self.piece._is_in_black_territory())                        

    def test_in_white_ter(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0, 50, 10): 
                self.piece.position = pos + col_incre
                self.assertFalse(self.piece._is_in_white_territory())

        for pos in self.pos_inboard_lowerbound: 
            for col_incre in range(0, 50, -10): 
                self.piece.position = pos + col_incre
                self.assertTrue(self.piece._is_in_white_territory())

    def test_in_black_palace(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0,100, 10): 
                self.piece.position = pos + col_incre
                if pos+col_incre in BLACK_PALACE_BOUNDARY:                     
                    self.assertTrue(self.piece._is_in_black_palace())
                else: 
                    self.assertFalse(self.piece._is_in_black_palace())

    def test_in_white_palace(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0,100, 10): 
                self.piece.position = pos + col_incre
                if pos+col_incre in WHITE_PALACE_BOUNDARY:                     
                    self.assertTrue(self.piece._is_in_white_palace())
                else: 
                    self.assertFalse(self.piece._is_in_white_palace())


class TestAdvisorVerifier(TestCase):
    def setUp(self):
        pass 

    def test_white_advisors_move_white_palace(self):
        pass 

    def test_black_advisors_move_black_paplace(self): 
        pass