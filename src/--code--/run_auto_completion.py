import autoCompletion
import autoCompletion_gui
import sys


if __name__ == "__main__":

    if len(sys.argv) >= 2 and "gui" == sys.argv[1]:
        autoCompletion_gui.start_app()
    else:
        autoCompletion.start_app()
