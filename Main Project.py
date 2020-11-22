"""Project PSIT"""
import tkinter as tk
from tkinter import messagebox
from tkinter import StringVar
import random



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
    word_hint.set(hint_list[word_list.index(word)])
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
                    tk.messagebox.showinfo("Answer", 'Answer : %s' %(word))
                    ans_new = tk.messagebox.askyesno("Hangman", "GAME OVER!!!\nDo You Want To Play Again ?")
                    if ans_new:
                        newgame()
                    else:
                        window_1.destroy()
    blank_txt.set("")


window_1 = tk.Tk()
window_1.title("Hangman!!!")
word_list = ["car", "dog", "cat", "shoes", "bloom", "book", "belt", "microwave", "shirts", \
"gloves","bat", "mouth", "coffee", "the moon", "glass"]
hint_list = ["It's a four-wheeled vehicle", "It can bark", "It's like a tiger but smaller", \
"It's cover your feet", "Sweep things on the ground", "You can read it or write it", \
"Keeping your pants on your waist", "Heating things up", "Wear on your upper body", \
"Cover your hands", "They are nocturnal and often live in caves.", \
"The organs you use to speak!!", "A sleepy drink with a unique aroma.", "Earth's satellite planets", \
"You use it as a container for drinking water."]
photos = [tk.PhotoImage(file=r"C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang4.png")\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang5.png')\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang6.png')\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang7.png')\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang8.png')\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang9.png')\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang10.png')\
    , tk.PhotoImage(file=r'C:\Users\LENOVO\OneDrive\เดสก์ท็อป\งาน Lab PSIT\Mini Project PSIT\images\hang11.png')]
window_1.option_add("*Font", "Consolas 40")
width_sc, height_sc = window_1.winfo_screenwidth(), window_1.winfo_screenheight()
window_1.geometry("%dx%d"%(width_sc, height_sc))
tk.Label(window_1, text="Welcome to Hangman Minigame!!!", bg="#61F3EB")\
    .place(anchor="center", x=width_sc/2, y=50)

imgLabel = tk.Label(window_1, bg="pink")
imgLabel.place(anchor="center", x=width_sc/2, y=height_sc/6)
imgLabel.config(image=photos[0])

lblword = StringVar()
txt_show = tk.Label(window_1, textvariable=lblword)
txt_show.place(anchor="center", x=width_sc/2, y=400)


word_hint = StringVar()
txt_hint = tk.Label(window_1, textvariable=word_hint)
txt_hint.place(anchor="center", x=width_sc/2, y=height_sc/2)


tk.Label(text="Enter your guess : ").place(x=400, y=650, anchor="w")
blank_txt = StringVar()
txt = tk.Entry(textvariable=blank_txt, width=10)
txt.place(anchor="w", x=width_sc/2, y=650)


enter = tk.Button(window_1, text="Enter", font="Consolas 30", fg="#FF3232", width=10, command=lambda txt=txt: guess(txt))
enter.place(anchor="center", x=width_sc/2, y=800)
newgame()
window_1.mainloop()
