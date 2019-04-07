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
                self.assertTrue(self.piece.is_inboard())

    def test_in_black_ter(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0, 50, 10): 
                self.piece.position = pos + col_incre
                self.assertTrue(self.piece.is_in_black_territory())

        for pos in self.pos_inboard_lowerbound: 
            for col_incre in range(0, 50, -10): 
                self.piece.position = pos + col_incre
                self.assertFalse(self.piece.is_in_black_territory())                        

    def test_in_white_ter(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0, 50, 10): 
                self.piece.position = pos + col_incre
                self.assertFalse(self.piece.is_in_white_territory())

        for pos in self.pos_inboard_lowerbound: 
            for col_incre in range(0, 50, -10): 
                self.piece.position = pos + col_incre
                self.assertTrue(self.piece.is_in_white_territory())

    def test_in_black_palace(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0,100, 10): 
                self.piece.position = pos + col_incre
                if pos+col_incre in BLACK_PALACE_BOUNDARY:                     
                    self.assertTrue(self.piece.is_in_black_palace())
                else: 
                    self.assertFalse(self.piece.is_in_black_palace())

    def test_in_white_palace(self):
        for pos in self.pos_inboard_upperbound: 
            for col_incre in range(0,100, 10): 
                self.piece.position = pos + col_incre
                if pos+col_incre in WHITE_PALACE_BOUNDARY:                     
                    self.assertTrue(self.piece.is_in_white_palace())
                else: 
                    self.assertFalse(self.piece.is_in_white_palace())


class TestAdvisorVerifier(TestCase):
    def setUp(self):
        self.advisor_w1 = Advisor('A', 0)
        self.advisor_w2 = Advisor('A', 1)
        self.advisor_b1 = Advisor('a', 0)
        self.advisor_b2 = Advisor('a', 1)

    def test_white_advisors_move_white_palace(self):
        self.assertEqual(self.advisor_w1.position, 104)
        self.assertEqual(self.advisor_w2.position, 106)
        self.assertTrue(self.advisor_w1.valid_move(95))
        self.assertTrue(self.advisor_w2.valid_move(95))

        self.advisor_w1.position = 95 
        self.advisor_w2.position = 95 

        self.assertTrue(self.advisor_w1.valid_move(104))
        self.assertTrue(self.advisor_w1.valid_move(106))
        self.assertTrue(self.advisor_w1.valid_move(84))
        self.assertTrue(self.advisor_w1.valid_move(86))

        self.assertTrue(self.advisor_w2.valid_move(104))
        self.assertTrue(self.advisor_w2.valid_move(106))
        self.assertTrue(self.advisor_w2.valid_move(84))
        self.assertTrue(self.advisor_w2.valid_move(86))

        self.advisor_w1.position = 84 
        self.advisor_w2.position = 86 

        self.assertTrue(self.advisor_w1.valid_move(95))
        self.assertTrue(self.advisor_w2.valid_move(95))

    def test_black_advisors_move_black_paplace(self): 
        self.assertTrue(self.advisor_b1.valid_move(25))
        self.assertTrue(self.advisor_b2.valid_move(25))

        self.advisor_b1.position = 25 
        self.advisor_b2.position = 25 

        self.assertTrue(self.advisor_b1.valid_move(14))
        self.assertTrue(self.advisor_b1.valid_move(16))
        self.assertTrue(self.advisor_b1.valid_move(34))
        self.assertTrue(self.advisor_b1.valid_move(36))

        self.assertTrue(self.advisor_b2.valid_move(14))
        self.assertTrue(self.advisor_b2.valid_move(16))
        self.assertTrue(self.advisor_b2.valid_move(34))
        self.assertTrue(self.advisor_b2.valid_move(36))

        self.advisor_b1.position = 34 
        self.advisor_b2.position = 36 

        self.assertTrue(self.advisor_b1.valid_move(25))
        self.assertTrue(self.advisor_b2.valid_move(25))