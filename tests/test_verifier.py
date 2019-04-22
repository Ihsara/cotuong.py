from unittest import TestCase

from cotuong_const import BLACK_PALACE_BOUNDARY, WHITE_PALACE_BOUNDARY, board_matrix
from cotuong_const import BLACK_TERRITORY_LOC_NUM, WHITE_TERRITORY_LOC_NUM
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
            for col_incre in range(0, 100, 10):
                self.piece.position = pos + col_incre
                self.assertTrue(self.piece.is_inboard())

        self.assertFalse(self.piece.is_inboard(next_pos=112))
        self.assertFalse(self.piece.is_inboard(next_pos=114))
        self.assertFalse(self.piece.is_inboard(next_pos=1110))
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
            for col_incre in range(0, 100, 10):
                self.piece.position = pos + col_incre
                if pos+col_incre in BLACK_PALACE_BOUNDARY:
                    self.assertTrue(self.piece.is_in_black_palace())
                else:
                    self.assertFalse(self.piece.is_in_black_palace())

    def test_in_white_palace(self):
        for pos in self.pos_inboard_upperbound:
            for col_incre in range(0, 100, 10):
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
        self.cannon_w1 = Cannon('C', 0)
        self.cannon_w2 = Cannon('C', 1)
        self.cannon_b1 = Cannon('c', 0)
        self.cannon_b2 = Cannon('c', 1)

    def test_cannon_move_vertically(self):
        self.assertEqual(self.cannon_w1.position, 82)
        self.assertEqual(self.cannon_w2.position, 88)
        self.assertEqual(self.cannon_b1.position, 32)
        self.assertEqual(self.cannon_b2.position, 38)

        for row in board_matrix:
            for col in row:
                if 109 >= col >= 11 and col % 10 != 0:
                    for delta in range(1, 10):
                        self.cannon_w1.position = col
                        if self.cannon_w1.is_inboard(col + delta*10):
                            self.assertTrue(
                                self.cannon_w1.valid_move(col + delta*10))
                        else:
                            self.assertFalse(
                                self.cannon_w1.valid_move(col + delta*10))

    def test_cannon_move_horinzontally(self):
        self.assertEqual(self.cannon_w1.position, 82)
        self.assertEqual(self.cannon_w2.position, 88)
        self.assertEqual(self.cannon_b1.position, 32)
        self.assertEqual(self.cannon_b2.position, 38)

        for row in board_matrix:
            for col in row:
                if 109 >= col >= 11 and col % 10 != 0:
                    self.cannon_b1.position = col
                    for horinz_delta in row:
                        if horinz_delta != col and 109 >= horinz_delta >= 11 and horinz_delta % 10 != 0:
                            self.assertTrue(
                                self.cannon_b1.valid_move(horinz_delta))


class TestElephantVerifier(TestCase):
    def setUp(self):
        self.elephant_w1 = Elephant('E', 0)
        self.elephant_w2 = Elephant('E', 1)
        self.elephant_b1 = Elephant('e', 0)
        self.elephant_b2 = Elephant('e', 1)

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
        self.general_w1 = General('G', 0)
        self.general_b1 = General('g', 0)
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

        self.general_w1.position = 94
        self.assertTrue(self.general_w1.valid_move(95))
        self.assertTrue(self.general_w1.valid_move(84))
        self.assertTrue(self.general_w1.valid_move(104))

        temp_white = [i for i in self.white_palace if i not in [95, 84, 104]]
        for loc in temp_white:
            self.assertFalse(self.general_w1.valid_move(loc))

        self.general_w1.position = 96
        self.assertTrue(self.general_w1.valid_move(95))
        self.assertTrue(self.general_w1.valid_move(86))
        self.assertTrue(self.general_w1.valid_move(106))

        temp_white = [i for i in self.white_palace if i not in [95, 86, 106]]
        for loc in temp_white:
            self.assertFalse(self.general_w1.valid_move(loc))

        self.general_w1.position = 95
        self.assertTrue(self.general_w1.valid_move(85))
        self.assertTrue(self.general_w1.valid_move(105))
        self.assertTrue(self.general_w1.valid_move(94))
        self.assertTrue(self.general_w1.valid_move(96))

        temp_white = [
            i for i in self.white_palace if i not in [85, 94, 96, 105]]
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

        self.general_b1.position = 24
        self.assertTrue(self.general_b1.valid_move(25))
        self.assertTrue(self.general_b1.valid_move(34))
        self.assertTrue(self.general_b1.valid_move(14))

        temp_black = [i for i in self.white_palace if i not in [25, 34, 14]]
        for loc in temp_black:
            self.assertFalse(self.general_b1.valid_move(loc))

        self.general_b1.position = 26
        self.assertTrue(self.general_b1.valid_move(25))
        self.assertTrue(self.general_b1.valid_move(36))
        self.assertTrue(self.general_b1.valid_move(16))

        temp_black = [i for i in self.white_palace if i not in [25, 36, 16]]
        for loc in temp_black:
            self.assertFalse(self.general_b1.valid_move(loc))

        self.general_b1.position = 25
        self.assertTrue(self.general_b1.valid_move(35))
        self.assertTrue(self.general_b1.valid_move(15))
        self.assertTrue(self.general_b1.valid_move(24))
        self.assertTrue(self.general_b1.valid_move(26))

        temp_black = [
            i for i in self.white_palace if i not in [35, 24, 26, 15]]
        for loc in temp_black:
            self.assertFalse(self.general_b1.valid_move(loc))


class TestHorseVerifier(TestCase):
    def setUp(self):
        self.horse_w1 = Horse('H', 0)
        self.horse_w2 = Horse('H', 1)
        self.horse_b1 = Horse('h', 0)
        self.horse_b2 = Horse('h', 1)

    def test_horse_two_side_blocked_northwest(self):
        self.horse_w1.position = 22
        self.assertTrue(self.horse_w1.valid_move(14))
        self.assertTrue(self.horse_w1.valid_move(34))
        self.assertTrue(self.horse_w1.valid_move(43))
        self.assertTrue(self.horse_w1.valid_move(41))
        self.assertFalse(self.horse_w1.valid_move(10))
        self.assertFalse(self.horse_w1.valid_move(1))
        self.assertFalse(self.horse_w1.valid_move(3))
        self.assertFalse(self.horse_w1.valid_move(30))

        self.horse_w1.position = 11
        self.assertTrue(self.horse_w1.valid_move(23))
        self.assertTrue(self.horse_w1.valid_move(32))
        self.assertFalse(self.horse_w1.valid_move(3))
        self.assertFalse(self.horse_w1.valid_move(30))

        self.horse_w1.position = 21
        self.assertTrue(self.horse_w1.valid_move(42))
        self.assertTrue(self.horse_w1.valid_move(33))
        self.assertTrue(self.horse_w1.valid_move(13))
        self.assertFalse(self.horse_w1.valid_move(40))
        self.assertFalse(self.horse_w1.valid_move(2))
        self.assertFalse(self.horse_w1.valid_move(0))

        self.horse_w1.position = 12
        self.assertTrue(self.horse_w1.valid_move(24))
        self.assertTrue(self.horse_w1.valid_move(33))
        self.assertTrue(self.horse_w1.valid_move(31))
        self.assertFalse(self.horse_w1.valid_move(4))
        self.assertFalse(self.horse_w1.valid_move(20))
        self.assertFalse(self.horse_w1.valid_move(0))

    def test_horse_two_side_blocked_northeast(self):
        self.horse_w1.position = 28
        self.assertTrue(self.horse_w1.valid_move(49))
        self.assertTrue(self.horse_w1.valid_move(47))
        self.assertTrue(self.horse_w1.valid_move(36))
        self.assertTrue(self.horse_w1.valid_move(16))
        self.assertFalse(self.horse_w1.valid_move(7))
        self.assertFalse(self.horse_w1.valid_move(9))
        self.assertFalse(self.horse_w1.valid_move(110))
        self.assertFalse(self.horse_w1.valid_move(310))

        self.horse_w1.position = 19
        self.assertTrue(self.horse_w1.valid_move(27))
        self.assertTrue(self.horse_w1.valid_move(38))
        self.assertFalse(self.horse_w1.valid_move(7))
        self.assertFalse(self.horse_w1.valid_move(310))

        self.horse_w1.position = 18
        self.assertTrue(self.horse_w1.valid_move(26))
        self.assertTrue(self.horse_w1.valid_move(37))
        self.assertTrue(self.horse_w1.valid_move(39))
        self.assertFalse(self.horse_w1.valid_move(6))
        self.assertFalse(self.horse_w1.valid_move(10))
        self.assertFalse(self.horse_w1.valid_move(210))

        self.horse_w1.position = 29
        self.assertTrue(self.horse_w1.valid_move(48))
        self.assertTrue(self.horse_w1.valid_move(37))
        self.assertTrue(self.horse_w1.valid_move(17))
        self.assertFalse(self.horse_w1.valid_move(8))
        self.assertFalse(self.horse_w1.valid_move(10))
        self.assertFalse(self.horse_w1.valid_move(410))

    def test_horse_two_side_blocked_southeast(self):
        self.horse_w1.position = 98
        self.assertTrue(self.horse_w1.valid_move(106))
        self.assertTrue(self.horse_w1.valid_move(86))
        self.assertTrue(self.horse_w1.valid_move(77))
        self.assertTrue(self.horse_w1.valid_move(79))
        self.assertFalse(self.horse_w1.valid_move(810))
        self.assertFalse(self.horse_w1.valid_move(119))
        self.assertFalse(self.horse_w1.valid_move(117))
        self.assertFalse(self.horse_w1.valid_move(1010))

        self.horse_w1.position = 109
        self.assertTrue(self.horse_w1.valid_move(88))
        self.assertTrue(self.horse_w1.valid_move(97))
        self.assertFalse(self.horse_w1.valid_move(810))
        self.assertFalse(self.horse_w1.valid_move(117))

        self.horse_w1.position = 108
        self.assertTrue(self.horse_w1.valid_move(96))
        self.assertTrue(self.horse_w1.valid_move(87))
        self.assertTrue(self.horse_w1.valid_move(89))
        self.assertFalse(self.horse_w1.valid_move(116))
        self.assertFalse(self.horse_w1.valid_move(1110))
        self.assertFalse(self.horse_w1.valid_move(910))

        self.horse_w1.position = 99
        self.assertTrue(self.horse_w1.valid_move(107))
        self.assertTrue(self.horse_w1.valid_move(87))
        self.assertTrue(self.horse_w1.valid_move(78))
        self.assertFalse(self.horse_w1.valid_move(710))
        self.assertFalse(self.horse_w1.valid_move(1110))
        self.assertFalse(self.horse_w1.valid_move(118))

    def test_horse_two_side_blocked_southwest(self):
        self.horse_w1.position = 92
        self.assertTrue(self.horse_w1.valid_move(71))
        self.assertTrue(self.horse_w1.valid_move(73))
        self.assertTrue(self.horse_w1.valid_move(84))
        self.assertTrue(self.horse_w1.valid_move(104))
        self.assertFalse(self.horse_w1.valid_move(80))
        self.assertFalse(self.horse_w1.valid_move(100))
        self.assertFalse(self.horse_w1.valid_move(111))
        self.assertFalse(self.horse_w1.valid_move(113))

        self.horse_w1.position = 101
        self.assertTrue(self.horse_w1.valid_move(82))
        self.assertTrue(self.horse_w1.valid_move(93))
        self.assertFalse(self.horse_w1.valid_move(80))
        self.assertFalse(self.horse_w1.valid_move(113))

        self.horse_w1.position = 91
        self.assertTrue(self.horse_w1.valid_move(72))
        self.assertTrue(self.horse_w1.valid_move(83))
        self.assertTrue(self.horse_w1.valid_move(103))
        self.assertFalse(self.horse_w1.valid_move(70))
        self.assertFalse(self.horse_w1.valid_move(110))
        self.assertFalse(self.horse_w1.valid_move(119))

        self.horse_w1.position = 102
        self.assertTrue(self.horse_w1.valid_move(81))
        self.assertTrue(self.horse_w1.valid_move(83))
        self.assertTrue(self.horse_w1.valid_move(94))
        self.assertFalse(self.horse_w1.valid_move(114))
        self.assertFalse(self.horse_w1.valid_move(110))
        self.assertFalse(self.horse_w1.valid_move(90))

    def test_horse_one_side_block_southern(self):
        self.horse_w2.position = 93
        self.assertTrue(self.horse_w2.valid_move(101))
        self.assertTrue(self.horse_w2.valid_move(81))
        self.assertTrue(self.horse_w2.valid_move(72))
        self.assertTrue(self.horse_w2.valid_move(74))
        self.assertTrue(self.horse_w2.valid_move(85))
        self.assertTrue(self.horse_w2.valid_move(105))
        self.assertFalse(self.horse_w2.valid_move(112))
        self.assertFalse(self.horse_w2.valid_move(114))

        self.horse_w2.position = 97
        self.assertTrue(self.horse_w2.valid_move(109))
        self.assertTrue(self.horse_w2.valid_move(89))
        self.assertTrue(self.horse_w2.valid_move(78))
        self.assertTrue(self.horse_w2.valid_move(76))
        self.assertTrue(self.horse_w2.valid_move(85))
        self.assertTrue(self.horse_w2.valid_move(105))
        self.assertFalse(self.horse_w2.valid_move(116))
        self.assertFalse(self.horse_w2.valid_move(118))

        self.horse_w2.position = 95
        self.assertTrue(self.horse_w2.valid_move(103))
        self.assertTrue(self.horse_w2.valid_move(83))
        self.assertTrue(self.horse_w2.valid_move(74))
        self.assertTrue(self.horse_w2.valid_move(76))
        self.assertTrue(self.horse_w2.valid_move(87))
        self.assertTrue(self.horse_w2.valid_move(107))
        self.assertFalse(self.horse_w2.valid_move(114))
        self.assertFalse(self.horse_w2.valid_move(116))

    def test_horse_one_side_block_eastern(self):
        self.horse_w2.position = 88
        self.assertTrue(self.horse_w2.valid_move(69))
        self.assertTrue(self.horse_w2.valid_move(67))
        self.assertTrue(self.horse_w2.valid_move(76))
        self.assertTrue(self.horse_w2.valid_move(96))
        self.assertTrue(self.horse_w2.valid_move(107))
        self.assertTrue(self.horse_w2.valid_move(109))
        self.assertFalse(self.horse_w2.valid_move(910))
        self.assertFalse(self.horse_w2.valid_move(710))

        self.horse_w2.position = 38
        self.assertTrue(self.horse_w2.valid_move(19))
        self.assertTrue(self.horse_w2.valid_move(17))
        self.assertTrue(self.horse_w2.valid_move(26))
        self.assertTrue(self.horse_w2.valid_move(46))
        self.assertTrue(self.horse_w2.valid_move(57))
        self.assertTrue(self.horse_w2.valid_move(59))
        self.assertFalse(self.horse_w2.valid_move(210))
        self.assertFalse(self.horse_w2.valid_move(410))

        self.horse_w2.position = 68
        self.assertTrue(self.horse_w2.valid_move(49))
        self.assertTrue(self.horse_w2.valid_move(47))
        self.assertTrue(self.horse_w2.valid_move(56))
        self.assertTrue(self.horse_w2.valid_move(76))
        self.assertTrue(self.horse_w2.valid_move(87))
        self.assertTrue(self.horse_w2.valid_move(89))
        self.assertFalse(self.horse_w2.valid_move(114))
        self.assertFalse(self.horse_w2.valid_move(116))

    def test_horse_one_side_block_western(self):
        self.horse_w2.position = 82
        self.assertTrue(self.horse_w2.valid_move(101))
        self.assertTrue(self.horse_w2.valid_move(94))
        self.assertTrue(self.horse_w2.valid_move(63))
        self.assertTrue(self.horse_w2.valid_move(74))
        self.assertTrue(self.horse_w2.valid_move(61))
        self.assertTrue(self.horse_w2.valid_move(103))
        self.assertFalse(self.horse_w2.valid_move(70))
        self.assertFalse(self.horse_w2.valid_move(90))

        self.horse_w2.position = 32
        self.assertTrue(self.horse_w2.valid_move(11))
        self.assertTrue(self.horse_w2.valid_move(13))
        self.assertTrue(self.horse_w2.valid_move(24))
        self.assertTrue(self.horse_w2.valid_move(44))
        self.assertTrue(self.horse_w2.valid_move(53))
        self.assertTrue(self.horse_w2.valid_move(51))
        self.assertFalse(self.horse_w2.valid_move(20))
        self.assertFalse(self.horse_w2.valid_move(40))

        self.horse_w2.position = 52
        self.assertTrue(self.horse_w2.valid_move(31))
        self.assertTrue(self.horse_w2.valid_move(33))
        self.assertTrue(self.horse_w2.valid_move(44))
        self.assertTrue(self.horse_w2.valid_move(64))
        self.assertTrue(self.horse_w2.valid_move(73))
        self.assertTrue(self.horse_w2.valid_move(71))
        self.assertFalse(self.horse_w2.valid_move(40))
        self.assertFalse(self.horse_w2.valid_move(60))

    def test_horse_one_side_block_northern(self):
        self.horse_w2.position = 23
        self.assertTrue(self.horse_w2.valid_move(11))
        self.assertTrue(self.horse_w2.valid_move(31))
        self.assertTrue(self.horse_w2.valid_move(42))
        self.assertTrue(self.horse_w2.valid_move(44))
        self.assertTrue(self.horse_w2.valid_move(35))
        self.assertTrue(self.horse_w2.valid_move(15))
        self.assertFalse(self.horse_w2.valid_move(2))
        self.assertFalse(self.horse_w2.valid_move(4))

        self.horse_w2.position = 27
        self.assertTrue(self.horse_w2.valid_move(19))
        self.assertTrue(self.horse_w2.valid_move(39))
        self.assertTrue(self.horse_w2.valid_move(48))
        self.assertTrue(self.horse_w2.valid_move(46))
        self.assertTrue(self.horse_w2.valid_move(35))
        self.assertTrue(self.horse_w2.valid_move(15))
        self.assertFalse(self.horse_w2.valid_move(6))
        self.assertFalse(self.horse_w2.valid_move(8))

        self.horse_w2.position = 25
        self.assertTrue(self.horse_w2.valid_move(13))
        self.assertTrue(self.horse_w2.valid_move(33))
        self.assertTrue(self.horse_w2.valid_move(44))
        self.assertTrue(self.horse_w2.valid_move(46))
        self.assertTrue(self.horse_w2.valid_move(37))
        self.assertTrue(self.horse_w2.valid_move(17))
        self.assertFalse(self.horse_w2.valid_move(4))
        self.assertFalse(self.horse_w2.valid_move(6))

    def test_horse_arrive_at_edges(self):
        self.horse_b1.position = 33
        self.assertTrue(self.horse_b1.valid_move(12))
        self.assertTrue(self.horse_b1.valid_move(14))
        self.assertTrue(self.horse_b1.valid_move(25))
        self.assertTrue(self.horse_b1.valid_move(45))
        self.assertTrue(self.horse_b1.valid_move(54))
        self.assertTrue(self.horse_b1.valid_move(52))
        self.assertTrue(self.horse_b1.valid_move(41))
        self.assertTrue(self.horse_b1.valid_move(21))

        self.horse_b1.position = 37
        self.assertTrue(self.horse_b1.valid_move(16))
        self.assertTrue(self.horse_b1.valid_move(18))
        self.assertTrue(self.horse_b1.valid_move(29))
        self.assertTrue(self.horse_b1.valid_move(49))
        self.assertTrue(self.horse_b1.valid_move(58))
        self.assertTrue(self.horse_b1.valid_move(56))
        self.assertTrue(self.horse_b1.valid_move(45))
        self.assertTrue(self.horse_b1.valid_move(25))

        self.horse_b1.position = 87
        self.assertTrue(self.horse_b1.valid_move(66))
        self.assertTrue(self.horse_b1.valid_move(68))
        self.assertTrue(self.horse_b1.valid_move(79))
        self.assertTrue(self.horse_b1.valid_move(99))
        self.assertTrue(self.horse_b1.valid_move(108))
        self.assertTrue(self.horse_b1.valid_move(106))
        self.assertTrue(self.horse_b1.valid_move(95))
        self.assertTrue(self.horse_b1.valid_move(75))

        self.horse_b1.position = 83
        self.assertTrue(self.horse_b1.valid_move(62))
        self.assertTrue(self.horse_b1.valid_move(64))
        self.assertTrue(self.horse_b1.valid_move(75))
        self.assertTrue(self.horse_b1.valid_move(95))
        self.assertTrue(self.horse_b1.valid_move(104))
        self.assertTrue(self.horse_b1.valid_move(102))
        self.assertTrue(self.horse_b1.valid_move(91))
        self.assertTrue(self.horse_b1.valid_move(71))

    def test_horse_normal_position(self):
        self.horse_b2.position = 44
        valid_move = [23, 25, 36, 56, 65, 63, 52, 32]
        for pos in valid_move:
            self.assertTrue(self.horse_b2.valid_move(pos))

        for loc in range(22, 67):
            if loc not in valid_move:
                self.assertFalse(self.horse_b2.valid_move(loc))

        self.horse_b2.position = 46
        valid_move = [25, 27, 38, 58, 67, 65, 54, 34]
        for pos in valid_move:
            self.assertTrue(self.horse_b2.valid_move(pos))

        for loc in range(24, 69):
            if loc not in valid_move:
                self.assertFalse(self.horse_b2.valid_move(loc))

        self.horse_b2.position = 76
        valid_move = [55, 57, 68, 88, 97, 95, 84, 64]
        for pos in valid_move:
            self.assertTrue(self.horse_b2.valid_move(pos))

        for loc in range(54, 99):
            if loc not in valid_move:
                self.assertFalse(self.horse_b2.valid_move(loc))

        self.horse_b2.position = 74
        valid_move = [53, 55, 66, 86, 95, 93, 82, 62]
        for pos in valid_move:
            self.assertTrue(self.horse_b2.valid_move(pos))

        for loc in range(52, 97):
            if loc not in valid_move:
                self.assertFalse(self.horse_b2.valid_move(loc))

        self.horse_b2.position = 65
        valid_move = [44, 46, 57, 77, 86, 84, 73, 53]
        for pos in valid_move:
            self.assertTrue(self.horse_b2.valid_move(pos))

        for loc in range(32, 99):
            if loc not in valid_move:
                self.assertFalse(self.horse_b2.valid_move(loc))

        self.horse_b2.position = 55
        valid_move = [34, 36, 47, 67, 76, 74, 63, 43]
        for pos in valid_move:
            self.assertTrue(self.horse_b2.valid_move(pos))

        for loc in range(22, 89):
            if loc not in valid_move:
                self.assertFalse(self.horse_b2.valid_move(loc))


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

    def test_pawn_white_in_white_territory(self):        
        for loc in range (60,90): 
            if loc == 61: 
                self.assertTrue(self.pawn_w1.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w1.valid_move(loc))
        
        for loc in range (60,90): 
            if loc == 63: 
                self.assertTrue(self.pawn_w2.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w2.valid_move(loc))
        
        for loc in range (60,90): 
            if loc == 65: 
                self.assertTrue(self.pawn_w3.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w3.valid_move(loc))
        
        for loc in range (60,90): 
            if loc == 67: 
                self.assertTrue(self.pawn_w4.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w4.valid_move(loc))
        
        for loc in range (60,90): 
            if loc == 69: 
                self.assertTrue(self.pawn_w5.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w5.valid_move(loc))
        
        self.pawn_w1.position = 61
        self.pawn_w2.position = 63
        self.pawn_w3.position = 65
        self.pawn_w4.position = 67
        self.pawn_w5.position = 69

        for loc in range (50,80): 
            if loc == 51: 
                self.assertTrue(self.pawn_w1.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w1.valid_move(loc))
        
        for loc in range (50,80): 
            if loc == 53: 
                self.assertTrue(self.pawn_w2.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w2.valid_move(loc))
        
        for loc in range (50,80): 
            if loc == 55: 
                self.assertTrue(self.pawn_w3.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w3.valid_move(loc))
        
        for loc in range (50,80): 
            if loc == 57: 
                self.assertTrue(self.pawn_w4.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w4.valid_move(loc))
        
        for loc in range (50,80): 
            if loc == 59: 
                self.assertTrue(self.pawn_w5.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_w5.valid_move(loc))

    def test_pawn_black_in_black_territory(self):        
        for loc in range (30,60): 
            if loc == 51: 
                self.assertTrue(self.pawn_b1.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b1.valid_move(loc))
        
        for loc in range (30,60): 
            if loc == 53: 
                self.assertTrue(self.pawn_b2.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b2.valid_move(loc))
        
        for loc in range (30,60): 
            if loc == 55: 
                self.assertTrue(self.pawn_b3.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b3.valid_move(loc))
        
        for loc in range (30,60): 
            if loc == 57: 
                self.assertTrue(self.pawn_b4.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b4.valid_move(loc))
        
        for loc in range (30,60): 
            if loc == 59: 
                self.assertTrue(self.pawn_b5.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b5.valid_move(loc))
        
        self.pawn_b1.position = 51
        self.pawn_b2.position = 53
        self.pawn_b3.position = 55
        self.pawn_b4.position = 57
        self.pawn_b5.position = 59

        for loc in range (40,70): 
            if loc == 61: 
                self.assertTrue(self.pawn_b1.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b1.valid_move(loc))
        
        for loc in range (40,70): 
            if loc == 63: 
                self.assertTrue(self.pawn_b2.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b2.valid_move(loc))
        
        for loc in range (40,70): 
            if loc == 65: 
                self.assertTrue(self.pawn_b3.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b3.valid_move(loc))
        
        for loc in range (40,70): 
            if loc == 67: 
                self.assertTrue(self.pawn_b4.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b4.valid_move(loc))
        
        for loc in range (40,70): 
            if loc == 69: 
                self.assertTrue(self.pawn_b5.valid_move(loc))
            else: 
                self.assertFalse(self.pawn_b5.valid_move(loc))

    def test_white_pawn_in_black_territory(self):
        for loc in BLACK_TERRITORY_LOC_NUM: 
            self.pawn_w1.position = loc 
            if loc%10 != 1 and loc%10 != 9 and loc >= 22:                 
                if not self.pawn_w1.valid_move(loc - 10):
                    print (loc-10, self.pawn_w1.position)
                self.assertTrue(self.pawn_w1.valid_move(loc + 1))
                self.assertTrue(self.pawn_w1.valid_move(loc - 1))
                self.assertTrue(self.pawn_w1.valid_move(loc - 10))
                for loc2 in BLACK_TERRITORY_LOC_NUM: 
                    if loc2 != loc + 1 and loc2 != loc - 1 and loc2 != loc - 10: 
                        self.assertFalse(self.pawn_w1.valid_move(loc2))
            elif loc%10 == 1:
                if loc == 11:                     
                    self.assertTrue(self.pawn_w1.valid_move(loc + 1))
                    self.assertFalse(self.pawn_w1.valid_move(loc - 1))
                    self.assertFalse(self.pawn_w1.valid_move(loc - 10))
                else:                     
                    self.assertTrue(self.pawn_w1.valid_move(loc + 1))
                    self.assertFalse(self.pawn_w1.valid_move(loc - 1))
                    self.assertTrue(self.pawn_w1.valid_move(loc - 10))   
            elif loc%10 == 9: 
                if loc == 19:                    
                    self.assertFalse(self.pawn_w1.valid_move(loc + 1))
                    self.assertTrue(self.pawn_w1.valid_move(loc - 1))
                    self.assertFalse(self.pawn_w1.valid_move(loc - 10))
                else:                     
                    self.assertFalse(self.pawn_w1.valid_move(loc + 1))
                    self.assertTrue(self.pawn_w1.valid_move(loc - 1))
                    self.assertTrue(self.pawn_w1.valid_move(loc - 10))  
            elif loc in range(12, 19): 
                self.assertTrue(self.pawn_w1.valid_move(loc + 1))
                self.assertTrue(self.pawn_w1.valid_move(loc - 1))
                self.assertFalse(self.pawn_w1.valid_move(loc - 10))                    

    def test_black_pawn_in_white_territory(self):
        for loc in WHITE_TERRITORY_LOC_NUM: 
            self.pawn_b1.position = loc 
            if loc%10 != 1 and loc%10 != 9 and loc <= 98:                 
                if not self.pawn_b1.valid_move(loc + 1):
                    print (loc+1, self.pawn_b1.position)
                self.assertTrue(self.pawn_b1.valid_move(loc + 1))
                self.assertTrue(self.pawn_b1.valid_move(loc - 1))
                self.assertTrue(self.pawn_b1.valid_move(loc + 10))
                for loc2 in WHITE_TERRITORY_LOC_NUM: 
                    if loc2 != loc + 1 and loc2 != loc - 1 and loc2 != loc + 10: 
                        self.assertFalse(self.pawn_b1.valid_move(loc2))
            elif loc%10 == 1:
                if loc == 101:                     
                    self.assertTrue(self.pawn_b1.valid_move(loc + 1))
                    self.assertFalse(self.pawn_b1.valid_move(loc - 1))
                    self.assertFalse(self.pawn_b1.valid_move(loc + 10))
                else:                     
                    self.assertTrue(self.pawn_b1.valid_move(loc + 1))
                    self.assertFalse(self.pawn_b1.valid_move(loc - 1))
                    self.assertTrue(self.pawn_b1.valid_move(loc + 10))   
            elif loc%10 == 9: 
                if loc == 109:                    
                    self.assertFalse(self.pawn_b1.valid_move(loc + 1))
                    self.assertTrue(self.pawn_b1.valid_move(loc - 1))
                    self.assertFalse(self.pawn_b1.valid_move(loc + 10))
                else:                     
                    self.assertFalse(self.pawn_b1.valid_move(loc + 1))
                    self.assertTrue(self.pawn_b1.valid_move(loc - 1))
                    self.assertTrue(self.pawn_b1.valid_move(loc + 10)) 
            elif loc in range(102, 109): 
                self.assertTrue(self.pawn_b1.valid_move(loc + 1))
                self.assertTrue(self.pawn_b1.valid_move(loc - 1))
                self.assertFalse(self.pawn_b1.valid_move(loc + 10))                                                    
        
class TestRockVerifier(TestCase):
    def setUp(self):
        self.rock_w1 = Rock('R', 0)
        self.rock_w2 = Rock('R', 1)
        self.rock_b1 = Rock('r', 0)
        self.rock_b2 = Rock('r', 1)

    def test_rock_move_vertically(self):
        self.assertEqual(self.rock_w1.position, 101)
        self.assertEqual(self.rock_w2.position, 109)
        self.assertEqual(self.rock_b1.position, 11)
        self.assertEqual(self.rock_b2.position, 19)

        for row in board_matrix:
            for col in row:
                if 109 >= col >= 11 and col % 10 != 0:
                    for delta in range(1, 10):
                        self.rock_w1.position = col
                        if self.rock_w1.is_inboard(col + delta*10):
                            self.assertTrue(
                                self.rock_w1.valid_move(col + delta*10))
                        else:
                            self.assertFalse(
                                self.rock_w1.valid_move(col + delta*10))

    def test_rock_move_horinzontally(self):
        self.assertEqual(self.rock_w1.position, 101)
        self.assertEqual(self.rock_w2.position, 109)
        self.assertEqual(self.rock_b1.position, 11)
        self.assertEqual(self.rock_b2.position, 19)

        for row in board_matrix:
            for col in row:
                if 109 >= col >= 11 and col % 10 != 0:
                    self.rock_b1.position = col
                    for horinz_delta in row:
                        if horinz_delta != col and 109 >= horinz_delta >= 11 and horinz_delta % 10 != 0:
                            self.assertTrue(
                                self.rock_b1.valid_move(horinz_delta))
