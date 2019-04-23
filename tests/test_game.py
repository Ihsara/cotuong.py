'''
Test Game object in cotuong.py
'''

from unittest import TestCase
from cotuong_const import board_matrix, start_coords_2
from cotuong import GameState


class TestGame(TestCase):
    def setUp(self):
        self.new_game = GameState()

    def test_create_fresh_game(self):
        new_game = GameState()
        self.assertEqual(new_game.board_matrix, board_matrix)
        self.assertEqual(new_game.history, [])
        self.assertEqual(new_game.next_move, 'w')
        self.assertEqual(new_game.turn, 1)

        new_game.new_game()
        self.assertEqual(new_game.board_matrix, board_matrix)
        self.assertEqual(new_game.history, [])
        self.assertEqual(new_game.next_move, 'w')
        self.assertEqual(new_game.turn, 1)

    def test_create_game_with_fen(self):
        pass

    def test_create_game_with_dict(self):
        pass

    def test_update_current_turn(self):
        pass

    def test_game_history(self):
        pass
