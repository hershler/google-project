from autoCompletion_gui import AutoCompGui
from autoCompletion import AutoComp
import sys


if __name__ == "__main__":

    if len(sys.argv) >= 2 and "gui" == sys.argv[1]:
        gui = AutoCompGui()
        gui.start_app()
    else:
        auto_comp = AutoComp()
        auto_comp.start_app()
