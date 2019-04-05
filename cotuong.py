from cotuong_const import board_matrix, start_coords_2 
from copy import deepcopy

BOARD_MATRIX = deepcopy(board_matrix)
START_COORDS = deepcopy(start_coords_2)

class Game: 
    def __init__(self):       
        self.SYMBOLS = 'aceghprACEGHPR'
        self.ALLOWED_MOVE_ORDER = '.-/'
        self.EMPTY = ' '
        self.BORDER = "|"
        self.nex_move = 'w'
        self.board_matrix = deepcopy(BOARD_MATRIX)
        self.start_coords = deepcopy(START_COORDS)
        self.game_state = []
        
    def new_game(self):
        self.game_state = deepcopy(self.start_coords)
        self.next_move = 'w'
        return self.game_state
    
    def _translate_move(self, move): #move is a string 'H2.4' means horse 2 move forth to 4 
        if move[0].islower() and self.next_move == 'w':
            translated_move = self._translate_move_red(move)
        elif move[0].isupper() and self.next_move == 'b':
            translated_move = self._translate_move_black(move)
        else: raise ValueError('Move cannot be proccessed!')
            
    def _translate_move_red(self, move):
        pass 
    
    def _translate_move_black(self,move):
        pass
    
    def _update_move(self):
        pass 
            
    def verify(self, move): 
        return len(move) == 4 and move[0] in self.SYMBOLS and move[2] in self.ALLOWED_MOVE_ORDER and 1 <= int(move[1]) <= 9 and 1 <= int(move[3]) <= 9 
    
    def _make_border_show(self, board):
        for i in range(1,len(board[0])): 
            if i < len(board[0])-1:
                board[0][i] = str(i)
                board[11][i] = str(len(board[0]) -1- i)
            board[i][0] = str(i)
            board[i][10] = str(i)
        return board 
    
    def _make_empty_space_show(self, board): 
        for i in range(12): 
            for j in range(11):
                if isinstance(board[i][j], int): 
                    board[i][j] = self.EMPTY
        return board
            
    def _make_board(self): 
        board = deepcopy(self.board_matrix)
        board = self._make_border_show(board) 
        for piece in self.game_state: 
            for val in self.game_state[piece]:
                board[val//10][val%10] = piece 
        board = self._make_empty_space_show(board)
        return board
    
    def display_board(self):
        pass
    
    def play(self):
        pass 