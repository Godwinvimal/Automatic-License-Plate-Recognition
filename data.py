import csv
import tkinter as tk

def store():
    file = open("dataset/storedata.csv")
    reader = csv.reader(file)
    lines = len(list(reader))

    count = lines

    with open('dataset/storedata.csv', 'a') as csvfile:
        writer = csv.writer(csvfile, lineterminator='\n')
        writer.writerow([str(count), (entry1.get())])

root = tk.Tk()


canvas1 = tk.Canvas(root, width=300, height=300)
canvas1.pack()

entry1 = tk.Entry(root)
canvas1.create_window(150, 100, window=entry1)

button1 = tk.Button(root, text='Add Data ', bg='green', fg='white', command=store)
canvas1.create_window(150, 140, window=button1)

var = tk.StringVar()
user_name = tk.Entry(root, textvariable=var)


root.mainloop()
