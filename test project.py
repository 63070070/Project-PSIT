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
             "knife", "silent", "majority", "elevator", "camera", "headphone", "drink", "star", "black mirror", \
             "sticker", "sorrow", "soccer", "bottle", "phone", "road", "switch", "dentist", "umbrella", "century"]
hint_list = ["It's a four-wheeled vehicle", "It can bark", "It's like a tiger but smaller", "Sweep things on the ground", \
             "You can read it or write it", "Keeping your pants on your waist", "Heating things up", \
             "Cover your hands", "It's a device for showing time", "Used for sit", \
             "Used for writing or drawing", "It's used for cutting", \
             "When thing goes quiet", "Most", "Used for lifting people", "Take a picture", "Listen to music", \
             "When you thristy", "Shinning in the space", "One-sided mirror", "Sticky Paper", "Sadness", \
             "American football", "Used for filling water", "Used for calling", "Where cars run", "On and off", \
             "The doctor for teeth", "Used for protection agianst rain", "A hundred years"]
path = os.getcwd()
photos = [tk.PhotoImage(file=path+r"\images\new hang1.png")\
    , tk.PhotoImage(file=path+r'\images\new hang2.png')\
    , tk.PhotoImage(file=path+r'\images\new hang3.png')\
    , tk.PhotoImage(file=path+r'\images\new hang4.png')\
    , tk.PhotoImage(file=path+r'\images\new hang5.png')\
    , tk.PhotoImage(file=path+r'\images\new hang6.png')\
    , tk.PhotoImage(file=path+r'\images\new hang7.png')\
    , tk.PhotoImage(file=path+r'\images\new hang8.png')]

window_1.option_add("*Font", "Consolas 40")
width_sc, height_sc = window_1.winfo_screenwidth(), window_1.winfo_screenheight()
window_1.geometry("%dx%d"%(width_sc, height_sc))
tk.Label(window_1, text="Welcome to Hangman Minigame!!!", bg="#61F3EB")\
    .place(anchor="center", x=width_sc/2, y=50)


imgLabel = tk.Label(window_1)
imgLabel.place(anchor="center", x=width_sc/2, y=height_sc/4)
imgLabel.config(image=photos[0])


lblword = StringVar()
txt_show = tk.Label(window_1, textvariable=lblword)
txt_show.place(anchor="center", x=width_sc/2, y=400)


word_hint = StringVar()
txt_hint = tk.Label(window_1, textvariable=word_hint, bg="yellow")
txt_hint.place(anchor="center", x=width_sc/2, y=525)


tk.Label(text="Enter your guess : ", bg="pink").place(x=200, y=650, anchor="w")
blank_txt = StringVar()
txt = tk.Entry(textvariable=blank_txt, width=10)
txt.place(anchor="w", x=750, y=650)


enter = tk.Button(window_1, text="Enter", font="Consolas 30", fg="#FF3232", width=10, command=lambda txt=txt: guess(txt))
enter.place(anchor="center", x=1200, y=650)

newgame()
window_1.mainloop()
