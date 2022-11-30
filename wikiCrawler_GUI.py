#!/usr/bin/env python3

from tkinter import *
from WikCrawler.__init__ import *
from WikCrawler import *
import sys
from io import StringIO
import subprocess


class root_window(Tk):
    def __init__(self):
        super().__init__()
        self.geometry("1200x530")
        self.resizable(False, False)

    def searching(self):
        self.option = self.search_type.get()
        print(self.option)
        if self.option == "Topic Search":
            return '-s'
        elif self.option == "Get Topic Info":
            return '-i'
        elif self.option == "Get Summary and References":
            return '-q'
        else:
            return '-o'

    def data(self):
        self.out = open("OUTPUT.txt", "r")
        self.info = self.out.read()
        for i in self.info:
            print(str(i),end='')
        self.results.insert(END,self.info)
        self.out.close()
        
    def onclick(self):
        self.topic = self.input.get()
        if len(str(self.topic)) > 0:
            self.results.config(state = NORMAL)
            self.results.delete('1.0', END)
            self.value = self.searching()
            subprocess.run(["WikCrawler", str(self.value), str(self.topic)])
            # subprocess.run(["WikCrawler", "-i", str(self.topic)])
            self.data()
            self.input.delete('0', END)
        self.results.config(state = DISABLED)

    def Label(self):
        # Title Bar
        self.title("WikiCrawler  -- Expand your knowledge through Linux")

        # Window background image
        self.background = PhotoImage(file = "HelloWorld.png")
        self.backgroundLabel = Label(self, image = self.background)
        self.backgroundLabel.place(x = 0, y = 0)

        self.text_header = Label(self, text = "Choose your Topic", font = ('Billabong', 28), fg = 'black')
        self.text_header.place(x = 50, y = 50)

        # Choose Search Type
        self.search_type = StringVar()
        self.search_type.set("Select Search Type")

        self.chose_type = OptionMenu(self, self.search_type, "Topic Search", "Get Topic Info", "Get Summary and References")
        self.chose_type.place(x = 145, y = 160)

        # Search Button
        self.search_butn = Button(self, command = self.onclick)
        self.img2 = PhotoImage(file = "icons8-google-web-search-60.png")
        self.search_butn.config(image = self.img2)
        self.search_butn.place(x = 30, y = 115)  

        self.input = Entry(self, width = 22, borderwidth = 2, font = ('Helvetica', 18))
        self.input.place(x = 105, y = 105)
        self.search = StringVar()
        

        # Right Side of Window -> results
        self.text_result = Label(self, text = "Results", font = ('Billabong', 26), fg = 'black')
        self.text_result.place(x = 460, y = 8)

        self.vert_scroll = Scrollbar(self, orient = 'vertical')
        self.vert_scroll.pack(side = 'right', fill = 'y')

        self.results = Text(self, width = 90, height = 25, wrap = WORD, yscrollcommand = self.vert_scroll.set)
        self.results.place(x = 458, y = 50)
        self.results.config(state = NORMAL)
        self.results.insert(INSERT, "Soon to be Searching...")
        self.results.config(state = DISABLED) 



if __name__=="__main__":
    root = root_window()
    root.Label()
    root.mainloop()