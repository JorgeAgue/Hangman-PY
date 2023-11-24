from random_word import RandomWords
import tkinter as tk

r = RandomWords()
word = r.get_random_word()

def initializeGame(): # Resets all variables associated with the game
    global strikes, guess, hintGiven, word, answerArr, guessArr
    
    answerArr = []
    guessArr = []
    guess = ""
    strikes = 0
    hintGiven= 0 # 0 = hint not given, 1= hint is being given, 2= hint already given
    for char in word:
        answerArr.append("_")

class GUI:
    def __init__(self):
        self.root = tk.Tk()
        
        initializeGame()
        
        self.root.geometry("500x600")
        self.root.minsize(400,400)
        self.root.title("Hangman")

        p1 = tk.PhotoImage(file = 'icon.png')
        self.root.iconphoto(False, p1)

        self.menubar = tk.Menu(self.root)
        self.menubar.add_command(label="Restart Game", command=self.setNormal)
        self.menubar.add_command(label="Give Hint", command=self.giveHint)
        
        self.difMenu = tk.Menu(self.menubar, tearoff=0)
        self.difMenu.add_command(label="Easy", command=self.setEasy)
        self.difMenu.add_command(label="Normal", command=self.setNormal)
        self.difMenu.add_command(label="Hard", command=self.setHard)
        self.menubar.add_cascade(label="Difficulty", menu=self.difMenu)

        self.topLabel = tk.Label(self.root, text= "Guess a letter", font= ('Arial, 18'))
        self.topLabel.pack(padx=20, pady=20)

        self.hangManBox = tk.Text(self.root, height= 6, width= 10, font=('Arial, 16')) 
        self.hangManBox.pack(padx=40, pady=10)

        self.guessEntry = tk.Entry(self.root, font= ('Arial, 18'), width= 2)
        self.guessEntry.pack(padx=20, pady=20)

        self.guessButton = tk.Button(self.root, text= "Guess", font= ('Arial, 18'), command=self.checkGuess)
        self.guessButton.pack()
        
        self.wordBox = tk.Entry(self.root, font= ('Arial, 18'), width= len(word)+10)
        self.wordBox.pack(padx=20, pady=20)
        
        self.strikesLabel= tk.Label(self.root,font= ('Arial, 18'))
        self.strikesLabel.pack(padx=20)
        self.strikesLabel.config(text= "Strikes left: {}".format(6- strikes))

        self.statusLabel = tk.Label(self.root,font= ('Arial, 18'))
        self.statusLabel.pack()

        self.letterLabel = tk.Label(self.root,font=('Arial, 18'))
        self.letterLabel.pack()
        
        #Initalization
        self.drawHangman(strikes)
        self.hangManBox.config(state='disabled')

        self.wordBox.insert("0", answerArr)
        self.wordBox.config(state='readonly')

        self.root.config(menu=self.menubar)
        self.root.mainloop()


    def checkGuess(self):   #Finds instances of guessed letter in word and updates the wordBox
        global strikes, guess, hintGiven

        if(hintGiven == 0 or hintGiven == 2): #Brother...
            guess= self.guessEntry.get()
        else:
            hintGiven= 2
            
        guess = guess.lower()
        if (guess.isalpha() and len(guess)== 1 and guess not in guessArr): #Validate the input. if not valid, guess button does nothing

            guessArr.append(guess)
            correct = False
            self.guessEntry.delete(0,'end')
            self.letterLabel.config(text= guessArr)
            for i in range(len(word)):    
                if guess == word[i]:
                    answerArr[i] = guess
                    correct = True
                    self.wordBox.config(state='normal')
                    self.wordBox.delete(0,'end')
                    self.wordBox.insert("0", answerArr)
                    self.wordBox.config(state='readonly')

            if not correct:
                strikes+=1
                self.drawHangman(strikes)
                self.strikesLabel.config(text= "Strikes left: {}".format(6- strikes))
        
        if "_" not in answerArr:
            self.endGame(True)
        if strikes == 6:
            self.endGame(False)


    def endGame(self, haveWon): 
        if haveWon:
            self.statusLabel.config(text="You won!\n The word is: {}".format(word))
        else:
            self.statusLabel.config(text="You lost. The answer was...\n {}!".format(word))

        self.guessEntry.config(state="disabled")
        self.guessButton.config(state="disabled")


    def drawHangman(self, strikes):
        self.hangManBox.config(state='normal')
        self.hangManBox.delete("1.0","end") #Clears the textbox
        
        self.hangManBox.insert("1.0","________ \n")
        self.hangManBox.insert("2.0","|  | \n")
        
        if strikes == 0:
            self.hangManBox.insert("3.0","| \n")
            self.hangManBox.insert("4.0","| \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 1:
            self.hangManBox.insert("3.0","| O \n")
            self.hangManBox.insert("4.0","| \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 2:
            self.hangManBox.insert("3.0","| O \n")
            self.hangManBox.insert("4.0","| / \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 3:
            self.hangManBox.insert("3.0","| O \n")
            self.hangManBox.insert("4.0","| /| \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 4:
            self.hangManBox.insert("3.0","| O \n")
            self.hangManBox.insert("4.0","| /|\ \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 5:
            self.hangManBox.insert("3.0","| O \n")
            self.hangManBox.insert("4.0","| /|\ \n")
            self.hangManBox.insert("5.0","| / \n")
        
        elif strikes == 6:
            self.hangManBox.insert("3.0","| O \n")
            self.hangManBox.insert("4.0","| /|\ \n")
            self.hangManBox.insert("5.0","| / \ \n")

        self.hangManBox.insert("6.0","| ")
        self.hangManBox.config(state='disabled')

    def giveHint(self): #Gives player a hint by finding the 1st blank char in word and filling it for the user
        global guess, hintGiven

        if(hintGiven == 2):
            print("No more hints!")
        else:
            for i in range(len(answerArr)):
                if answerArr[i] == '_':
                    guess= word[i]
                    break
            hintGiven = 1
            self.checkGuess()
    
    def restartGame(self):
        self.root.destroy()
        self.__init__()
        initializeGame()
        self.root.mainloop()
    
    def setDifficulty(self, mode): #Not working currently
        global word
        r= RandomWords()
        if mode == "E":
            while len(word) >5:
                word = r.get_random_word()
                print("E")
        elif mode == "H":
            while len(word) <8:
                word = r.get_random_word()
                print(len(word) <8)
        elif mode == "M": # default/ normal was picked
            word = r.get_random_word()
            print("M")
        self.restartGame()
    
    def setEasy(self):
        global word
        r = RandomWords()
        word = r.get_random_word()
        
        while len(word) >5:
            word = r.get_random_word()
            print("Easy")
            print(word)
        
        self.restartGame()

    def setNormal(self):
        global word
        r = RandomWords()
        word = r.get_random_word()
        
        self.restartGame()
    
    def setHard(self):
        global word
        r = RandomWords()
        word = r.get_random_word()
        
        while len(word) <8:
            word = r.get_random_word()

        self.restartGame()

GUI()