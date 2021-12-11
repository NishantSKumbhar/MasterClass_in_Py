import sys
import tkinter
import sys


def main():

    root_win = tkinter.Tk()
    root_win.title("LEX CROP Encrypted.")

    app_wid = tkinter.Label(root_win)
    app_wid.configure(text="""

Copyright © 2021 Blue Sky Inc. All rights reserved.

Privacy - PolicyTerms of UseSales - PolicyLegalSite Map
""")
    app_wid.pack(side=tkinter.BOTTOM, expand=tkinter.NO, fill=tkinter.BOTH)

    app_button = tkinter.Button(root_win)
    app_button.configure(text="Quit", command=sys.exit)
    app_button.pack(side=tkinter.BOTTOM)

    root_win.mainloop()


main()
