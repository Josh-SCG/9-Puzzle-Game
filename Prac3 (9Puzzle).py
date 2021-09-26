#imports
import csv
import tkinter as tk
import random as r


class puzzle(tk.Frame):

#constructor function
    def __init__(self):
        tk.Frame.__init__(self)
        self.grid()
        self.master.title("9-Puzzle")

        self.mainGrid = tk.Frame(self, bg="#00ffff",bd=3,width=500,height=500)
        self.mainGrid.grid(pady=(100,0))
        self.makeGUI()
        root = tk.Tk()
        tk.Label(root,text = "Defualt Board State. \nClick New Game to Start.\nUse Control buttons or Click tiles to move",pady=100,padx=100).pack()
        root.attributes("-topmost", True)
        self.mainloop()


    def makeGUI(self):
        count=1
        self.cells = []
        for i in range(3):
            row = []
            for j in range(3):
                if count < 9:
                    cellFrame = tk.Frame(self.mainGrid)
                    cellFrame.grid(row=i,column=j,pady=5,padx=5)
                    cellNumber = tk.Label(self.mainGrid)
                    cellNumber.grid(row=i,column=j)
                    cellData = {"frame":cellFrame,"number":cellNumber}
                    row.append(cellData)
                    count +=1
                else:
                    cellFrame = tk.Frame(self.mainGrid)
                    cellFrame.grid(row=i,column=j,pady=5,padx=5)
                    cellNumber = tk.Label(self.mainGrid)
                    cellNumber.grid(row=i,column=j)
                    cellData = {"frame":cellFrame,"number":cellNumber}
                    row.append(cellData)
                    count +=1
            self.cells.append(row)

        #Tile Buttons
        b1Button = tk.Button(self.mainGrid,bg="teal",command=self.b1, text = "1",width = 17,height=8)
        b1Button.grid(row=0,column=0,padx=5,pady=5)
        b2Button = tk.Button(self.mainGrid,bg="teal",command=self.b2,text = "2",width = 17,height=8)
        b2Button.grid(row=0,column=1,padx=5,pady=5)
        b3Button = tk.Button(self.mainGrid,bg="teal",command=self.b3,text = "3",width = 17,height=8)
        b3Button.grid(row=0,column=2,padx=5,pady=5)
        b4Button = tk.Button(self.mainGrid,bg="teal",command=self.b4,text = "4",width = 17,height=8)
        b4Button.grid(row=1,column=0,padx=5,pady=5)
        b5Button = tk.Button(self.mainGrid,bg="teal",command=self.b5,text = "5",width = 17,height=8)
        b5Button.grid(row=1,column=1,padx=5,pady=5)
        b6Button = tk.Button(self.mainGrid,bg="teal",command=self.b6,text = "6",width = 17,height=8)
        b6Button.grid(row=1,column=2,padx=5,pady=5)
        b7Button = tk.Button(self.mainGrid,bg="teal",command=self.b7,text = "7",width = 17,height=8)
        b7Button.grid(row=2,column=0,padx=5,pady=5)
        b8Button = tk.Button(self.mainGrid,bg="teal",command=self.b8,text = "8",width = 17,height=8)
        b8Button.grid(row=2,column=1,padx=5,pady=5)
        b9Button = tk.Button(self.mainGrid,bg="#00ffff",command=self.b9,text = "",width = 17,height=8)
        b9Button.grid(row=2,column=2,padx=5,pady=5)

        self.buttonList = [[b1Button ,b2Button ,b3Button] ,[b4Button ,b5Button ,b6Button], [b7Button, b8Button, b9Button]]

        self.moveCounter = 0
        movesFrame = tk.Frame(self)
        movesFrame.place(relx=0.9,y=45,anchor="center")
        tk.Label(movesFrame,text = "Moves").grid(row=0)
        self.movesLabel = tk.Label(movesFrame,text="0")
        self.movesLabel.grid(row=1)

        buttonsFrame = tk.Frame(self)
        buttonsFrame.place(relx=0.6,y=45,anchor="e")
        tk.Label(buttonsFrame,text = "Buttons").grid(row=0)
        loadStateButton = tk.Button(buttonsFrame, text="Random Start State",command = self.loadRandom ,fg="blue",bg="teal") #can use hex colour codes on fg bg
        loadStateButton.grid(row=1,column=0)
        newGameButton = tk.Button(buttonsFrame, text="New Game(Load .csv)",command = self.newGame,fg="blue",bg="teal") #can use hex colour codes on fg bg
        newGameButton.grid(row=2,column=0)

        '''
        Code of test controls.
        '''
        '''
        buttonsFrame2 = tk.Frame(self)
        buttonsFrame2.place(relx=0.3,y=45,anchor="e")
        tk.Label(buttonsFrame2,text = "Controls").grid(row=0,column=1)
        up = tk.Button(buttonsFrame2, text="^",command=self.up,fg="red",bg="black") #can use hex colour codes on fg bg
        up.grid(row=1,column=1)
        down = tk.Button(buttonsFrame2, text="\/",command=self.down,fg="red",bg="black") #can use hex colour codes on fg bg
        down.grid(row=3,column=1)
        left = tk.Button(buttonsFrame2, text="<",command=self.left,fg="red",bg="black") #can use hex colour codes on fg bg
        left.grid(row=2,column=0)
        right = tk.Button(buttonsFrame2, text=">",command=self.right,fg="red",bg="black") #can use hex colour codes on fg bg
        right.grid(row=2,column=2)
        '''


#Button functions and extras
#reading in the csv csv_file
    def csvToList(self):
        #requires csv file to be in the format of:
        #1,2,3,4,5,6,7,8,B with B indicating the blank tile
        list = []
        returnList = []
        try:
            with open('StartState.csv') as csv_file: #name of csv file is important
                csv_reader = csv.reader(csv_file, delimiter=',')
                for row in csv_reader:
                    for item in row:
                        list.append(item)
        except:
            print("Invalid .csv file")
            root = tk.Tk()
            tk.Label(root,text = "Invalid .csv file\nRename file to StartState.csv",pady=100,padx=100).pack()
            root.attributes("-topmost", True)
            return

        row1 = []
        row2 = []
        row3 = []
        count = 0
        for item in list:
            if count < 3:
                row1.append(item)
                count += 1
            elif count < 6:
                row2.append(item)
                count += 1
            else:
                row3.append(item)
                count +=1

        if len(row3) != 3: #Grid is 3x3 hence can only have 9 items
            print("Invalid .csv format")
            root = tk.Tk()
            tk.Label(root,text = "Invalid .csv format\nContents of .csv file not supported\nSEE DOCUMENTATION\nGame cannot be solved with current .csv file",pady=100,padx=100).pack()
            root.attributes("-topmost", True)

        returnList.append(row1)
        returnList.append(row2)
        returnList.append(row3)
        print(returnList)
        return returnList;

#Load state
    def loadStartStateGUI(self): #loads the csv file onto the GUI
        self.boardState = self.csvToList()
        self.updateBoard()

#random State
    def loadRandom(self): #loads a random board onto the GUI
        deck = '1 2 3 4 5 6 7 8 B'.split()
        r.shuffle(deck)
        row1 = []
        row2 = []
        row3 = []
        count = 0
        for item in deck:
            if count < 3:
                row1.append(item)
                count += 1
            elif count < 6:
                row2.append(item)
                count += 1
            else:
                row3.append(item)
                count +=1
        self.makeGUI()
        self.boardState = [row1,row2,row3]
        self.updateBoard()
        root = tk.Tk()
        tk.Label(root,text = "DISCLAIMER:\nBoard may not be solvable",pady=50,padx=50).pack()
        root.attributes("-topmost", True)

#update boardState
    def updateBoard(self): #updates the GUI to the new state found in the boardState
        for i in range(3):
            for j in range(3):
                if self.boardState[i][j] == 'B':
                    self.cells[i][j]["frame"].configure(bg="#00ffff")
                    self.cells[i][j]["number"].configure(bg="#00ffff",text=str(""))
                    self.buttonList[i][j].configure(bg = "#00ffff",text=str(""))
                else:
                    self.cells[i][j]["frame"].configure(bg="teal")
                    self.cells[i][j]["number"].configure(bg="teal",text=str(self.boardState[i][j]))
                    self.buttonList[i][j].configure(bg = "teal",text=str(self.boardState[i][j]))

#incriment moves counter
    def addMoves(self): #incriment for the move counter
        self.moveCounter += 1
        self.movesLabel.configure(text=str(self.moveCounter))

#find blank tile
    def findBlank(self): # finds grid location of the blank tile
        row = 0
        col = 0
        returnList = []
        for i in range(3):
            for j in range(3):
                if self.boardState[i][j] == 'B':
                    row = i
                    col = j
        #print(str(row+1)+" "+str(col+1))
        return row,col

#Check if board is in solved state
    def checkSolved(self): #method to determine if game is over
        self.solvedState = [['1','2','3'],['4','5','6'],['7','8','B']]
        if self.boardState == self.solvedState:
            solvedFrame = tk.Frame(self.mainGrid,borderwidth=4)
            solvedFrame.place(relx=0.5,rely=0.5,anchor="center")
            tk.Label(solvedFrame,text="SOLVED!",bg="teal",fg="red",font = "arial").pack()
            return True
        return False

#control functions
    def down(self): #moves tile down if possible
        try:
            if self.checkSolved():
                print("Load Board First With New Game")
                root = tk.Tk()
                tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
                root.attributes("-topmost", True)

            else:
                row,col = self.findBlank()
                if row == 0:
                    print("Invalid move")
                else:
                    self.boardState[row][col] = self.boardState[row-1][col]
                    self.boardState[row-1][col] = 'B'
                    self.updateBoard()
                    self.addMoves()
                    self.checkSolved()
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def up(self): #moves tile up if possible
        try:
            if self.checkSolved():
                print("Load Board First With New Game")
                root = tk.Tk()
                tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
                root.attributes("-topmost", True)
            else:
                row,col = self.findBlank()
                if row == 2:
                    print("Invalid move")
                else:
                    self.boardState[row][col] = self.boardState[row+1][col]
                    self.boardState[row+1][col] = 'B'
                    self.updateBoard()
                    self.addMoves()
                    self.checkSolved()
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def left(self): #moves tile left if possible
        try:
            if self.checkSolved():
                print("Load Board First With New Game")
                root = tk.Tk()
                tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
                root.attributes("-topmost", True)
            else:
                row,col = self.findBlank()
                if col == 2:
                    print("Invalid move")
                else:
                    self.boardState[row][col] = self.boardState[row][col+1]
                    self.boardState[row][col+1] = 'B'
                    self.updateBoard()
                    self.addMoves()
                    self.checkSolved()
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def right(self): #moves tile right if possible
        try:
            if self.checkSolved():
                print("Load Board First With New Game")
                root = tk.Tk()
                tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
                root.attributes("-topmost", True)
            else:
                row,col = self.findBlank()
                if col == 0:
                    print("Invalid move")
                else:
                    self.boardState[row][col] = self.boardState[row][col-1]
                    self.boardState[row][col-1] = 'B'
                    self.updateBoard()
                    self.addMoves()
                    self.checkSolved()
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

#Tile move functions
    '''
    all the following are just the controls of the Puzzle
    the buttons are numbered by location on board such as
    1 2 3
    4 5 6
    7 8 9
    where each controls the tile and sees if it can be moved and moves it if possible
    ie tile 1 and go to tiles 2 and 4 but not others
    '''
    def b1(self):
        try:
            row, col = self.findBlank()
            if col == 0 and row == 1:
                self.down()
            elif col == 1 and row == 0:
                self.right()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)


    def b2(self):
        try:
            row, col = self.findBlank()
            if col == 0 and row == 0:
                self.left()
            elif col == 1 and row == 1:
                self.down()
            elif col == 2 and row == 0:
                self.right()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b3(self):
        try:
            row, col = self.findBlank()
            if col == 1 and row == 0:
                self.left()
            elif col == 2 and row == 1:
                self.down()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b4(self):
        try:
            row, col = self.findBlank()
            if col == 0 and row == 0:
                self.up()
            elif col == 1 and row == 1:
                self.right()
            elif col == 0 and row == 2:
                self.down()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b5(self):
        try:
            row, col = self.findBlank()
            if col == 1 and row == 0:
                self.up()
            elif col == 0 and row == 1:
                self.left()
            elif col == 2 and row == 1:
                self.right()
            elif col == 1 and row == 2:
                self.down()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b6(self):
        try:
            row, col = self.findBlank()
            if col == 2 and row == 0:
                self.up()
            elif col == 1 and row == 1:
                self.left()
            elif col == 2 and row == 2:
                self.down()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b7(self):
        try:
            row, col = self.findBlank()
            if col == 0 and row == 1:
                self.up()
            elif col == 1 and row == 2:
                self.right()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b8(self):
        try:
            row, col = self.findBlank()
            if col == 0 and row == 2:
                self.left()
            elif col == 1 and row == 1:
                self.up()
            elif col == 2 and row == 2:
                self.right()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

    def b9(self):
        try:
            row, col = self.findBlank()
            if col == 2 and row == 1:
                self.up()
            elif col == 1 and row == 2:
                self.left()
            else:
                print("Illegal move")
        except:
            print("Load Board First With New Game")
            root = tk.Tk()
            tk.Label(root,text = "Load Board First With New Game",pady=50,padx=50).pack()
            root.attributes("-topmost", True)

#reset the game/ new game
    def newGame(self):
        self.makeGUI()
        self.loadStartStateGUI()

puzzle()
