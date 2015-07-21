import tkinter as tk
import random
import time

root = tk.Tk(className = 'Random Name Generator')
w = 800
h = 600
ws = root.winfo_screenwidth()
hs = root.winfo_screenheight()
x = (ws/2) - (w/2)
y = (hs/2) - (h/2)
root.geometry('%dx%d+%d+%d' % (w, h, x, y))

class Window:
    def __init__(self, master):
        self.frame = tk.Frame(master)
        self.text = tk.StringVar()
        self.ranNameLabel = tk.Label(self.frame, textvariable = self.text, font=("Helvetica", 40), height = 3, width = 15)
        self.genButton = tk.Button(self.frame, text = 'Generate Random Name', command = self.genRanName, font = ('Helvertica', 18))
        self.ranNameLabel.grid(row = 0)
        self.genButton.grid(row = 1)
        self.frame.grid()
        self.NAMES = ['alfonso', 'cale', 'chris', 'colin', 'derrick', 'jeffrey', 'jessica', 'rohit', 'tammy', 'will', 'yulin', 'albert', 'robert']
        self.USED = []

    def genRanName(self):
        i = 0
        while i <= 50:
            root.update()
            if i > 30:
                time.sleep(0.4)
                self.helper()
            elif i > 40:
                time.sleep(0.6)
                self.helper()
            elif i > 45:
                time.sleep(1)
                self.helper()
            else:
                time.sleep(0.2)
                self.helper()
            if i == 50:
                name = self.text.get()
                self.USED.append(name)
                self.NAMES.remove(name)
                if not self.NAMES:
                    self.NAMES = self.USED
                    self.USED = []  
            i += 1    

    def helper(self):
        fonts = "#"+("%06x"%random.randint(0,16777215))
        backgrounds = "#"+("%06x"%random.randint(0,16777215))
        self.frame.configure(background = backgrounds)
        self.genButton.configure(highlightbackground = backgrounds)
        self.ranNameLabel.config(foreground = fonts)
        self.text.set(random.choice(self.NAMES))

def main():
    app = Window(root)
    app.frame.configure(padx=250, pady=225, height=300)
    root.mainloop()

if __name__ == '__main__':
    main()