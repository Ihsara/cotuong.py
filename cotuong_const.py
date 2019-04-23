w = 'w'
b = 'b'
advisor = 'a'
cannon = 'c'
elephant = 'e'
general = 'g'
horse = 'h'
pawn = 'p'
rock = 'r'

OFFICIAL_NAMES = {
    'a': 'Advisor', 
    'c': 'Cannon', 
    'e': 'Elephant', 
    'g': 'General',
    'h': 'Horse',
    'p': 'Pawn',
    'r': 'Rock'
}

DESTINATION = 'destination'
VERTICAL = 'vertical'
HORIZONTAL = 'horizontal'
DIAGONAL_LEFT_DESC = 'diagonal_left_descend_to_right'
DIAGONAL_LEFT_ASCE = 'diagonal_right_ascend_to_right'
LSHAPE = 'lshape'
BLOCKING_TYPES = {
    1: DESTINATION,
    2: VERTICAL,
    3: HORIZONTAL,
    4: DIAGONAL_LEFT_DESC,
    5: DIAGONAL_LEFT_ASCE,
    6: LSHAPE
}
BLOCKING_RULES = {
    DESTINATION: lambda curr_pos, target_pos: [target_pos], 
    VERTICAL: lambda curr_pos, target_pos: list(range(curr_pos, target_pos+1, 10)) if target_pos > curr_pos else list(range(target_pos, curr_pos+1, 10)),
    HORIZONTAL: lambda curr_pos, target_pos: list(range(curr_pos, target_pos+1)) if target_pos > curr_pos else list(range(target_pos, curr_pos+1)),
    DIAGONAL_LEFT_DESC: lambda curr_pos, target_pos: list(range(curr_pos, target_pos, 11)) if target_pos > curr_pos else list(range(target_pos, curr_pos, 11)),
    DIAGONAL_LEFT_ASCE: lambda curr_pos, target_pos: list(range(curr_pos, target_pos, 9)) if target_pos > curr_pos else list(range(target_pos, curr_pos, 9)),
    LSHAPE: lambda curr_pos, target_pos: [curr_pos + 1] if target_pos%10 - 2 == curr_pos%10 else ([curr_pos -1] if target_pos%10 + 2 == curr_pos%10 else([curr_pos -10] if target_pos//10 - 2 == curr_pos//10 else [curr_pos + 10]))
}

INVALID_POS = -1110

start_coords = {
    w: {
        advisor: [104, 106],
        cannon: [82, 88],
        elephant: [103, 107],
        general: [105],
        horse: [102, 108],
        pawn: [71, 73, 75, 77, 79],
        rock: [101, 109]
    },
    b: {
        advisor: [14, 16],
        cannon: [32, 38],
        elephant: [13, 17],
        general: [15],
        horse: [12, 18],
        pawn: [41, 43, 45, 47, 49],
        rock: [11, 19]
    }
}

start_coords_2 = {
    'A': [104, 106],
    'C': [82, 88],
    'E': [103, 107],
    'G': [105],
    'H': [102, 108],
    'P': [71, 73, 75, 77, 79],
    'R': [101, 109],
    'a': [14, 16],
    'c': [32, 38],
    'e': [13, 17],
    'g': [15],
    'h': [12, 18],
    'p': [41, 43, 45, 47, 49],
    'r': [11, 19]
}

board_matrix = [
    [0,  1,  2,  3,  4,  5,  6,  7,  8,  9,  10],
    [10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 110],
    [20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 210],
    [30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 310],
    [40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 410],
    [50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 510],
    [60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 610],
    [70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 710],
    [80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 810],
    [90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 910],
    [100, 101, 102, 103, 104, 105, 106, 107, 108, 109, 1010],
    [110, 111, 112, 113, 114, 115, 116, 117, 118, 119, 1110]
]

BOARD_LOC_NUM = [i for i in range(11, 110) if i % 10 != 0]
WHITE_TERRITORY_LOC_NUM = [i for i in BOARD_LOC_NUM if i>= 61]
BLACK_TERRITORY_LOC_NUM = [i for i in BOARD_LOC_NUM if i<= 59]

BLACK_PALACE_BOUNDARY = [14, 15, 16, 24, 25, 26, 34, 35, 36]
WHITE_PALACE_BOUNDARY = [84, 85, 86, 94, 95, 96, 104, 105, 106]

MOVE_VERTICALLY_ONE_UNIT_FWD = {w: -10, b: 10}
MOVE_VERTICALLY_ONE_UNIT_BWD = {w: 10, b: -10}
MOVE_HORIZONTALLY_ONE_UNIT_LEFT = {w: -1, b: 1}
MOVE_HORIZONTALLY_ONE_UNIT_RIGHT = {w: 1, b: -1}
