import random
from tkinter import Tk, Label, Button, Entry, StringVar, DISABLED, NORMAL, END, W, E

class GuessingGame:

    
    
    def __init__(self, master):
        self.master = master
        master.title("Joe's Mad Lib Quiz")

        self.secret_number = random.randint(1, 100)
        self.guess = ["o","o","o","o",]
        self.num_guesses = 0
        self.num_right = 0
        self.goodboy = 4
        self.message=["The quiz is for my","The Python was name after ","A program is a set of ","A For loop does ","My name is"]
        self.anslist=["a","b","c","d","e"]
        
       
        self.label_text = StringVar()
        self.label_text.set(self.message[0])
        self.label = Label(master, textvariable=self.label_text)

        self.label_text1 = StringVar()
        self.label_text1.set(self.message[1])
        self.label1 = Label(master, textvariable=self.label_text1)


        self.label_text2 = StringVar()
        self.label_text2.set(self.message[2])
        self.label2 = Label(master, textvariable=self.label_text2)

        self.label_text3 = StringVar()
        self.label_text3.set(self.message[3])
        self.label3 = Label(master, textvariable=self.label_text3)

        self.label_text4 = StringVar()
        self.label_text4.set(self.message[4])
        self.label4 = Label(master, textvariable=self.label_text4)

        self.label_textR = StringVar()
        self.label_textR.set(self.message[0])
        self.labelR = Label(master, textvariable=self.label_text)



        #vcmd = master.register(self.validate) # we have to wrap the command
        self.entry = Entry(master)
        self.entry1 = Entry(master)
        self.entry2 = Entry(master)
        self.entry3 = Entry(master)
        self.entry4 = Entry(master)

        self.guess_button = Button(master, text="Guess", command=self.guess_number)
        self.reset_button = Button(master, text="Play again", command=self.reset, state=DISABLED)

        self.label.grid(row=0, column=0, columnspan=2, sticky=W+E)
        self.label1.grid(row=1, column=0, columnspan=2, sticky=W+E)
        self.label2.grid(row=2, column=0, columnspan=2, sticky=W+E)
        self.label3.grid(row=3, column=0, columnspan=2, sticky=W+E)
        self.label4.grid(row=4, column=0, columnspan=2, sticky=W+E)
        self.labelR.grid(row=6, column=1, columnspan=2, sticky=W+E)
        
        self.entry.grid(row=0, column=2, columnspan=2, sticky=W+E)
        self.entry1.grid(row=1, column=2, columnspan=2, sticky=W+E)
        self.entry2.grid(row=2, column=2, columnspan=2, sticky=W+E)
        self.entry3.grid(row=3, column=2, columnspan=2, sticky=W+E)
        self.entry4.grid(row=4, column=2, columnspan=2, sticky=W+E)
        
        self.guess_button.grid(row=5, column=0)
        self.reset_button.grid(row=5, column=1)

    def validate(self, new_text):
        #if not new_text: # the field is being cleared
         #   self.guess = None
          #  return True

        #try:
            self.guess.append(new_text) 
        #    if 1 <= guess <= 100:
       #         self.guess = guess
        #        return True
        #    else:
        #        return False
       # except ValueError:
            return True

    def guess_number(self):
        self.num_guesses += 1
        self.guess[0]=self.entry.get()
        self.guess[1]=self.entry1.get()
        self.guess[2]=self.entry2.get()
        self.guess[3]=self.entry3.get()
        

        for x in range(0, 4):
        
            if self.guess[x] is None:
                self.message = "Time to Play"

            elif self.guess[x] == self.anslist[x]:
                    self.num_right+=1

        if self.num_right==self.goodboy:
                  
           self.message = "Congratulations! You guessed the number after %d guess%s." 
           self.guess_button.configure(state=DISABLED)
           self.reset_button.configure(state=NORMAL)

       
        self.message = "Congratulations! You guessed the number after %d guess%s." 
        self.label_textR.set(self.message)
        print (self.num_right)

    def reset(self):
        self.entry.delete(0, END)
        self.secret_number = random.randint(1, 100)
        self.guess = 0
        self.num_guesses = 0

        self.message = "Guess a number from 1 to 100"
        self.label_text.set(self.message)

        self.guess_button.configure(state=NORMAL)
        self.reset_button.configure(state=DISABLED)

root = Tk()
root.geometry("600x400")
my_gui = GuessingGame(root)
root.mainloop()
