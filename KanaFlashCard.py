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

randHiragana = ""

class MyFrame(customtkinter.CTkFrame):   
    def __init__(self, master,):
        super().__init__(master)
        
        self.label = customtkinter.CTkLabel(self,text=randHiragana,font=("Calibri",80))
        self.label.grid(row=0,column=0,pady=25)
        
        self.entry = customtkinter.CTkEntry(self,font=("Calibri",28),width=250)
        self.entry.grid(row=1,column=0,pady=25)
        
        self.submit = customtkinter.CTkButton(self,font=("Calibri",28),command=lambda: App.submit(),text="Submit")
        self.submit.grid(row=2,column=0,pady=25)
        
        self.new_card = customtkinter.CTkButton(self,font=("Calibri",28),command=lambda: App.index(randHiragana),text="New Card")
        self.new_card.grid(row=3,column=0,pady=25)
        
        self.result = customtkinter.CTkLabel(self,font=("Calibri",28),text=App.result,text_color=App.result_color)
        self.result.grid(row=4,column=0)
        
        
class App(customtkinter.CTk):
    
    result = "Incorrect"
    result_color= "red"
    
    def __init__(self):
        super().__init__()
        self.title("Kana Flashcards")
        self.geometry("640x480")
        
        customtkinter.set_appearance_mode("System")
        customtkinter.set_default_color_theme("green")
        
        self.my_frame = MyFrame(master=self)
        self.my_frame.pack()
        
        self.bind("<Return>",App.submit_hotkey)
        
        

    def index(randHiragana):
        indx = random.randint(0,45)
        newHiragana = list(hiragana_dict)[indx]
        randHiragana = newHiragana
        print(randHiragana)
        return randHiragana
        
        
    def submit():
        print("Answer Submitted")
        
    def submit_hotkey(event):
        print("Answer Submitted")

if __name__ == "__main__":
    app = App()
    app.mainloop()
    