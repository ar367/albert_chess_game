def location2index(loc: str) -> tuple[int, int]:
    '''converts chess location to corresponding x and y coordinates'''
   
    column =  loc.strip()[1]

    alphabets_weights = {} #empty dictionary

    alphabets = 'abcdefghijklmnopqrstuvwxyz'

    for index in range(1, len(alphabets)+1):
        alphabets_weights[alphabets[index-1]] = index

    column_value = alphabets_weights[column]
    return (column_value, int(loc.strip()[2]))

	
def index2location(x: int, y: int) -> str:
    '''converts  pair of coordinates to corresponding location'''

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''


Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B''' 
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''

class Bishop(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to all chess rules
        
        Hints:
        - firstly, check [Rule1] and [Rule3] using can_reach
        - secondly, check if result of move is capture using is_piece_at
        - if yes, find the piece captured using piece_at
        - thirdly, construct new board resulting from move
        - finally, to check [Rule4], use is_check on new board
        '''
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this rook to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''


class King(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''
    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''

def is_check(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is check for side
    Hint: use can_reach
    '''

def is_checkmate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is checkmate for side

    Hints: 
    - use is_check
    - use can_move_to
    '''

def is_stalemate(side: bool, B: Board) -> bool:
    '''
    checks if configuration of B is stalemate for side

    Hints: 
    - use is_check
    - use can_move_to 
    '''

def read_board(filename: str) -> Board:
    '''
    reads board configuration from file in current directory in plain format
    raises IOError exception if file is not valid (see section Plain board configurations)
    '''

def save_board(filename: str, B: Board) -> None:
    '''saves board configuration into file in current directory in plain format'''


def find_black_move(B: Board) -> tuple[Piece, int, int]:
    '''
    returns (P, x, y) where a Black piece P can move on B to coordinates x,y according to chess rules 
    assumes there is at least one black piece that can move somewhere

    Hints: 
    - use methods of random library
    - use can_move_to
    '''

def conf2unicode(B: Board) -> str: 
    '''converts board cofiguration B to unicode format string (see section Unicode board configurations)'''


def main() -> None:
   
    # filename = input("File name for initial configuration: ")
    try:
        board_validation = False
        # print("Testing")
        while board_validation == False:
            filename = input("File name for initial configuration: ")  
            # filename="board_examp.txt"
            file = open(filename)
            file_content = file.readlines()
            if (int(file_content[0]) <= 3 or int(file_content[0]) >= 26):
                board_validation = False
                print("Dimentions are not correct")
                continue
            
            # while (int(file_content[0]) <= 3 or int(file_content[0]) >= 26):
            #     file_content[0] = int(input("Enter the number again"))
            
            white_pieces = file_content[1].split(",")

            bool_pool = []
            for white_piece in white_pieces:
                # print(white_piece)
                loc2index = location2index(white_piece)

                # if (alphabets_weights[white_piece.strip()[1]] > 0) and (alphabets_weights[white_piece.strip()[1]] <= int(file_content[0])) and (int(white_piece.strip()[2:]) <= int(file_content[0])):
                if (loc2index[0] > 0) and (loc2index[0] <= int(file_content[0])) and (int(white_piece.strip()[2:]) <= int(file_content[0])):
                    # pass
                    print("In White Piece")
                    board_validation = True
                    
                else:
                    print("The file is not valid: white")
                    # board_validation = False
                    bool_pool.append(False)
                    break

            black_pieces = file_content[2].split(",")

            for black_piece in black_pieces:
                # print(black_piece)

                loc2index = location2index(black_piece)

                if (loc2index[0] > 0) and (loc2index[0] <= int(file_content[0])) and (int(black_piece.strip()[2:]) <= int(file_content[0])):
                    # pass
                    print("In Black Piece")
                    board_validation = True
                else:
                    # print("The file is not valid: black") 
                    # board_validation = False
                    bool_pool.append(False)
                    break
            if False in bool_pool:
                board_validation = False
            elif board_validation == True:
                print("File is valid")

            file.close()
        # print("Ending")
    except FileNotFoundError:
        print("The file does not exist.")

     

if __name__ == '__main__': #keep this in
   main()
