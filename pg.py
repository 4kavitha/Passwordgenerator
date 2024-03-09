from tkinter import *
import random
import string

pg = Tk()
pg.geometry("450x450")
pg.title("PASSWORD GENERATOR")
pg.configure(bg="#52bdff")
Label(pg, text="PASSWORD GENERATOR", font='ariel 15 bold', bg="#52bdff").pack()
pass_label = Label(pg, text='PASSWORD LENGTH', font='ariel 10 bold', bg="#52bdff")
pass_label.pack(pady=10)
pass_len = IntVar()
length = Spinbox(pg, from_=6, to_=12, textvariable=pass_len, width=12)
length.pack()

pass_str = StringVar()



def Generator():
    password = ''
    for x in range(0, 4):
        password += random.choice(string.ascii_uppercase) + random.choice(string.ascii_lowercase)
    for y in range(0, pass_len.get() - 4):
        password += random.choice(string.ascii_uppercase + string.ascii_lowercase + string.digits + string.punctuation)
    pass_str.set(password)

Generate = Button(pg, text="GENERATE PASSWORD", command=Generator, padx=5, pady=5)
Generate.configure(background="yellow", foreground="red", font=('ariel', 10, 'bold'))
Generate.pack(side=TOP, pady=20)

Entry(pg, textvariable=pass_str).pack()

def ok_button():
    pg.destroy()

ok_button = Button(pg, text="OK", command=ok_button, padx=5, pady=5)
ok_button.configure(background="yellow", foreground="red", font=('ariel', 10, 'bold'))
ok_button.pack(side=BOTTOM, pady=20)

pg.mainloop()

