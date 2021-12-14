from tkinter import Tk
from ui.ui import UI


def main():
    window = Tk()
    window.title('WordList')

    user_intrface = UI(window)
    user_intrface.start()

    window.mainloop()


if __name__ == '__main__':

    main()
