from tkinter import *
from complete_to_sentences import init_system, find_best_k_completions
from utils import normal_string, detailed_completion
import threading
from tkinter import messagebox
from PIL import ImageTk, Image


class AutoCompGui:

    def __init__(self):
        self.root = Tk()
        self.user_input = StringVar(self.root)

    def completions(self):
        normal_input = normal_string(self.user_input.get())

        if len(normal_input) < 2:
            return "the string to search must have a length of at least 2 letters", 1

        completions = find_best_k_completions(normal_string(normal_input))
        m = len(completions)

        if not completions:
            return "no suggestions :(", 2

        txt = ""

        for i in range(len(completions)):
            txt += detailed_completion(completions[i - 1]) + "\n"

        return txt, 0

    def temp_label_input(self, comps):
        label = Label(self.root, text=comps)
        label.pack()
        timer = threading.Timer(2.0, label.destroy)
        timer.start()

    def show_comps(self):
        comps, status = self.completions()
        ic = "info" if 0 == status else "warning" if 1 == status else "error"
        messagebox._show("completions", comps, _icon=ic)

        if not status:
            self.temp_label_input(comps)

    def start_app(self):

        self.root.title(string='Great AutoCompletion!!')
        self.root.iconphoto(False, PhotoImage(file='icon.png'))
        self.root.geometry('500x500')

        init_system()

        lab = Label(self.root, text='please enter a string to search')
        lab.pack()

        e = Entry(self.root, textvariable=self.user_input)
        e.pack()
        
        img = ImageTk.PhotoImage(Image.open("book_mark.png"))
        search_button = Button(self.root, command=self.show_comps, image=img, width=120, height=100)
        search_button.pack()


        mainloop()
