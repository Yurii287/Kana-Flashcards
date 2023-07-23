import random
import tkinter as tk
from tkinter import *
from tkinter import ttk

# Have menu bar for quit options
# add the dakten
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
#Variables
        answer = []
        score = 0
#String Var
        Hiraganastring_variable = tk.StringVar(self,"Start")
        
        Katakanastring_variable = tk.StringVar(self,"Start")
        
        Resultstring_variable = tk.StringVar(self," ")
#Window Config
        self.title(title)
        self.geometry(f'{size[0]}x{size[1]}')
        self.minsize(size[0],size[1])
#MenuBar
        menubar = Menu(self)
        self.config(menu=menubar)
        Navbar(self,menubar)
        
#Frames
        self.hiraganaframe = HiraganaFrame(self,Resultstring_variable,Hiraganastring_variable,answer,score)
        self.hiraganaframe.place(x=160,y=50)
        
        self.katakanaframe = KatakanaFrame(self,Resultstring_variable,Katakanastring_variable,answer,score)
        self.katakanaframe.place(x=160,y=50)
        
        self.mainloop()

class Navbar(tk.Menu):
        def __init__(self,parent,menubar):
                super().__init__(parent)
                
                fileMenu = Menu(menubar,tearoff=0)
                menubar.add_cascade(label="Switch Script",menu=fileMenu,font=("Calibri",14))
        
                fileMenu.add_command(label="Hiragana",command=lambda: changeHiragana(),font=("Calibri",14))
                fileMenu.add_command(label="Katakana",command=lambda: changeKatakana(),font=("Calibri",14))


class HiraganaFrame(ttk.Frame):
    def __init__(self,parent,Resultstring_variable,Hiraganastring_variable,answer,score):
        super().__init__(parent)
        
        self.answer = answer
        self.score = score
                
        def Start(self):
                Submit(self,Resultstring_variable)
                self.startbtn.destroy()
                self.submitbtn = tk.Button(self,text="Submit",command=lambda: Submit(self,Resultstring_variable),font=("Calibri",24))
                self.submitbtn.pack()
        
        def HiraganaIndx(self):
                for i in list(hiragana_dict)[random.randint(0,45)]:
                        chosenHiragana = i, list(hiragana_dict[i])
                Hiraganastring_variable.set(chosenHiragana[0])
                answer.append(''.join(chosenHiragana[1]))
                print(answer)
                
        def Submit(self,Resultstring_variable):
                HiraganaIndx(self)
                if len(answer) <= 1:
                        pass
                else:
                        if self.Userentry.get() == answer[len(answer)-2]:
                                Resultstring_variable.set("Correct")
                                self.score += 1
                                print(self.score)
                                self.scoreLabel.config(text=str(self.score))
                                
                        else:
                                Resultstring_variable.set("Incorrect")
                                print(self.score)
                        self.Userentry.delete(0, tk.END)
                        if len(answer) > 2:
                                answer.pop(0)


        self.Mainlabel = tk.Label(self,textvariable=Hiraganastring_variable,font=("Calibri",64))
        self.Mainlabel.pack()
        
        self.startbtn = tk.Button(self,text="Start",command=lambda: Start(self),font=("Calibri",24))
        self.startbtn.pack()

        self.Userentry = tk.Entry(self,font=("Calibri",24))
        self.Userentry.pack()
        
        self.resultLabel = tk.Label(self,textvariable=Resultstring_variable,font=("Calibri",32))
        self.resultLabel.pack()
        
        self.scoreLabel = tk.Label(self,text=str(self.score),font=("Calibri",24))
        self.scoreLabel.pack()
        
                
class KatakanaFrame(ttk.Frame):
        def __init__(self,parent,Resultstring_variable,Katakanastring_variable,answer,score):
                super().__init__(parent)
                pass


App("Kana Flash Cards",(640,480))