import random
from tkinter import *

class GuessingGame:

    
    
    def __init__(self, master):

        #initizing method
        self.master = master
        master.title("Joe's Mad Lib Quiz")

        #class varibles
        self.EASY=0 #defined diffculty levels
        self.HARD=1
        self.EXPERT=2
        self.guess = ["o","o","o","o",] # player answer list
        self.num_guesses = 3 # number of guesses constant
        self.level_free=0 
        self.num_right = 0 # var that keeps track of correct answers
        self.good_ans = 4 # number of correct answers needed 
        self.message=[["A ______ is created with the def keyword.","Operators are the constructs which can manipulate the value of","A program is a set of ","_____ are identified as a set of characters represented in the quotation marks. "," This is My Mad Lib Quiz Project. There are 3 Differculty Levels EASY-HARD-EXPERT \n You must correctly answer all the questions by filling in the blanks, before you will be able to move the next. Press the'Submit'Button after you answer the questions. \n If you miss any answers you will have press RESET to try again.  You have 3 chances to pass.  "],["A ___ is a sequence of immutable Python objects","The most basic data structure in Python is the______ . ","A ___ contains items separated by commas and enclosed within square brackets ([]).","Tuples can be thought of as ___only lists"],["____statement lets you import specific attributes from a module into the current namespace","______ are names (identifiers) that map to objects","The____built-in function returns a sorted list of strings containing the names defined by a module.","____is a unique instance of a data structure that's defined by its class."]]
        self.anslist=[["method","operands","instructions","strings"],["tuple","sequence","list","read"],["from","variables","dir()","object"]]
        self.max_try=0
        self.level=0 #current game level
        self.wrong_list=["-"] #wrong answer list
        
        #setting up result box
        self.result_text = Text(root,height=1,width=10,bg='lightgreen', font=('times', 10, 'italic'))
        self.open_scene_text = Message(root,width=500,text=self.message[0][4])
        self.open_scene_text.grid(row=0, column=1)

        # calling program methods
        self.text_setup()
        self.button_setup()
        self.answer_box()
        self.button_free()
       

    def button_setup(self):

        # set up program buttons
        self.easy_button = Button(root, text="Easy", command=lambda:self.play_scene(self.EASY))
        self.hard_button = Button(root, text="Hard", command=lambda:self.play_scene(self.HARD))
        self.expert_button = Button(root, text="Expert", command=lambda:self.play_scene(self.EXPERT))
        self.submit_button = Button(root, text="Submit", command=self.guess_number)
        self.reset_button = Button(root, text="Reset", command=self.reset,height=1,width=10)
        self.quit_button = Button(root, text="QUIT", command=self.quit,height=1,width=10)

        self.easy_button.grid(row=11, column=0)
        self.hard_button.grid(row=12, column=0)
        self.expert_button.grid(row=13, column=0)
        self.reset_button.grid(row=15, column=1)
        self.quit_button.grid(row=15, column=0)
        self.submit_button.grid(row=14, column=2)

        
    def text_setup(self):

        #set up questions text
        self.label_text = StringVar()
        self.label_text.set(self.message[0][0])
        self.label = Message(root, textvariable=self.label_text,foreground='red')
        self.label.config(width=500, justify=LEFT)

        self.label_text1 = StringVar()
        self.label_text1.set(self.message[0][1])
        self.label1 = Message(root, textvariable=self.label_text1,foreground='red')
        self.label1.config(width=500,justify=LEFT)

        self.label_text2 = StringVar()
        self.label_text2.set(self.message[0][2])
        self.label2 = Message(root, textvariable=self.label_text2,foreground='red')
        self.label2.config(width=500,justify=LEFT)
        
        self.label_text3 = StringVar()
        self.label_text3.set(self.message[0][3])
        self.label3 = Message(root, textvariable=self.label_text3,foreground='red')
        self.label3.config(width=500,justify=LEFT)

        
        self.result_text = Text(root,height=1,width=10,bg='lightgreen', font=('times', 10, 'italic'))
        self.result_text.grid(row=14, column=0,columnspan=2, sticky=W+E)


    def answer_box(self):

        #set up answer entry boxes
        self.entry = Entry(root)
        self.entry1 = Entry(root)
        self.entry2 = Entry(root)
        self.entry3 = Entry(root)
        self.entry4 = Entry(root)
       
        self.entry.grid(row=10, column=2, columnspan=1, sticky=W+E)
        self.entry1.grid(row=11, column=2, columnspan=1, sticky=W+E)
        self.entry2.grid(row=12, column=2, columnspan=1, sticky=W+E)
        self.entry3.grid(row=13, column=2, columnspan=1, sticky=W+E)
        # placing questions on grid
        self.label.grid(row=10, column=0, columnspan=2, sticky=W+E)
        self.label1.grid(row=11, column=0, columnspan=2, sticky=W+E)
        self.label2.grid(row=12, column=0, columnspan=2, sticky=W+E)
        self.label3.grid(row=13, column=0, columnspan=2, sticky=W+E)

        
    def play_scene(self, ulevel):
        #changes game level
       self.reset()
       self.level=ulevel         
       self.label_text.set(self.message[ulevel][0])
       self.label_text1.set(self.message[ulevel][1])
       self.label_text2.set(self.message[ulevel][2])
       self.label_text3.set(self.message[ulevel][3])


    
   
        
        
    def button_free(self):

        #Changes button status based on game level
        
        if self.level_free == 0:
            self.easy_button.configure(state=NORMAL)
            self.hard_button.configure(state=DISABLED)
            self.expert_button.configure(state=DISABLED)
            
        elif self.level_free == 1:
            self.easy_button.configure(state=NORMAL)
            self.hard_button.configure(state=NORMAL)
            self.expert_button.configure(state=DISABLED)
            
        elif self.level_free == 2:
            self.easy_button.configure(state=NORMAL)
            self.hard_button.configure(state=NORMAL)
            self.expert_button.configure(state=NORMAL)
        

    def guess_number(self):

        #Places answer box entries in a list        
        self.num_guesses -=1        # keeps track of the players guesses
        self.guess[0]=self.entry.get()
        self.guess[1]=self.entry1.get()
        self.guess[2]=self.entry2.get()
        self.guess[3]=self.entry3.get()
        

        for x in range(0, 4):  #checks the player answers vs the answer list
        
            if self.guess[x] == self.anslist[self.level][x]:
                self.num_right+=1
            else:
                self.wrong_list.append(self.guess[x])

        

        if self.num_right>=self.good_ans :
           self.yes_passed()       
           
        else:
           self.not_passed()
           if self.num_guesses == self.max_try:
               self.end_game()

    def not_passed(self):
        # the incorrect answer method
        self.result_message = "The following answers are wrong "
        
        self.label_textR = StringVar()
        self.result_text.insert(END,self.result_message)
        self.result_text.insert(END,self.wrong_list)
        self.result_text.insert(END,"- You have ")
        self.result_text.insert(END,self.num_guesses,)
        self.result_text.insert(END," guesses left")
        self.num_right=0

        
    def yes_passed(self):
        # the correct method
        self.reset()
        self.result_message = ("Congratulations! You guessed all the answers right on this level")
        self.result_text.insert(END,self.result_message)
        self.level_free+=1
        self.button_free()
        self.num_guesses = 3
        self.num_right=0
         
    def end_game(self):  # the method if they run out of guesses
        self.reset()
        self.result_message = ("Sorry You ran out chances")
        self.result_text.insert(END,self.result_message)
        self.easy_button.configure(state=DISABLED)
        self.hard_button.configure(state=DISABLED)
        self.expert_button.configure(state=DISABLED)
        self.reset_button.configure(state=DISABLED)
        self.submit_button.configure(state=DISABLED)
        
    def quit(self):
        # the quit method
        exit(0)
        
    def reset(self):
        # reset all the answer boxes and clears the wrong answer list
        self.entry.delete(0, END)
        self.entry1.delete(0, END)
        self.entry2.delete(0, END)
        self.entry3.delete(0, END)
        self.wrong_list.clear()
        
        self.result_text.delete(1.0,END)
       


root = Tk()
root.geometry("700x300")
my_gui = GuessingGame(root)
root.mainloop()
