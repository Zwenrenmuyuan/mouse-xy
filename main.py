import tkinter as tk

from tracker import MouseTrackerApp


def main():
    root = tk.Tk()
    MouseTrackerApp(root)
    root.mainloop()


if __name__ == "__main__":
    main()
