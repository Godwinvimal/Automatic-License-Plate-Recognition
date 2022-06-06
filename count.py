import tkinter


def hi():
        print(startEntry.get())


root=tkinter.Tk()

startLabel =tkinter.Label(root, text="Enter Star: ")
startEntry=tkinter.Entry(root)


startLabel.pack()
startEntry.pack()

plotButton= tkinter.Button(root,text="plot", command=hi)

plotButton.pack()

root.mainloop()