from tkinter import *
import random

def updatebtn(btn):
    global current
    try:
        lines[current].config(text=btn.cget('text'))
        current += 1
    except:
        lbl.config(text='Guess the Motherfucking Number!')

def restart():
    global current
    for line in lines:
        line.config(text='_')
    current = 0

def check():
    global tries
    if tries >= 10:
        lbl.config(text='Sorry, you have reached the maximum number of tries.')
        return
    
    correct_number = ''.join(str(random.randint(1, 6)) for _ in range(5))
    
    guessed_number = ''.join(map(lambda line: line.cget('text'), lines))
    correct_position = sum(map(lambda x, y: x == y, correct_number, guessed_number))
    
    if correct_position == 5:
        lbl.config(text=f'Congratulations! You guessed the correct number and position in {tries} tries!')
    else:
        tries += 1
        lbl.config(text=f'Correct digits in position: {correct_position}. Try again! Attempts remaining: {10 - tries}')

    

root = Tk()
root.title('Guess the Number')
root.geometry('600x500')
root.resizable(False, False)
root.configure(bg="#333333")
font = ('Arial', 20)

lbl = Label(root, text='Guess the Motherfucking Number!',font=font,bg='#333333',fg='white')
lbl.pack(pady=10)

frame1 = Frame(root,bg='#333333')
frame1.pack()

cornum1 = Label(frame1, text='Correct Number:',font=font,bg='#333333',fg='white')
cornum1.grid(row=0, column=0, padx=5, pady=10)
cornum = Label(frame1, text='0',font=font,bg='#333333',fg='white')
cornum.grid(row=0, column=1, padx=5, pady=10)
corpos1 = Label(frame1, text='Correct Position:',font=font,bg='#333333',fg='white')
corpos1.grid(row=1, column=0, padx=5, pady=10)
corpos = Label(frame1, text='0',font=font,bg='#333333',fg='white')
corpos.grid(row=1, column=1, padx=5, pady=10)

frame = Frame(root,bg="#333333")
frame.pack()

btn1 = Button(frame, text='1', font=font,command=lambda: updatebtn(btn1))
btn1.grid(row=0, column=0, padx=5, pady=10)
btn2 = Button(frame, text='2', font=font,command=lambda: updatebtn(btn2))
btn2.grid(row=0, column=1, padx=5, pady=10)
btn3 = Button(frame, text='3', font=font,command=lambda: updatebtn(btn3))
btn3.grid(row=0, column=2, padx=5, pady=10)
btn4 = Button(frame, text='4', font=font,command=lambda: updatebtn(btn4))
btn4.grid(row=0, column=3, padx=5, pady=10)
btn5 = Button(frame, text='5', font=font,command=lambda: updatebtn(btn5))
btn5.grid(row=0, column=4, padx=5, pady=10)
btn6 = Button(frame, text='6', font=font,command=lambda: updatebtn(btn6))
btn6.grid(row=0, column=5, padx=5, pady=10)
btns = Button(frame,text='Submit',font=font,bg='green',fg='white',command=check)
btns.grid(row=0,column=6,padx=5,pady=10)
btnd = Button(frame,text='Delete',font=font,bg='green',fg='white',command=restart)
btnd.grid(row=0,column=7,padx=5,pady=10)

frame2 = Frame(root,bg="#333333")
frame2.pack()

line1 = Label(frame2,text='_',font=font,bg='#333333',fg='white')
line1.grid(row=0,column=0,pady=10)
line2 = Label(frame2,text='_',font=font,bg='#333333',fg='white')
line2.grid(row=0,column=1,pady=10)
line3 = Label(frame2,text='_',font=font,bg='#333333',fg='white')
line3.grid(row=0,column=2,pady=10)
line4 = Label(frame2,text='_',font=font,bg='#333333',fg='white')
line4.grid(row=0,column=3,pady=10)
line5 = Label(frame2,text='_',font=font,bg='#333333',fg='white')
line5.grid(row=0,column=4,pady=10)

lines = [line1,line2,line3,line4,line5]
current = 0
tries = 0

root.mainloop()
