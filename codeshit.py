from tkinter import *
from tkinter import messagebox

def radop():
    selop = radbtn.get()

    if selop == '1':
        def sadge():
            if chkbtn.get():
                messagebox.showinfo('Congrats','Congrats, You are Aware of Yourself!')
            else:
                messagebox.showinfo('Hell Nah','You Cappin, you a fucking restarted')

        root.destroy()
        newroot = Tk()
        newroot.title('YOU CHOSE 1')
        newroot.geometry('250x100')

        chkbtn = IntVar()
        chkr = Checkbutton(newroot,text='Check if you are a restarted',variable=chkbtn)
        chkr.pack(pady=10)

        cbtn = Button(newroot,text='Confirm',command=sadge)
        cbtn.pack(pady=10)
        newroot.mainloop()

    if selop == '2':
        def rizzave(value):
            if value in (0,1,2,3,4,5):
                messagebox.showinfo('NO KING','No King, you are more than that, stop underrating yourself!')
            elif value in (6,7):
                messagebox.showinfo('YUP','Sounds about right')
            elif value in (8,9):
                messagebox.showwarning('the fuck','hell fucking nah')
            else:
                messagebox.showerror('CAP','You don\'t even deserve that rating, you\'re a fucking loser who have no bitches and will have no bitches in life so stop overrating yourself you useless cock, you should k1ll yourself tbh')
            
        def rizz():
            value = scale.get()
            rizzave(value)

        root.destroy()
        newroot1 = Tk()
        newroot1.title('YOU CHOSE 2')
        newroot1.geometry('800x400')

        scla = Label(newroot1,text='RATE YOUR RIZZ',font=fnt)
        scla.pack(pady=20)
        scale = Scale(newroot1,from_=0,to=10,orient=HORIZONTAL, font=fnt)
        scale.pack(pady=10)


        scbtn = Button(newroot1,text='Rate',command=rizz)
        scbtn.pack()
        newroot1.mainloop()

    if selop == '3':

        def textget():
            content = textwid.get('1.0', 'end-1c')
            message = "The message '{}' radiates a bitchless energy. You should go outside and touch some grass, you fucking loser!".format(content)
            messagebox.showerror('RESTARTED ALERT', message)

        root.destroy()
        newroot2 = Tk()
        newroot2.title('YOU CHOSE 3')
        newroot2.geometry('800x400')

        head = Label(newroot2,text='What\'s on your mind?',font=fnt)
        head.pack(pady=10)

        textwid = Text(newroot2,wrap='word',height=10,width=40)
        textwid.pack(padx=10,pady=10)

        tbtn = Button(newroot2,text='Submit',command=textget)
        tbtn.pack()

        newroot2.mainloop()

    if selop == '4':

        def opti():
            getc = selopt.get()

            if getc == '1':
                messagebox.showwarning('wtf am i doing','I just wasted my time coding for this nonsense why the hell am I doing this')
                newroot3.destroy()
            
            if getc == '2':
                messagebox.showinfo('fact','I poop 3-5 times a day.')
                newroot3.destroy()
            
            if getc == '3':
                messagebox.showwarning('?','am I going to be a successful developer?\nam I going to gave a successful future?\nam I going to have a good life?\nI don\'t know....')
                newroot3.destroy()
            
            if getc == '4':
                messagebox.showinfo('.|.','tite.')
                newroot3.destroy()

        root.destroy()
        newroot3 = Tk()
        newroot3.title('YOU CHOSE 4')
        newroot3.geometry('800x400')

        hea = Label(newroot3,text='CHOOSE BELOW',font=fnt)
        hea.pack(pady=20)

        opt = ['1','2','3','4']
        selopt = StringVar()
        selopt.set(opt[0])
        combo = OptionMenu(newroot3,selopt,*opt)
        combo.pack(pady=10)

        obtn = Button(newroot3,text='Select',command=opti)
        obtn.pack(pady=10)

        newroot3.mainloop()


root = Tk()
root.title('MY FUCKING PROJECT')
root.geometry('800x400')
fnt = ('Arial',20)

header = Label(root,text='CHOOSE ONE BELOW', font=fnt)
header.pack(pady=40)

radbtn = StringVar()
rad1 = Radiobutton(root,text='1',variable=radbtn,value="1",font=fnt)
rad2 = Radiobutton(root,text='2',variable=radbtn,value="2",font=fnt)
rad3 = Radiobutton(root,text='3',variable=radbtn,value="3",font=fnt)
rad4 = Radiobutton(root,text='4',variable=radbtn,value="4",font=fnt)
rad1.pack()
rad2.pack()
rad3.pack()
rad4.pack()
radbtn.set(None)

btn = Button(root,text="Confirm",command=radop)
btn.pack()
root.mainloop()