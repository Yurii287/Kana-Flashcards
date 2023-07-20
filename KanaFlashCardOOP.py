import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Have menu bar for quit options
# add the dakten
# Keep a score 
# Pick how many cards to practice
#       use a for loop with a window opening for an int


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
        Hiraganastring_variable = tk.StringVar(self,"Start")
        
        Resultstring_variable = tk.StringVar(self," ")      
#Window Config
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
#Frame
        self.hiraganaframe = HiraganaFrame(self,Resultstring_variable,Hiraganastring_variable)
        self.hiraganaframe.place(x=160,y=50)
        
        self.mainloop()
class HiraganaFrame(ttk.Frame):
    def __init__(self,parent,Resultstring_variable,Hiraganastring_variable):
        super().__init__(parent)
        
        answer = []
        
        def Start():
                Submit(Resultstring_variable)
                self.startbtn.destroy()
        
        def HiraganaIndx():
                for i in list(hiragana_dict)[random.randint(0,45)]:
                        chosenHiragana = i, list(hiragana_dict[i])
                Hiraganastring_variable.set(chosenHiragana[0])
                answer.append(''.join(chosenHiragana[1]))
                print(answer)
                
        def Submit(Resultstring_variable):
                HiraganaIndx()
                if len(answer) <= 1:
                        pass
                else:
                        if self.Userentry.get() == answer[len(answer)-2]:
                                Resultstring_variable.set("Correct")
                        else: Resultstring_variable.set("Incorrect")
                        self.Userentry.delete(0, tk.END)
                        if len(answer) > 2:
                                answer.pop(0)

        self.label = tk.Label(self,textvariable=Hiraganastring_variable,font=("Calibri",64))
        self.label.pack()
        
        self.startbtn = tk.Button(self,text="Start",command=Start,font=("Calibri",24))
        self.startbtn.pack()
        
        self.submitbtn = tk.Button(self,text="Submit",command=lambda: Submit(Resultstring_variable),font=("Calibri",24))
        self.submitbtn.pack()

        self.Userentry = tk.Entry(self,font=("Calibri",24))
        self.Userentry.pack()
        
        self.resultLabel = tk.Label(self,textvariable=Resultstring_variable,font=("Calibri",32))
        self.resultLabel.pack()
        
App("Kana Flash Cards",(640,480))
