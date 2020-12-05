"""Project PSIT"""
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import random
import os


def newgame():
    """New game Function"""
    global word
    global word_withspaces
    global number_guess
    global lblword
    global already_guess
    number_guess = 0
    imgLabel.config(image=photos[0])
    word = random.choice(word_list)
    word_hint.set("Hint : "+hint_list[word_list.index(word)])
    word_withspaces = " ".join(word)
    lblword.set(" ".join("_"*(len(word))))
    already_guess = []


def guess(input_txt):
    """Check Function"""
    global word_withspaces
    global number_guess
    global already_guess
    input_txt = input_txt.get().rstrip().lower()
    txt = list(word_withspaces)
    guessed = list(lblword.get())

    if len(input_txt) > 1:
        tk.messagebox.showerror('Warning!!', 'Please type only one letter')
    elif not input_txt.isalpha():
        tk.messagebox.showerror('Warning!!', 'Please type a letter')
    elif input_txt in already_guess:
        tk.messagebox.showwarning("Warning!!!", "You have already guessed this letter")
    else:
        already_guess += [input_txt]
        if word_withspaces.count(input_txt) > 0:
            for i in range(len(txt)):
                if txt[i] == input_txt:
                    guessed[i] = input_txt
                lblword.set("".join(guessed))
                if lblword.get() == word_withspaces:
                    ans_new = tk.messagebox.askyesno("Hangman", "You Win!!!\nDo You Want To Play Again ?")
                    if ans_new:
                        newgame()
                    else:
                        window_1.destroy()
        else:
            number_guess += 1
            imgLabel.config(image=photos[number_guess])
            if number_guess == 7:
                tk.messagebox.showinfo("Answer", "Answer : %s" %(word))
                ans_new = tk.messagebox.askyesno("Hangman", "GAME OVER!!!\nDo You Want To Play Again ?")
                if ans_new:
                    newgame()
                else:
                    window_1.destroy()
    blank_txt.set("")


window_1 = tk.Tk()
window_1.title("Hangman!!!")

word_list = ["car", "dog", "cat", "bloom", "book", "belt", "microwave", "gloves", "clock", "chair", "pencil", \
             "knife", "silent", "majority", "elevator", "arrow", "ambulance", "drink", "star", "ability", \
             "sticker", "sorrow", "soccer", "bottle", "phone", "road", "switch", "polite", "umbrella", "century", \
             "school", "behavior", "current", "day", "death", "father", "flight", "look", "meat", "rain", "religion"]
hint_list = ["it's a four-wheeled vehicle", "it can bark", "it's like a tiger but smaller", "sweep things on the ground", \
             "you can read it or write it", "keeping your pants on your waist", "heating things up", \
             "cover your hands", "a device for showing time", "used for sit", "used for writing or drawing", "used for cutting", \
             "when thing goes quiet", "most", "used for lifting people", "Used with a bow", "Used for receiving patients", \
             "when you thristy", "shinning in the space", "skill", "sticky paper", "sadness", \
             "american football", "used for filling water", "used for calling", "a place where cars run", "on and off", \
             "As opposed to rude", "used for protection agianst rain", "a period hundred years", "a place where people goes to study", \
             "the way that someone behaves", "of the present time", "a period of 24 hours", "the end of life", "a male parent", \
             "a journey in an aircraft", "to direct your eyes in order to see", "the flesh of an animal when it is used for food", \
             "drops of water from clouds", "the belief in, and worship of, a god or gods"]
path = os.getcwd()
photos = [tk.PhotoImage(file=path+r"\images\new hang1_removebg.png").subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang2_removebg.png').subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang3_removebg.png').subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang4_removebg.png').subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang5_removebg.png').subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang6_removebg.png').subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang7_removebg.png').subsample(2)\
    , tk.PhotoImage(file=path+r'\images\new hang8_removebg.png').subsample(2)]

window_1.option_add("*Font", "Consolas 40")
width_sc, height_sc = window_1.winfo_screenwidth(), window_1.winfo_screenheight()
window_1.geometry("%dx%d"%(width_sc, height_sc))
tk.Label(window_1, text="Welcome to Hangman Minigame!!!", bg="#61F3EB")\
    .place(anchor="center", x=width_sc/2, y=50)


imgLabel = tk.Label(window_1)
imgLabel.place(anchor="center", x=width_sc/2, y=height_sc/3.5)
imgLabel.config(image=photos[0])


lblword = StringVar()
txt_show = tk.Label(window_1, textvariable=lblword)
txt_show.place(anchor="center", x=width_sc/2, y=550)


word_hint = StringVar()
txt_hint = tk.Label(window_1, textvariable=word_hint, bg="yellow")
txt_hint.place(anchor="center", x=width_sc/2, y=675)


tk.Label(text="Enter your guess : ", bg="pink").place(x=200, y=800, anchor="w")
blank_txt = StringVar()
txt = tk.Entry(textvariable=blank_txt, width=10)
txt.place(anchor="w", x=750, y=800)


enter = tk.Button(window_1, text="Enter", font="Consolas 30", fg="#FF3232", width=10, command=lambda txt=txt: guess(txt))
enter.place(anchor="center", x=1200, y=800)

newgame()
window_1.mainloop()
