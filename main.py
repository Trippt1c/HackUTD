from tkinter import *
from tkinter import ttk
from tkinter import Menu

from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

# basic GUI app
root = Tk()
frm = ttk.Frame(root, padding=150)
frm.grid()
ttk.Label(frm, text="[INSERT TEAM NAME]").grid(column=0, row=0)
ttk.Label(frm, text="\n").grid(column=0, row=1)
ttk.Label(frm, text="Upload a .csv file:").grid(column=0, row=2)
ttk.Label(frm, text="\n").grid(column=0, row=3)
ttk.Label(frm, text="\n").grid(column=0, row=4)
ttk.Label(frm, text="\n").grid(column=0, row=5)
ttk.Button(frm, text="Quit", command=root.destroy).grid(column=0, row=20)

# button
def open_file():
    file_path = askopenfile(mode='r', filetypes=[('.csv files', '*csv')])
    if file_path is not None:
        pass

def uploadFiles():
    pb1 = Progressbar(
        root, 
        orient=HORIZONTAL, 
        length=300, 
        mode='determinate'
        )
    pb1.grid(row=4, columnspan=3, pady=20)
    for i in range(5):
        root.update_idletasks()
        pb1['value'] += 20
        time.sleep(1)
    pb1.destroy()
    Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=10)
        
chooseFileButton = Button(
    root, 
    text ='Choose File', 
    command = lambda:open_file()
    ) 
chooseFileButton.grid(row=0, column=0)

uploadFileButton = Button(
    root, 
    text='Upload File',
    command=uploadFiles
    )
uploadFileButton.grid(row=0, columnspan=3, pady=10)




# navigation bar at the top
menubar = Menu(root)
root.config(menu=menubar)

file_menu = Menu(
    menubar,
    tearoff=0
)
file_menu.add_command(label='New')
file_menu.add_command(label='Open...')
menubar.add_cascade(
    label="Home",
    menu=file_menu
)

stock_menu = Menu(
    menubar,
    tearoff=0
)
stock_menu.add_command(label='Welcome')
stock_menu.add_command(label='About...')
menubar.add_cascade(
    label="Stock",
    menu=stock_menu
)

bonds_menu = Menu(
    menubar,
    tearoff=0
)
bonds_menu.add_command(label='Welcome')
bonds_menu.add_command(label='About...')
menubar.add_cascade(
    label="Bonds",
    menu=bonds_menu
)

savings_menu = Menu(
    menubar,
    tearoff=0
)
savings_menu.add_command(label='Welcome')
savings_menu.add_command(label='About...')
menubar.add_cascade(
    label="Savings",
    menu=savings_menu
)

root.mainloop()

