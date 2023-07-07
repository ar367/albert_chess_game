import numpy as np


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
   
    for list in board:
        # print(list, "\n")
        for piece_ in list:
            
            if piece_ == None:
                continue
            a, b = piece_[0]
            a = int(a)
            b = int(b)
            # print(a,b)
            if (a, b) == (x, y):
                return piece_[1].strip()
           

class Piece:
    pos_x : int	
    pos_y : int
    side : bool #True for White and False for Black
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values'''
        self.pos_X = pos_X
        self.pos_Y = pos_Y
        self.side_ = side_


Board = tuple[int, list[Piece]]


def is_piece_at(pos_X : int, pos_Y : int, B: Board) -> bool:
    '''checks if there is piece at coordinates pox_X, pos_Y of board B''' 
    board_pieces = B[1]
    check_list = []
    
    for piece_ in board_pieces:
        if piece_[0] == pos_X and piece_[1] == pos_Y:
            check_list.append(piece_)
    if check_list != None:
        return True
    else:
        return False
    
	
def piece_at(pos_X : int, pos_Y : int, B: Board) -> Piece:
    '''
    returns the piece at coordinates pox_X, pos_Y of board B 
    assumes some piece at coordinates pox_X, pos_Y of board B is present
    '''
    board_pieces =  B[1]
    check_list_ = []
    
    for piece_ in board_pieces:
        
        
        if piece_[0] == pos_X and piece_[1] == pos_Y:
            check_list_.append(piece_)
        else:
            continue
    
    if check_list_ == []:
        return None
    elif check_list_ != None:
        return check_list_[0]
    


class Bishop(Piece):
    def __init__(self, pos_X : int, pos_Y : int, side_ : bool):
        '''sets initial values by calling the constructor of Piece'''
        self.initial_position_x_bishop = pos_X
        self.initial_position_y_bishop = pos_Y
        self.side_ = side_
        
	
    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''
        checks if this bishop can move to coordinates pos_X, pos_Y
        on board B according to rule [Rule1] and [Rule3] (see section Intro)
        Hint: use is_piece_at
        '''
        updated_position_x_bishop = pos_X
        updated_position_y_bishop = pos_Y

        bishop_movement_condition = abs(self.initial_position_x_bishop - updated_position_x_bishop) == abs(self.initial_position_y_bishop - updated_position_y_bishop)

        if bishop_movement_condition:
            can_reach_side_bool = []
            for piece_ in B[1]:
                if updated_position_x_bishop == piece_[0] and updated_position_y_bishop == piece_[1]:
                    can_reach_side_bool.append(piece_[2])
                    
                # else:
                #     # print("we are here")
                #     return "Hello"
            if can_reach_side_bool != []:

                if self.side_ == can_reach_side_bool[0]:
                    return (False, "side is same")
                else: 
                    return True
            else:
                return "can_reach_side_bool is empty"
        
        else: 
            return False


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
        self.initial_position_x_king = pos_X
        self.initial_position_y_king = pos_Y
        self.side_ = side_

        

    def can_reach(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to rule [Rule2] and [Rule3]'''

        updated_position_x_king = pos_X
        updated_position_y_king = pos_Y

        """
            Meaningful words
                abs - absdolute
                diff - difference
                up - updated 
                init - initial
                comp - comparison

                
                attr - attribute 
                bwd - between
        """

        abs_diff_up_x_from_init_x = abs(self.initial_position_x_king - updated_position_x_king)
        abs_diff_up_y_from_init_y = abs(self.initial_position_y_king - updated_position_y_king) 
        comp_btw_init_and_up_attr_king = (self.initial_position_x_king, self.initial_position_y_king) != ( updated_position_x_king,updated_position_y_king)
        
        one = 1

        valid_move = abs_diff_up_x_from_init_x <= one and  abs_diff_up_y_from_init_y <= one and comp_btw_init_and_up_attr_king
        # print("B1", B[1])
        if valid_move:
            # for piece_ in B[1]:
            #         if piece_[2] != self.side_:
            #             return True
            #         else:
            #             return False
                    
                    
            can_reach_side_bool_king = []
            for piece_ in B[1]:
                if updated_position_x_king == piece_[0] and updated_position_y_king == piece_[1]:
                    can_reach_side_bool_king.append(piece_[2])
                    
                # else:
                #     # print("we are here")
                #     return "Hello"
            if can_reach_side_bool_king != []:

                if self.side_ == can_reach_side_bool_king[0]:
                    return (False, "side is same")
                else: 
                    return True
            else:
                return "can_reach_side_bool is empty"
            

        else:
            return False
                    
    


    def can_move_to(self, pos_X : int, pos_Y : int, B: Board) -> bool:
        '''checks if this king can move to coordinates pos_X, pos_Y on board B according to all chess rules'''

        return 
    def move_to(self, pos_X : int, pos_Y : int, B: Board) -> Board:
        '''
        returns new board resulting from move of this king to coordinates pos_X, pos_Y on board B 
        assumes this move is valid according to chess rules
        '''
        updated_position_x_king = pos_X
        updated_position_y_king = pos_Y

        """
            Meaningful words
                abs - absdolute
                diff - difference
                up - updated 
                init - initial
                comp - comparison

                
                attr - attribute 
                bwd - between
        """

        abs_diff_up_x_from_init_x = abs(self.initial_position_x_king - updated_position_x_king)
        abs_diff_up_y_from_init_y = abs(self.initial_position_y_king - updated_position_y_king) 
        comp_btw_init_and_up_attr_king = (self.initial_position_x_king, self.initial_position_y_king) != ( updated_position_x_king,updated_position_y_king)
        
        one = 1

        valid_move = abs_diff_up_x_from_init_x <= one and  abs_diff_up_y_from_init_y <= one and comp_btw_init_and_up_attr_king
        
        if valid_move:
            print("YES")
        else:
            print("NO")

def is_check(side: bool, B: Board) ->bool: 
    '''
    checks if configuration of B is check for side
    Hint: use can_reach-
    '''
    
    white_king = ""
    black_king = ""
    for coordinates in B[1]:
        piece_at_ = piece_at(coordinates[0], coordinates[1], B)
        piece = index2location(coordinates[0], coordinates[1])
        if piece[0] == 'K':
            if piece_at_[2] == 1:
                white_king += piece
            elif piece_at_[2] == 0:
                black_king += piece
    
    move_cord = location2index(move)
    if side == 1:
        white_king_can_reach_moves = general_moves[white_king]
        white_king_can_reach_moves_unique = set()
        for moves in white_king_can_reach_moves:
            white_king_can_reach_moves_unique.add(moves[0])
        print("white_king_can_reach_moves: ", white_king_can_reach_moves_unique)

        in_check__white_king_excluded_coordinates_unique=set()
        for cords in in_check_excluded_coordinates[0]:
            in_check__white_king_excluded_coordinates_unique.add(tuple(cords))
        print("in_check_excluded_coordinates: ", in_check__white_king_excluded_coordinates_unique)

        set_difference = white_king_can_reach_moves_unique.difference(in_check__white_king_excluded_coordinates_unique)

        print("length of set_difference: ", len(set_difference))
        if len(set_difference) == 0:
            return True
        else:
            return False
    elif side == 0:
        black_king_can_reach_moves = general_moves[black_king]
        black_king_can_reach_moves_unique = set()
        for moves in black_king_can_reach_moves:
            black_king_can_reach_moves_unique.add(moves[0])
        print("black_king_can_reach_moves: ", black_king_can_reach_moves_unique)

        in_check_black_king_excluded_coordinates_unique=set()
        for cords in in_check_excluded_coordinates[0]:
            in_check_black_king_excluded_coordinates_unique.add(tuple(cords))
        print("in_check_excluded_coordinates: ", in_check_black_king_excluded_coordinates_unique)

        set_difference_black = black_king_can_reach_moves_unique.difference(in_check_black_king_excluded_coordinates_unique)

        print("length of set_difference: ", len(set_difference_black))
        if len(set_difference_black) == 0:
            return True
        else:
            return False

    # move_cord = location2index(move)

    # if side == 1:
        
    #     if move_cord in in_check_excluded_coordinates[0]:
    #         return "In Check"
    #     else:
    #         return "Not in check"
    # elif side == 0:
    #     if move_cord in in_check_excluded_coordinates[1]:
    #         return "In Check"
    #     else:
    #         return "Not in check"
        
    

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
    pieces = B[1]

    board_configuration_2_unicode = ""
    
    for piece in pieces:

        index2loc = index2location(piece[0], piece[1])
        bishop_or_king = index2loc[0]

        piece_at_ = piece_at(piece[0], piece[1], B)
        bishop_or_king_side = piece_at_[2]

        if bishop_or_king == "K" and bishop_or_king_side == 1:
            white_king = "\u2654", f"{piece[0]},{piece[1]}", "#"
            white_king = "_".join(white_king)
            board_configuration_2_unicode += white_king
            # print("\u2654", "\u2001", f"{piece[0]}, {piece[1]}")
        elif bishop_or_king == "K" and bishop_or_king_side == 0:
            black_king = "\u265A", f"{piece[0]},{piece[1]}", "#"
            black_king = "_".join(black_king)
            board_configuration_2_unicode += black_king
            # print("\u265A", "\u2001", f"{piece[0]}, {piece[1]}")
        elif bishop_or_king == "B" and bishop_or_king_side == 1:
            white_bishop = "\u2657", f"{piece[0]},{piece[1]}", "#"
            white_bishop = "_".join(white_bishop)
            board_configuration_2_unicode += white_bishop
            # print("\u2657", "\u2001", f"{piece[0]}, {piece[1]}")
        elif bishop_or_king == "B" and bishop_or_king_side == 0:
            black_bishop = "\u265D", f"{piece[0]},{piece[1]}","#"
            black_bishop = "_".join(black_bishop)
            board_configuration_2_unicode += black_bishop
            # print("\u265D", "\u2001", f"{piece[0]}, {piece[1]}")

    for every_sis_spaces in board_configuration_2_unicode:
        pass


    return board_configuration_2_unicode




def main() -> None:
    # filename = input("File name for initial configuration: ")
    try:
        global piece
        pieces = []
        piece = []
        board_validation = False
        # print("Testing")
        while board_validation == False:
            filename = input("File name for initial configuration: ")   
            # filename="board_examp.txt"
            file = open(filename)
            global file_content
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

                piece_class = Piece(int(loc2index[0]), int(loc2index[1]), 1)
                pieces.append([piece_class.pos_X, piece_class.pos_Y, piece_class.side_])

                piece.append([loc2index, white_piece, "white"])

                # if (alphabets_weights[white_piece.strip()[1]] > 0) and (alphabets_weights[white_piece.strip()[1]] <= int(file_content[0])) and (int(white_piece.strip()[2:]) <= int(file_content[0])):
                if (loc2index[0] > 0) and (loc2index[0] <= int(file_content[0])) and (int(white_piece.strip()[2:]) <= int(file_content[0])):
                    # pass
                    # print("In White Piece")
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

                piece_class = Piece(int(loc2index[0]), int(loc2index[1]), 0)
                pieces.append([piece_class.pos_X, piece_class.pos_Y, piece_class.side_])

                piece.append([loc2index, black_piece, "black"])

                if (loc2index[0] > 0) and (loc2index[0] <= int(file_content[0])) and (int(black_piece.strip()[2:]) <= int(file_content[0])):
                    # pass
                    # print("In Black Piece")
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
    
    # print(pieces) 
    global board
    board = [[None for i in range(int(file_content[0]))] for j in range(int(file_content[0]))]
    # global all_board_coordinates
    all_board_coordinates = [[None for i in range(int(file_content[0]))] for j in range(int(file_content[0]))]
    # print("Length of board: ", len(board[1]))
    for i in range(int(file_content[0]),0,-1):
        for j in range(1, int(file_content[0])+1):

            row_5 = 0
            row_4 = 1
            row_3 = 2
            row_2 = 3
            row_1 = 4

            rows = [5-1, 4-1, 3-1, 2-1, 1-1]

            col_1 = 0
            col_2 = 1
            col_3 = 2
            col_4 = 3
            col_5 = 4

            cols = [1-1, 2-1, 3-1, 4-1, 5-1]

            for k in piece:
                if k[0] == (j,i):
                    # print("Hello World", j, i)
                    board[rows[i-1]][cols[j-1]] = k
                all_board_coordinates[rows[i-1]][cols[j-1]] = (j,i)

    # print(board[0])
    # for list in board:
    #     print(list)
    index2loc = index2location(3, 1)




    # print(index2loc)

    Bo = (5, pieces)
    # print(Bo)

    # print('\n Board', board)

    # print("\n")

    # is_piece_at_ = is_piece_at(4 , 4, Bo)
    # print(is_piece_at_, "Is piece at")


    # print("\n")
    # piece_at_ = piece_at(5 ,3, Bo)
    # print(piece_at_)
    
    #-------------------------------------------------  Can Reach  ---------------------------------------------------
    global general_moves
    general_moves = {}

    for k in piece:
        general_moves[k[1].strip()] = []

    for list_of_coordinates in all_board_coordinates:
        for coordinates in list_of_coordinates:
            # print(coordinates)
            # print(piece)
            for k in piece:
                if k[1].strip()[0] == 'B':
                    pass
                    
                    is_piece_at_ = is_piece_at( k[0][0], k[0][1], Bo)
                    piece_at_ = piece_at(k[0][0], k[0][1], Bo)
                    piece_at_other_cord = piece_at(coordinates[0], coordinates[1], Bo)

                    bishop = Bishop(k[0][0], k[0][1], piece_at_[2])

                    can_reach_ = bishop.can_reach(coordinates[0], coordinates[1], Bo)

                    if piece_at_other_cord == None:
                        if can_reach_:
                            list_to_append = (coordinates[0], coordinates[1]), None
                            general_moves[k[1].strip()] += [list_to_append]
                    else:
                        if piece_at_[2]  == piece_at_other_cord[2]:
                            pass
                        else: 
                            if can_reach_:
                                list_to_append = [(coordinates[0], coordinates[1]), piece_at_[2]]
                                general_moves[k[1].strip()] += [list_to_append]

                    # print("bishop.can_reach: ",can_reach_)

                    # if (piece_at_[0], piece_at_[1]) == coordinates:

                        
                    #     if can_reach_:

                    #         list_to_append = [(coordinates[0], coordinates[1]), piece_at_[2]]
                    #         general_moves[k[1].strip()] += [list_to_append]
                    # else:

                    #     if can_reach_:
                    #         list_to_append = (coordinates[0], coordinates[1]), None
                    #         general_moves[k[1].strip()] += [list_to_append]

                if k[1].strip()[0] == 'K':
                    pass
                    is_piece_at_ = is_piece_at( k[0][0], k[0][1], Bo)
                    piece_at_ = piece_at(k[0][0], k[0][1], Bo)
                    piece_at_other_cord = piece_at(coordinates[0], coordinates[1], Bo)

                    king = King(k[0][0], k[0][1], piece_at_[2])

                    can_reach_ = king.can_reach(coordinates[0], coordinates[1], Bo)

                    if piece_at_other_cord == None:
                        if can_reach_:
                            list_to_append = (coordinates[0], coordinates[1]), None
                            general_moves[k[1].strip()] += [list_to_append]
                    else:
                        if piece_at_[2]  == piece_at_other_cord[2]:
                            pass
                        else: 
                            if can_reach_:
                                list_to_append = [(coordinates[0], coordinates[1]), piece_at_[2]]
                                general_moves[k[1].strip()] += [list_to_append]


    print("general_moves: ", general_moves)
    print('\n')

    general_moves_keys = general_moves.keys()

    # ------------------------------------------------  Identify White and Black Pieces  -------------------------------------------------------
    white_pieces = []
    black_pieces = []

    for key in general_moves_keys:
        piece_cord = location2index(key)
        piece_coordinates_with_side = piece_at(piece_cord[0], piece_cord[1], Bo)
        if piece_coordinates_with_side[2] == 1:
            white_pieces.append(key)
        elif piece_coordinates_with_side[2] == 0:
            black_pieces.append(key) 

    print("\nWhite pieces: ", white_pieces)
    print("\nBlack pieces: ", black_pieces)
    # -------------------------------------------  Excluded Coordinates for King is in_cheque  -------------------------------------------------

    
    import numpy as np

    next_move = (2,3)

    global in_check_excluded_coordinates
    in_check_excluded_coordinates = []
    same_side_excluded_coordinates = []
    
    for key in general_moves_keys:

        if key[0] == 'K':
            king_coordinates = location2index(key)

            king_coordinates_with_side = piece_at(king_coordinates[0], king_coordinates[1], Bo)
            # print(king_coordinates_with_side[2])

            same_side_coordinates_excluded = []
            coordinates_excluded = []

            for list_of_coordinates in all_board_coordinates:
                for coordinates in list_of_coordinates:
                    if is_piece_at(coordinates[0], coordinates[1], Bo) == True:
                        pieces_side = piece_at(coordinates[0], coordinates[1], Bo)
                        if pieces_side != None:
                            if pieces_side[2] == king_coordinates_with_side[2]:
                                same_side_coordinates_excluded.append((coordinates[0], coordinates[1]))
                            else:
                                king_values = general_moves[key]
                                for value in king_values:
                                    
                                    piece_cord_with_side = piece_at(coordinates[0], coordinates[1], Bo)
                                    if piece_cord_with_side[2] != king_coordinates_with_side[2]:
                                        piece_str = index2location(coordinates[0], coordinates[1])
                                        piece_values = general_moves[piece_str]
                                        if value in piece_values:
                                            coordinates_excluded.append(value[0])

            

            arr = np.concatenate((coordinates_excluded, same_side_coordinates_excluded))
            in_check_excluded_coordinates.append(arr)

            same_side_excluded_coordinates.append(same_side_coordinates_excluded)
            # in_check_excluded_coordinates.append(coordinates_excluded)
                                            
            print("King: ", king_coordinates_with_side)
            print("Excluded Coordniates: ", list(set(coordinates_excluded)))
            print("Excluded Coordniates same side: ", same_side_coordinates_excluded)

   
    # ---------------------------------------------------  Board Configuration 2 Unicode  --------------------------------------------------------

    board_config_to_unicode = (conf2unicode(Bo))
    # print(board_config_to_unicode)

    
    config_to_unicode = board_config_to_unicode.split("#")
    # print(config_to_unicode)


    all_board_coordinates_to_unicode = all_board_coordinates

    """ ---------  getting index of rows and cols 
                   from our board configuration
                              (Start)              ------------"""
    
    row_index_board_config = []
    for number in range(Bo[0]):
        row_index_board_config.append(None)

    col_index_board_config = []
    for number in range(Bo[0]):
        col_index_board_config.append(None)


    for index in range(Bo[0]):
        row_index_board_config[index] = index + 1
        col_index_board_config[index] = Bo[0] - (index)

    # print("Row values: ", row_index_board_config)
    # print("Column values: ", col_index_board_config)



    """ ---------  Prinitng the configuration   ------------"""

    # print("all_board_coordinates_to_unicode", all_board_coordinates_to_unicode)
    row_index = []
    col_index = []

    for piece in config_to_unicode:
        if piece != "":
            for index, number in enumerate(row_index_board_config):
                if number == int(piece[2]):
                    # print(piece[2], index)
                    row_index.append(index)
            
            for index, number in enumerate(col_index_board_config):
                if number == int(piece[4]):
                    # print(piece[4], index)
                    col_index.append(index)
            

    # print("row, col index", row_index, col_index)
    for index, piece in enumerate(config_to_unicode):
        
        if len(piece) > 2:
            # print(piece[0])
            # print(row_index_board_config[row_index[index]], col_index_board_config[col_index[index]])
            all_board_coordinates_to_unicode[col_index[index]][row_index[index]] = piece[0]


    print("Board configuration 2 unicode")

    for row in all_board_coordinates_to_unicode:
        row_str = ""
        for value in row:
            if type(value) == tuple:
                row_str += "\u2001"
            elif type(value) == str:
                row_str += value
        print(row_str)


    selected_piece = input("Select White Piece: ")
    global move
    move = input("Next move of White: ")
    print(move)

    selected_piece_cord = location2index(selected_piece)
    selected_piece_cord_with_side = piece_at(selected_piece_cord[0], selected_piece_cord[1], Bo)   

    print("board: ", Bo)
    print(is_check(selected_piece_cord_with_side[2], Bo))


if __name__ == '__main__': #keep this in
   main()
