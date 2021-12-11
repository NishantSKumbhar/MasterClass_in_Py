import tkinter


def main():
    root_app = tkinter.Tk()
    root_app.title("Blue Sky Inc.")

    app_widget = tkinter.Label(root_app)
    app_widget.configure(text="Hello Blue Sky.")
    app_widget.pack(side=tkinter.TOP, expand=tkinter.YES, fill=tkinter.BOTH)

    root_app.mainloop()


main()
