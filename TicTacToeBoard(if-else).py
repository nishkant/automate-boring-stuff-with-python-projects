GameBoard = {"Top Row"   :{"L" : " ", "M" : " " , "R" : " "},
             "Mid Row"   :{"L" : " ", "M" : " " , "R" : " "},
             "Bottom Row":{"L" : " ", "M" : " " , "R" : " "}}

for i in GameBoard.keys():
    for m in GameBoard[i]:
        if m != "R":
            print(GameBoard[i][m], end= " | ")
        else:
            print(GameBoard[i][m], end="")
    if i != "Bottom Row":
        print("\n--$---$--")




