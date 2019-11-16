from tkinter import *
#import Image
# from PIL import Image   # pip install pillow


def printt():
    fng = fn.get()
    lng = ln.get()
    dbg = db.get()
    vrg = var.get()
    adg = ad.get()
    ctg = ct.get()
    pcg = pc.get()
    phg = ph.get()
    emg = em.get()

    print("Welcome to Suhumar's Tkinter Tutorial")
    print("First Name   :",fng)
    print("Last Name    :",lng)
    print("Date of Birth:",dbg)
    print("Address      :",vrg)
    print("Address      :",adg)
    print("City         :",ctg)
    print("Post Code    :",pcg)
    print("Phone Number :",phg)
    print("Email Adress :",emg)





def exit1():
    exit()


window = Tk()
fn = StringVar()
ln = StringVar()
db = StringVar()
ad = StringVar()
ct = StringVar()
pc = StringVar()
ph = StringVar()
em = StringVar()
var = StringVar()

window.geometry("500x900")
window.title("Welcome to Book Club")

image = PhotoImage(file="D:\pycharm\person.png")
itt = Label(window, image=image)#.pack()
itt.place(x= 190, y=0)

#Krishnana picture
#image = PhotoImage(file="D:\pycharm\krishnan.gif")
#krish = Label(window, image=image)#.pack()
#krish.place(x= 475, y=35)

list1 = [" ","85 Essex Road", "87 Essex Road", "89 Essex Road", "91 Essex Road", "93 Essex Road", "95 Essex Road", "97 Essex Road", "99 Essex Road", "101 Essex Road","103 Essex Road","105 Essex Road","107 Essex Road","109 Essex Road","111 Essex Road"]


label = Label(window, text="Welcome to Suhumar's Tkinter Tutorial", fg="dark blue", relief="solid", font=("arial", 18, "bold"))
label.pack(fill=BOTH, padx=4, pady=90)
#label.grid(row=1, column=30)
#label2 = Label(window, text="", bg="light gray",
#               relief="solid").pack(fill=BOTH, expand=True)
# label2.pack(fill=BOTH)#,padx=1, pady=1)
label3 = Label(window, text="Registration Form",fg="red", font=("arial", 16, "bold")).place(x=140, y=140)
# oR for Filling the whole BG Colour
#label = Label(window, text="Welcome to Suhumar's Tkinter Tutorial Lession", fg="blue", bg= "yellow", relief = 'solid', font=("arial", 14, "bold"))
# label.pack(fill=BOTH,pady=2, padx=2, expand = True)# expand true fills the bg colour
fname = Label(window, text="First Name", fg="black", font=("times roman", 12, ))
fname.place(x=140, y=210)
fnentry = Entry(window, textvar=fn, fg="black", font=("arial", 12))
fnentry.place(x=140, y=230)

lname = Label(window, text="Last Name ", fg="black", font=("times roman", 12))
lname.place(x=140, y=270)
lnentry = Entry(window, textvar=ln, fg="black", font=("arial", 12))
lnentry.place(x=140, y=290)

dob = Label(window, text="Date of Birth", fg="black", font=("times roman", 12))
dob.place(x=140, y=330)
dbentry = Entry(window, textvar=db, fg="black", font=("arial", 12))
dbentry.place(x=140, y=350)

add = Label(window, text="Address", fg="black", font=("times roman", 12))
add.place(x=140, y=410)
droplist=OptionMenu(window,var,*list1)
var.set("Select an Option")
droplist.config(width=16, fg="black")
droplist.place(x=220, y=410)
adentry = Entry(window, textvar=ad, fg="black", font=("arial", 12))
adentry.place(x=220, y=440)

cty = Label(window, text="City", fg="black", font=("times roman", 12))
cty.place(x=140, y=460)
ctentry = Entry(window, textvar=ct, fg="black", font=("arial", 12))
ctentry.place(x=140, y=490)

pcod = Label(window, text="Post Code", fg="black", font=("times roman", 12))
pcod.place(x=140, y=530)
pcentry = Entry(window, textvar=pc, fg="black", font=("arial", 12))
pcentry.place(x=140, y=560)

phn = Label(window, text="Telephone", fg="black", font=("times roman", 12))
phn.place(x=140, y=600)
phentry = Entry(window, textvar=ph, fg="black", font=("arial", 12))
phentry.place(x=140, y=630)

eml = Label(window, text="Email @", fg="black", font=("times roman", 12))
eml.place(x=140, y=670)
ementry = Entry(window, textvar=em,  fg="black", font=("arial", 12))
ementry.place(x=140, y=700)

b1 = Button(window, text="Create", width=12, bg = 'brown', fg='white', command=printt)
b1.place(x=200, y=750)

b2 = Button(window, text="Exit", width=12,bg = 'brown', fg='white', command=exit1)
b2.place(x=300, y=750)

window.mainloop()
