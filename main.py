from tkinter import *
from tkinter import ttk
from tkinter import Menu

from tkinter.ttk import *
from tkinter.filedialog import askopenfile 
import time

import requests

################################################### GUI stuff ###################################################
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
    Label(root, text='File Uploaded Successfully!', foreground='green').grid(row=4, columnspan=3, pady=1)
        
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
uploadFileButton.grid(row=0, columnspan=3, pady=1)




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



################################################### API stuff ###################################################
# Register new webhook for earnings
r = requests.post('https://finnhub.io/api/v1/webhook/add?token=cdo4chiad3i5o5ol2cg0cdo4chiad3i5o5ol2cgg', json={'event': 'earnings', 'symbol': 'AAPL'})
res = r.json()
print(res)

webhook_id = res['id']
# List webhook
r = requests.get('https://finnhub.io/api/v1/webhook/list?token=cdo4chiad3i5o5ol2cg0cdo4chiad3i5o5ol2cgg')
res = r.json()
print(res)

#Delete webhook
r = requests.post('https://finnhub.io/api/v1/webhook/delete?token=cdo4chiad3i5o5ol2cg0cdo4chiad3i5o5ol2cgg', json={'id': webhook_id})
res = r.json()
print(res)


#####################################
response = requests.get('https://api.fiscaldata.treasury.gov/services/api/fiscal_service/v1/accounting/od/rates_of_exchange')
print(response.text)