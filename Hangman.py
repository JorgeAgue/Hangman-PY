from random_word import RandomWords
import tkinter as tk

r = RandomWords()
word = r.get_random_word()

answerArr = []
guessArr = []
guess = ""
strikes = 0

for char in word:
    answerArr.append("_")


class GUI:
    def __init__(self):
        self.root = tk.Tk()
        self.root.geometry("600x600")
        self.root.title("Hangman")

        self.label = tk.Label(self.root, text= "Guess a letter", font= ('Arial, 18'))
        self.label.pack(padx=20, pady=20)

        self.guessEntry = tk.Entry(self.root, font= ('Arial, 18'), width= 2)
        self.guessEntry.pack(padx=20, pady=20)

        self.guessButton = tk.Button(self.root, text= "Guess", font= ('Arial, 18'), command=self.checkGuess)
        self.guessButton.pack()
        
        self.wordBox = tk.Entry(self.root, font= ('Arial, 18'), width= 35)
        self.wordBox.pack(padx=20, pady=40)
        
        self.hangManBox = tk.Text(self.root, height= 6)
        self.hangManBox.pack(padx=40, pady=40)

        self.statusLabel = tk.Label(self.root,font= ('Arial, 18'))
        self.statusLabel.pack()

        self.letterLabel = tk.Label(self.root,font=('Arial, 18'))
        self.letterLabel.pack()
        
        #Initalization
        self.drawHangmanTextBoxVer(strikes)
        self.wordBox.insert("0", answerArr)

        self.root.mainloop()
        
    def checkGuess(self):    #Finds instances of guessed letter in word and updates the wordBox
        global strikes
        guess= self.guessEntry.get()
        guessArr.append(guess)
        correct = False
        self.guessEntry.delete(0,'end')
        
        self.letterLabel.config(text= guessArr)
        for i in range(len(word)):    
            if guess == word[i]:
                answerArr[i] = guess
                correct = True
                
                self.wordBox.delete(0,'end')
                self.wordBox.insert("0", answerArr)
        
        if not correct:
            strikes+=1
            self.drawHangmanTextBoxVer(strikes)
        
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


    def drawHangmanTextBoxVer(self, strikes):
        self.hangManBox.delete("1.0","end") #Clears the textbox
        self.hangManBox.insert("1.0","________ \n")
        self.hangManBox.insert("2.0","|  | \n")
        
        if strikes == 0:
            self.hangManBox.insert("3.0","| \n")
            self.hangManBox.insert("4.0","| \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 1:
            self.hangManBox.insert("3.0","|  O \n")
            self.hangManBox.insert("4.0","| \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 2:
            self.hangManBox.insert("3.0","|  O \n")
            self.hangManBox.insert("4.0","| / \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 3:
            self.hangManBox.insert("3.0","|  O \n")
            self.hangManBox.insert("4.0","| /| \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 4:
            self.hangManBox.insert("3.0","|  O \n")
            self.hangManBox.insert("4.0","| /|\ \n")
            self.hangManBox.insert("5.0","| \n")
        
        elif strikes == 5:
            self.hangManBox.insert("3.0","|  O \n")
            self.hangManBox.insert("4.0","| /|\ \n")
            self.hangManBox.insert("5.0","| / \n")
        
        elif strikes == 6:
            self.hangManBox.insert("3.0","|  O \n")
            self.hangManBox.insert("4.0","| /|\ \n")
            self.hangManBox.insert("5.0","| / \ \n")

        self.hangManBox.insert("6.0","| ")

GUI()