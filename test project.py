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
        tk.messagebox.showerror('Warning!!', 'Please type only one word')
    elif not input_txt.isalpha():
        tk.messagebox.showerror('Warning!!', 'Please type a word')
    elif input_txt in already_guess:
        tk.messagebox.showwarning("Warning!!!", "You have already guessed this word")
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
hint_list = ["It's a four-wheeled vehicle", "It can bark", "It's like a tiger but smaller", "sweep things on the ground", \
             "you can read it or write it", "keeping your pants on your waist", "heating things up", \
             "cover your hands", "a device for showing time", "used for sit", "used for writing or drawing", "used for cutting", \
             "when thing goes quiet", "most", "used for lifting people", "Used with a bow", "Used for receiving patients", \
             "when you thristy", "shinning in the space", "skill", "sticky paper", "sadness", \
             "american football", "used for filling water", "used for calling", "a place where cars run", "on and off", \
             "As opposed to rude", "used for protection agianst rain", "a period hundred years", "a place where people goes to study", \
             "the way that someone behaves", "of the present time", "a period of 24 hours", "the end of life", "a male parent", \
             "a journey in an aircraft", "to direct your eyes in order to see", "the flesh of an animal when it is used for food", \
             "drops of water from clouds", "the belief in, and worship of, a god or gods"]

photos = [tk.PhotoImage(file=r"images\new hang1_removebg.png").subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang2_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang3_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang4_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang5_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang6_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang7_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\new hang8_removebg.png').subsample(2, 2)\
    , tk.PhotoImage(file=r'images\enter btn.png').subsample(2)]

window_1.option_add("*Font", "Consolas 40")
width_sc, height_sc = window_1.winfo_screenwidth(), window_1.winfo_screenheight()
window_1.geometry("%dx%d"%(width_sc, height_sc))
window_1.state('zoom')
tk.Label(window_1, text="Welcome to Hangman Minigame!!!", bg="#61F3EB", font=("Comic Sans MS", 40))\
    .pack(side="top", pady=(height_sc//20, 0))


frame_image = tk.Frame(window_1)
imgLabel = tk.Label(frame_image)
imgLabel.config(image=photos[0])
imgLabel.pack()
frame_image.pack(side="top", pady=(height_sc//20, 0))


lblword = StringVar()
txt_show = tk.Label(window_1, textvariable=lblword)
txt_show.pack(side="top", pady=(height_sc//20, 0))


word_hint = StringVar()
txt_hint = tk.Label(window_1, textvariable=word_hint, bg="yellow", font=("Comic Sans MS", 40))
txt_hint.pack(side="top", pady=(height_sc//20, 0))


frame_guess = tk.Frame(window_1)
tk.Label(frame_guess, text="Enter your guess : ", bg="pink", font=("Franklin Gothic", 40)).pack(side="left", padx=(0, 10))
blank_txt = StringVar()
txt = tk.Entry(frame_guess, textvariable=blank_txt, width=5, bd=5, justify="center")
txt.pack(side="left", padx=(0, 10))
enter = tk.Button(frame_guess, image=photos[8], text="Enter", command=lambda txt=txt: guess(txt), borderwidth=0)
enter.pack(side="left", padx=(10, 0))
frame_guess.pack(side="top", pady=(height_sc//20, 0))

newgame()
window_1.mainloop()
