from tkinter import *
from complete_to_sentences import init_system, find_best_k_completions
from utils import normal_string, detailed_completion
import threading
from tkinter import messagebox


root = Tk()
user_input = StringVar(root)


def completions():

    normal_input = normal_string(user_input.get())

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


def temp_label_input(comps):
    label = Label(root, text=comps)
    label.pack()
    timer = threading.Timer(2.0, label.destroy)
    timer.start()


def show_comps():
    comps, status = completions()
    ic = "info" if 0 == status else "error" if 1 == status else "warning"
    messagebox._show("completions", comps, _icon=ic)

    if not status:
        temp_label_input(comps)


def start_app():

    root.title(string='Great AutoCompletion!!')
    root.iconphoto(False, PhotoImage(file='icon.png'))
    root.geometry('500x500')
    init_system()

    lab = Label(root, text='please enter a string to search')
    lab.pack()

    e = Entry(root, textvariable=user_input)
    e.pack()

    search_button = Button(root, text="Search", command=show_comps)
    search_button.pack()

    mainloop()
