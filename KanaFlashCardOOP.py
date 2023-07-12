import random
import tkinter as tk
from tkinter import ttk

# Entry Box & Buttons for submitting answers
# Potentially use label to display the character
#   - Randomly select a key:value to print for the label
# Have menu bar for quit options
# Show progress bar of how far through the session you are
# In future add the dakten


katakana_dict = {"ア":"a",
                "イ":"i",
                "ウ":"u",
                "エ":"e",
                "オ":"o", 
                "カ":"ka",
                "キ":"ki",
                "ク":"ku",
                "ケ":"ke",
                "コ":"ko",
                "サ":"sa",
                "シ":"shi",
                "ス":"su",
                "セ":"se",
                "ソ":"so",
                "タ":"ta",
                "チ":"chi",
                "ツ":"tsu",
                "テ":"te",
                "ト":"to",
                "ナ":"na",
                "ニ":"ni",
                "ヌ":"nu",
                "ネ":"ne",
                "ノ":"no",
                "ハ":"ha",
                "ヒ":"hi",
                "フ":"fu",
                "ヘ":"he",
                "ホ":"ho",
                "マ":"ma",
                "ミ":"mi",
                "ム":"mu",
                "メ":"me",
                "モ":"mo",
                "ヤ":"ya",
                "ユ":"yu",
                "ヨ":"yo",
                "ラ":"ra",
                "リ":"ri",
                "ル":"ru",
                "レ":"re",
                "ロ":"ro",
                "ワ":"wa",
                "ヲ":"wo",
                "ン":"n"}


hiragana_dict= {"あ":"a",
                "い":"i",
                "う":"u",
                "え":"e",
                "お":"o", 
                "か":"ka",
                "き":"ki",
                "く":"ku",
                "け":"ke",
                "こ":"ko",
                "さ":"sa",
                "し":"shi",
                "す":"su",
                "せ":"se",
                "そ":"so",
                "た":"ta",
                "ち":"chi",
                "つ":"tsu",
                "て":"te",
                "と":"to",
                "な":"na",
                "に":"ni",
                "ぬ":"nu",
                "ね":"ne",
                "の":"no",
                "は":"ha",
                "ひ":"hi",
                "ふ":"fu",
                "へ":"he",
                "ほ":"ho",
                "ま":"ma",
                "み":"mi",
                "む":"mu",
                "め":"me",
                "も":"mo",
                "や":"ya",
                "ゆ":"yu",
                "よ":"yo",
                "ら":"ra",
                "り":"ri",
                "る":"ru",
                "れ":"re",
                "ろ":"ro",
                "わ":"wa",
                "を":"wo",
                "ん":"n"}

class App(tk.Tk):
    def __init__(self,title,size):
        super().__init__()
#String Var
        Hiraganastring_variable = tk.StringVar(self,"あ")
        
        Resultstring_variable = tk.StringVar(self," ")      
#Window Config
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
#Frame
        self.mainframe = MainFrame(self,Resultstring_variable,Hiraganastring_variable)
        self.mainframe.place(x=160,y=50)

        self.mainloop()

class MainFrame(ttk.Frame):
    def __init__(self,parent,Resultstring_variable,Hiraganastring_variable):
        super().__init__(parent)

        def HiraganaIndx():
                shown_hiragana = list(hiragana_dict.keys())[random.randint(0,45)]
                return shown_hiragana
        
        def Submit(Resultstring_variable, Hiraganastring_variable):
                Hiraganastring_variable.set(HiraganaIndx())

        self.label = tk.Label(self,textvariable=Hiraganastring_variable,font=("Calibri",64))
        self.label.pack()

        self.submitbtn = tk.Button(self,text="Submit",command=lambda: Submit(Resultstring_variable, Hiraganastring_variable),font=("Calibri",24))
        self.submitbtn.pack()

        self.entry = tk.Entry(self,font=("Calibri",24))
        self.entry.pack()
        
        self.resultLabel = tk.Label(self,textvariable=Resultstring_variable)
        self.resultLabel.pack()

App("Kana Flash Cards",(640,480))