import tkinter as tk
import tkinter.font as tkFont
from enum import Enum


class WidgetTypes(Enum):
    LABEL = 0
    BUTTON = 1
    EDITOR = 2


def add_widget(root, widget_type=WidgetTypes.LABEL, pos_x=0, pos_y=0, width=0, height=0, text="label"):
    widget = None
    if WidgetTypes.LABEL == widget_type:
        widget = tk.Label(root)
    elif WidgetTypes.BUTTON == widget_type:
        widget = tk.Button(root)
    elif WidgetTypes.EDITOR == widget_type:
        widget = tk.Entry(root)
        widget["cursor"] = "dotbox"


    ft = tkFont.Font(family='Times', size=10)
    widget["font"] = ft
    widget["fg"] = "black"
    widget["bg"] = "lightgray"
    widget["justify"] = "center"
    widget["text"] = text
    widget.place(x=pos_x, y=pos_y, width=width, height=height)
    return widget


class App:
    def __init__(self, root):
        # setting window size
        width = 800
        height = 600
        screenwidth = root.winfo_screenwidth()
        screenheight = root.winfo_screenheight()
        spacer = (" " * (int(screenwidth) // 10))
        root.title(spacer + "bupa8694")
        alignstr = '%dx%d+%d+%d' % (width, height, (screenwidth - width) / 2, (screenheight - height) / 2)
        root.geometry(alignstr)
        root.resizable(width=False, height=False)

        frame_1 = tk.Frame(root, width=600, height=600, bg='yellow')
        frame_1.pack_propagate(0)
        frame_1.pack(fill='both', side='left', expand='False')

        frame_2 = tk.Frame(root, width=200, height=600, bg='lightgray')
        frame_2.pack_propagate(0)
        frame_2.pack(fill='both', side='right', expand='False')

        w_lbl_amount = add_widget(frame_2, WidgetTypes.LABEL, 0, 0, 70, 25, "Amount:")
        w_button_amount = add_widget(frame_2, WidgetTypes.EDITOR, 80, 2, 70, 25, "2")


if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
