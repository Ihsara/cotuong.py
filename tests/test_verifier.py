from unittest import TestCase 

from cotuong_const import BLACK_PALACE_BOUNDARY, WHITE_PALACE_BOUNDARY
from verify import Piece, Advisor, Cannon, Elephant, General, Horse, Pawn, Rock

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

class TestCannonVerifier(TestCase):
    def setUp(self): 
        self.cannon_w1 = Cannon('C',0)
        self.cannon_w2 = Cannon('C',1)
        self.cannon_b1 = Cannon('c',0)
        self.cannon_b2 = Cannon('c',1)

    def test_cannon_move_vertically(self):
        pass 

    def test_cannon_move_horinzontally(self):
        pass 

class TestElephantVerifier(TestCase):
    def setUp(self): 
        self.elephant_w1 = Elephant('E',0)
        self.elephant_w2 = Elephant('E',1)
        self.elephant_b1 = Elephant('e',0)
        self.elephant_b2 = Elephant('e',1)

    def test_elephant_white_territory(self):
        self.assertEqual(self.elephant_w1.position, 103)
        self.assertEqual(self.elephant_w2.position, 107)
        self.assertTrue(self.elephant_w1.valid_move(81))
        self.assertTrue(self.elephant_w1.valid_move(85))
        self.assertTrue(self.elephant_w2.valid_move(89))
        self.assertTrue(self.elephant_w2.valid_move(85))

        self.elephant_w1.position = 81 
        self.elephant_w2.position = 89

        self.assertTrue(self.elephant_w1.valid_move(63))
        self.assertTrue(self.elephant_w1.valid_move(103))
        self.assertTrue(self.elephant_w2.valid_move(107))
        self.assertTrue(self.elephant_w2.valid_move(67))    

        self.elephant_w1.position = 63
        self.elephant_w2.position = 67

        self.assertTrue(self.elephant_w1.valid_move(81))
        self.assertTrue(self.elephant_w1.valid_move(85))
        self.assertTrue(self.elephant_w2.valid_move(85))
        self.assertTrue(self.elephant_w2.valid_move(89))    

        self.elephant_w1.position = 85
        self.assertTrue(self.elephant_w1.valid_move(63))
        self.assertTrue(self.elephant_w1.valid_move(67))
        self.assertTrue(self.elephant_w1.valid_move(103))
        self.assertTrue(self.elephant_w1.valid_move(107))

    def test_elephant_black_territory(self):
        self.assertTrue(self.elephant_b1.valid_move(31))
        self.assertTrue(self.elephant_b1.valid_move(35))
        self.assertTrue(self.elephant_b2.valid_move(39))
        self.assertTrue(self.elephant_b2.valid_move(35))

        self.elephant_b1.position = 31 
        self.elephant_b2.position = 39

        self.assertTrue(self.elephant_b1.valid_move(53))
        self.assertTrue(self.elephant_b1.valid_move(13))
        self.assertTrue(self.elephant_b2.valid_move(17))
        self.assertTrue(self.elephant_b2.valid_move(57))    

        self.elephant_b1.position = 53
        self.elephant_b2.position = 57

        self.assertTrue(self.elephant_b1.valid_move(31))
        self.assertTrue(self.elephant_b1.valid_move(35))
        self.assertTrue(self.elephant_b2.valid_move(35))
        self.assertTrue(self.elephant_b2.valid_move(39))    

        self.elephant_b1.position = 35
        self.assertTrue(self.elephant_b1.valid_move(53))
        self.assertTrue(self.elephant_b1.valid_move(57))
        self.assertTrue(self.elephant_b1.valid_move(13))
        self.assertTrue(self.elephant_b1.valid_move(17))

    def test_elephant_in_enemy_territory(self):
        pass 

class TestGeneralVerifier(TestCase):
    def setUp(self): 
        self.general_w1 = General('G',0)
        self.general_b1 = General('g',0)
        self.white_palace = WHITE_PALACE_BOUNDARY.copy() 
        self.black_palace = BLACK_PALACE_BOUNDARY.copy() 

    def test_general_white_palace(self):
        self.assertTrue(self.general_w1.valid_move(95))
        self.assertTrue(self.general_w1.valid_move(104))
        self.assertTrue(self.general_w1.valid_move(106))

        temp_white = [i for i in self.white_palace if i not in [95, 104, 106]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc))   

        self.general_w1.position = 104
        self.assertTrue(self.general_w1.valid_move(94))
        self.assertTrue(self.general_w1.valid_move(105))

        temp_white = [i for i in self.white_palace if i not in [94, 105]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc)) 

        self.general_w1.position = 106
        self.assertTrue(self.general_w1.valid_move(96))
        self.assertTrue(self.general_w1.valid_move(105))

        temp_white = [i for i in self.white_palace if i not in [96, 105]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc)) 

        self.general_w1.position = 84
        self.assertTrue(self.general_w1.valid_move(94))
        self.assertTrue(self.general_w1.valid_move(85))

        temp_white = [i for i in self.white_palace if i not in [94, 85]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc)) 

        self.general_w1.position = 86
        self.assertTrue(self.general_w1.valid_move(96))
        self.assertTrue(self.general_w1.valid_move(85))

        temp_white = [i for i in self.white_palace if i not in [96, 85]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc)) 

        self.general_w1.position = 85
        self.assertTrue(self.general_w1.valid_move(95))
        self.assertTrue(self.general_w1.valid_move(84))
        self.assertTrue(self.general_w1.valid_move(86))

        temp_white = [i for i in self.white_palace if i not in [95, 84, 86]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc))   

        self.general_w1.position=94
        self.assertTrue(self.general_w1.valid_move(95))
        self.assertTrue(self.general_w1.valid_move(84))
        self.assertTrue(self.general_w1.valid_move(104))

        temp_white = [i for i in self.white_palace if i not in [95, 84, 104]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc)) 

        self.general_w1.position=96
        self.assertTrue(self.general_w1.valid_move(95))
        self.assertTrue(self.general_w1.valid_move(86))
        self.assertTrue(self.general_w1.valid_move(106))

        temp_white = [i for i in self.white_palace if i not in [95, 86, 106]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc))   

        self.general_w1.position=95
        self.assertTrue(self.general_w1.valid_move(85))
        self.assertTrue(self.general_w1.valid_move(105))
        self.assertTrue(self.general_w1.valid_move(94))
        self.assertTrue(self.general_w1.valid_move(96))

        temp_white = [i for i in self.white_palace if i not in [85, 94, 96, 105]]
        for loc in temp_white: 
            self.assertFalse(self.general_w1.valid_move(loc))  

    def test_general_black_palace(self):
        self.assertTrue(self.general_b1.valid_move(25))
        self.assertTrue(self.general_b1.valid_move(14))
        self.assertTrue(self.general_b1.valid_move(16))

        temp_black = [i for i in self.white_palace if i not in [25, 14, 16]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc))   

        self.general_b1.position = 14
        self.assertTrue(self.general_b1.valid_move(24))
        self.assertTrue(self.general_b1.valid_move(15))

        temp_black = [i for i in self.white_palace if i not in [24, 15]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc)) 

        self.general_b1.position = 16
        self.assertTrue(self.general_b1.valid_move(26))
        self.assertTrue(self.general_b1.valid_move(15))

        temp_black = [i for i in self.white_palace if i not in [26, 15]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc)) 

        self.general_b1.position = 34
        self.assertTrue(self.general_b1.valid_move(24))
        self.assertTrue(self.general_b1.valid_move(35))

        temp_black = [i for i in self.white_palace if i not in [24, 35]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc)) 

        self.general_b1.position = 36
        self.assertTrue(self.general_b1.valid_move(26))
        self.assertTrue(self.general_b1.valid_move(35))

        temp_black = [i for i in self.white_palace if i not in [26, 35]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc)) 

        self.general_b1.position = 35
        self.assertTrue(self.general_b1.valid_move(25))
        self.assertTrue(self.general_b1.valid_move(34))
        self.assertTrue(self.general_b1.valid_move(36))

        temp_black = [i for i in self.white_palace if i not in [25, 34, 36]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc))   

        self.general_b1.position=24
        self.assertTrue(self.general_b1.valid_move(25))
        self.assertTrue(self.general_b1.valid_move(34))
        self.assertTrue(self.general_b1.valid_move(14))

        temp_black = [i for i in self.white_palace if i not in [25, 34, 14]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc)) 

        self.general_b1.position=26
        self.assertTrue(self.general_b1.valid_move(25))
        self.assertTrue(self.general_b1.valid_move(36))
        self.assertTrue(self.general_b1.valid_move(16))

        temp_black = [i for i in self.white_palace if i not in [25, 36, 16]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc))   

        self.general_b1.position=25
        self.assertTrue(self.general_b1.valid_move(35))
        self.assertTrue(self.general_b1.valid_move(15))
        self.assertTrue(self.general_b1.valid_move(24))
        self.assertTrue(self.general_b1.valid_move(26))

        temp_black = [i for i in self.white_palace if i not in [35, 24, 26, 15]]
        for loc in temp_black: 
            self.assertFalse(self.general_b1.valid_move(loc))  

class TestHorseVerifier(TestCase):
    def setUp(self):
        self.horse_w1 = Horse('H', 0)
        self.horse_w2 = Horse('H', 1)
        self.horse_b1 = Horse('h', 0)
        self.horse_b2 = Horse('h', 1)

class TestPawnVerifier(TestCase):
    def setUp(self):
        self.pawn_w1 = Pawn('P', 0)
        self.pawn_w2 = Pawn('P', 1)
        self.pawn_w3 = Pawn('P', 2)
        self.pawn_w4 = Pawn('P', 3)
        self.pawn_w5 = Pawn('P', 4)

        self.pawn_b1 = Pawn('p', 0)
        self.pawn_b2 = Pawn('p', 1)
        self.pawn_b3 = Pawn('p', 2)
        self.pawn_b4 = Pawn('p', 3)
        self.pawn_b5 = Pawn('p', 4)



class TestRockVerifier(TestCase):
    def setUp(self):
        self.rock_w1 = Rock('R', 0)
        self.rock_w2 = Rock('R', 1)
        self.rock_b1 = Rock('r', 0)
        self.rock_b2 = Rock('r', 1)
