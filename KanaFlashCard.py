import random
import customtkinter
from tkinter import *
from threading import Thread

# Entry Box & Buttons for submitting answers
# Potentially use label to display the character
#   - Randomly select a key:value to print for the label
# Have menu bar for quit options
# Show progress bar of how far through the session you are
# In future add the dakten
#
# Use CustomTkinter

class Katakana:
    def __init__(self):
        self.katakana = {"ア":"a",
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
    randKatakana = "ア"

class Hiragana:
    def __init__(self):
        self.hiragana = {"あ":"a",
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

    rand_H = "あ"

class MyFrame(customtkinter.CTkFrame,Hiragana):
    
    result = "Incorrect"
    result_color= "red"
    
    def __init__(self, master,):
        super().__init__(master)
        
        self.label = customtkinter.CTkLabel(self,text=Hiragana.rand_H,font=("Calibri",80))
        self.label.grid(row=0,column=0,pady=25)
        
        self.entry = customtkinter.CTkEntry(self,font=("Calibri",28),width=250)
        self.entry.grid(row=1,column=0,pady=25)
        
        self.submit = customtkinter.CTkButton(self,font=("Calibri",28),command=lambda: MyFrame.submit(),text="Submit")
        self.submit.grid(row=2,column=0,pady=25)
        
        self.new_card = customtkinter.CTkButton(self,font=("Calibri",28),command=lambda: MyFrame.index(self.label),text="New Card")
        self.new_card.grid(row=3,column=0,pady=25)
        
        self.result = customtkinter.CTkLabel(self,font=("Calibri",28),text=MyFrame.result,text_color=MyFrame.result_color)
        self.result.grid(row=4,column=0)
    
    def index(label):
        print(Hiragana.rand_H)
        label.configure(text="New Text")
        
        
    def submit():
        print("Answer Submitted")


class App(customtkinter.CTk):
    def __init__(self):
        super().__init__()
        self.title("Kana Flashcards")
        self.geometry("640x480")
        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        
        self.my_frame = MyFrame(master=self)
        self.my_frame.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()
    