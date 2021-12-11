import tkinter


def main():

    root_win = tkinter.Tk()
    root_win.title("LEX CROP Encrypted.")

    app_wid = tkinter.Label(root_win)
    app_wid.configure(text="""

Copyright © 2021 Blue Sky Inc. All rights reserved.

Privacy - PolicyTerms of UseSales - PolicyLegalSite Map
""")
    app_wid.pack(side='bottom', expand=0, fill='both')

    root_win.mainloop()


main()
