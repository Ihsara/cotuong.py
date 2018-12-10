"""
Test Game objects when display on cli 
"""

from unittest import TestCase
from pprint import pprint

from cotuong import Game 

class GameInCLI(TestCase):
    def setUp(self): 
        self.game = Game()

    def test_starter_pos_in_cli(self):
        pprint(self.game.cli_view())