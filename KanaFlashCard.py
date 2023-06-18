import random
import tkinter as tk
from tkinter import ttk
from threading import Thread

# Entry Box & Buttons for submitting answers
# Potentially use label to display the character
#   - Randomly select a key:value to print for the label
# Have menu bar for quit options
# Show progress bar of how far through the session you are
# Use a 2 dictionaries for hiragana and katakana to relate to the sounds
# In future add the dakten

katakana = {"ア":"a",
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

    def hiragana_indx(self):
        pass
    
    def submit(self):
        print("OOP working")

class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Kana Flashcards")
        self.geometry("640x480")
        #all tkinter configs go here
        
        #label
        self.flashcard = tk.Label(self,text="ロ",font=("",40))
        self.flashcard.pack()
        
        #entry
        self.answer_box = tk.Entry(self,font=("Arial",24))
        self.answer_box.pack()

        #submit button
        self.submit = tk.Button(self,text="Submit",command=lambda: Hiragana.submit(self),font=("Arial",18))
        self.submit.pack()


if __name__ == "__main__":
    app = App()
    app.mainloop()