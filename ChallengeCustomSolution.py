#Made By Boris Kerbs on May 18, 2023
import sys

def dataEntry():
    #This method handles the entry of the 3 main data structures: Dimension, 
    #list of rows where the bombs are located and list of columns where the bombs are located.

    bombRows = []
    bombColumns = []
    pptDimension = input("Enter the  number of rows and columns: ")
    print("")
    print("Board dimensions are: {}X{}".format(pptDimension, pptDimension))
    pptDimension = int(pptDimension)
    print("")
    print("Enter {} row numbers or less for the bombs".format(pptDimension*pptDimension))
    print("this numbers should be unique and lower than {}".format(pptDimension))

    #The first while handles the entry of the rows where the bombs are located and limits the maximum number of rows
    while len(bombRows) <= (pptDimension*pptDimension):
        pptBombRows = input("Enter the next row number or the keyword 'q' to finish the entry ({} rows left): "
                            .format(pptDimension*pptDimension - len(bombRows)))
        if pptBombRows == "q":
            break
        else: 
            if int(pptBombRows) < pptDimension:
                bombRows.append(int(pptBombRows))
                print("R = {}".format(bombRows))
                print("")
            else:
                print("The number should be unique and lower than {}".format(pptDimension))
                print("R = {}".format(bombRows))
                print("")
    print("")

    #The second while handles the entry of the columns where the bombs are located and takes care of
    #both the quantity and the uniqueness
    while len(bombColumns) < len(bombRows):
        pptBombColumns = input("Enter the next column number or the keyword 'q' to finish the entry ({} columns left): "
                            .format((len(bombRows)) - len(bombColumns)))
        
        if pptBombColumns == "q":
            break
        else:
            tempCoord = (bombRows[len(bombColumns)], int(pptBombColumns))
            tempCoordList = list(zip(bombRows, bombColumns))
            if int(pptBombColumns) < pptDimension and tempCoord not in tempCoordList:
                bombColumns.append(int(pptBombColumns))
                print("C = {}".format(bombColumns))
                print("")
            elif tempCoord in tempCoordList:
                print("The number should be unique, the coordinate {} already exist".format(tempCoord))
                print("")
            else:
                print("The number should be unique and lower than {}".format(pptDimension))
                print("C = {}".format(bombColumns))
                print("")
    print("")
    return(pptDimension, bombRows, bombColumns)

def generateNeighbors(bombCoord, board):    
    #This method recives a empty board and the bomb coordinates, with this information
    #evaluates every position next to a bomb and summarizes the neighbors 
    #each time the condition is fulfilled, this method will be invoked later in the solution
    #to reveal every neighboor value

    for mine in bombCoord:
        x,y = mine 
        board[x][y] = "B"
        neighbors = [(x-1,y),(x-1,y+1),(x,y-1),(x+1,y-1),(x+1,y),(x+1,y+1),(x,y+1),(x-1,y-1)]
        for n in neighbors:
            if 0 <= n[0] <= len(board)-1 and 0 <= n[1] <= len(board)-1 and n not in bombCoord:
                board[n[0]][n[1]] += 1
        
def solution(n,r,c):
    #this method puts together the bombs and the neighboors usign mainly two for loops
    #one for each dimension after retriving the vaalues from the previous method

    print("Dimension: {}X{} - Rows: {} - Columns: {}".format(n,n,r,c))
    board = [[0 for i in range(0,n)] for j in range(0,n)]
    bombCoord = list(zip(r, c))
    generateNeighbors(bombCoord, board)
    c = [x for _,x in sorted(zip(r,c))]
    r.sort()

    for i in range(n):
        for j in range(n):
            if i in r and j == c[r.index(i)]:
                sys.stdout.write(" B ")
                r.remove(i)
                c.remove(j)
            else:
                neighbors = board[i][j]
                sys.stdout.write(" {} ".format(neighbors))
        print("")


def mainGame():
    #this method is used to unify both the data input and the solution
    #can be used to skip the entry by commenting out dataEntry()

    data = dataEntry()
    solution(data[0], data[1], data[2])

    #solution(5,[0,3,2],[1,4,3])
    #solution(15,[0,3,2,13,5],[1,4,3,7,11])
    #solution(5,[2, 3, 2, 3, 1, 1, 3, 1],[3, 3, 1, 1, 1, 2, 2, 3])
    
mainGame()