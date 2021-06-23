'''
    Checking weather a chess board is valid or not.

    Created: May 30, 2021
    Creator: Nishkant
'''

goats = ["pawn", "rook", "bishop", "king", "queen", "knight"] #valid names of goats
piece_names = ["bpawn", "brook", "bbishop", "bking", "bqueen", "bknight" , 
                 "wpawn", "wrook", "wbishop", "wking", "wqueen", "wknight"] #valid names of pieces
spaces = []  #valid names of spaces
for i in range(1,9):
    for j in ("a","b","c","d","e","f","g","h"):
        x = str(i) + j
        spaces.append(x)

#defining some test chess boards
chess_board =  {'1h': 'bking', '6c': 'wqueen',  '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking', "4a":"wpawn", "4b":"bpawn"}
chess_board2 =  {'1h': 'king', '6c': 'wqueen', '2g': 'bbishop', '5h': 'bqueen', '3e': 'wking' , "9z":"wpawn"}



def bothkings(dict):
    if "bking" not in dict.values() or "wking" not in dict.values():
        print("Both kings must be present in the game.")
        return False

def MaxPlayers(dict):
    white_piece = 0
    black_piece = 0
    white_pawn = 0
    black_pawn = 0

    for piece in dict.values():
        for goat in range(len(goats)):
            if piece == "w"+ goats[goat]:
                white_piece += 1
            elif piece == "b" + goats[goat]:
                black_piece += 1 
        if piece == "wpawn":
            white_pawn += 1
        elif piece == "bpawn":
            black_pawn += 1
    if white_piece > 16 or black_piece > 16 or white_pawn > 8 or black_pawn > 8:
        print("Max players each side must be 16 and max pawns must be 8.")
        return False

def valid_spaces(dict):
    for space in dict.keys():
        if space not in spaces:
            print("Invalid space")
            return False

def valid_pieces(dict):
    for piece in dict.values():
        if piece not in piece_names:
            print("Invalid piece name")
            return False

def isChessBoardValid(dict):
    if bothkings(dict) == False or MaxPlayers(dict) == False or valid_pieces(dict) == False or valid_spaces(dict) == False:
        return "The chess board is invalid."
    else:
        return "The chess board is valid."


print(isChessBoardValid(chess_board2))
print(isChessBoardValid(chess_board))

