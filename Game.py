from tkinter import  *
import tkinter.font as font
import tkinter.messagebox as mb
import random as rand
from point import point as p

class messageBox:
    def __init__(self,CTP):
        box=self.box=Toplevel()
        self.input=Entry(box,width=10)
        self.input.grid(row=0,column=1)
        if(CTP):
            box.title("Change Cash to Point")
            Label(box,text='Enter Cash ',font=font.Font(size=12)).grid(row=0,column=0)
            Button(box,text='OK',font=font.Font(size=12),command=self.CashToPoint).grid(row=1,column=1)
            Button(box,text='Cancel',font=font.Font(size=12),command=self.box.destroy).grid(row=1,column=0)
        else:
            box.title("Change points to Cash")
            Label(box,text='Enter Points ',font=font.Font(size=12)).grid(row=0,column=0)
            Button(box,text='OK',font=font.Font(size=12),command=self.PointToCash).grid(row=1,column=1)
            Button(box,text='Cancel',font=font.Font(size=12),command=self.box.destroy).grid(row=1,column=0)

    def CashToPoint(self):
        self.value=self.input.get()
        if(not self.value.isnumeric() or int(self.value)<0):
            self.value=0
        p.total+=int(self.value)+int(int(self.value)/10)
        lblpt3.configure(text='Points - '+str(p.total))
        self.box.destroy()

    def PointToCash(self):
        self.value=(self.input.get())
        if(not self.value.isnumeric() or int(self.value)<0 ):
            self.value=0
        if(int(self.value)>p.total):
            self.value=p.total
        p.total-=int(self.value)
        lblpt3.configure(text='Points - '+str(p.total))
        self.box.destroy()

def message1():
    a=messageBox(True)

def message2():
    a=messageBox(False)


app=Tk()
app.attributes('-fullscreen',True)
app.configure(bg='black')
app.title("Gambling Game")

start=Frame(app,width=app.winfo_screenwidth(),height=app.winfo_screenheight(),bg='black')
menu=Frame(app,bg='black')
exchange=Frame(app,bg='black')
game1=Frame(app,bg='black')
game2=Frame(app,bg='black')

for frame in (start,menu,exchange,game1,game2):
    frame.grid(row=0,column=0,sticky='nesw')

start.tkraise()
lblpt1=Label(start,text='Points - '+str(p.total),font=font.Font(size=15),fg='white',bg='black')
lblpt1.place(x=1200,y=10)
lblpt2=Label(menu,text='Points - '+str(p.total),font=font.Font(size=15),fg='white',bg='black')
lblpt2.place(x=1200,y=10)
lblpt3=Label(exchange,text='Points - '+str(p.total),font=font.Font(size=15),fg='white',bg='black')
lblpt3.place(x=1200,y=10)
lblpt4=Label(game1,text='Points - '+str(p.total),font=font.Font(size=15),fg='white',bg='black')
lblpt4.place(x=1200,y=10)
lblpt5=Label(game2,text='Points - '+str(p.total),font=font.Font(size=15),fg='white',bg='black')
lblpt5.place(x=1200,y=10)

def changeFrame(name):
    frame=name
    frame.tkraise()
    lblpt1.configure(text='Points - '+str(p.total))
    lblpt2.configure(text='Points - '+str(p.total))
    lblpt3.configure(text='Points - '+str(p.total))
    lblpt4.configure(text='Points - '+str(p.total))
    lblpt5.configure(text='Points - '+str(p.total))


#for start page
btnmenu=Button(start,text='Games',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(menu))
btnmenu.place(x=300,y=250)
btnexchange=Button(start,text='Exchange',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(exchange))
btnexchange.place(x=1000,y=250)
btnexit=Button(start,text='Quit',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=app.destroy)
btnexit.place(x=700,y=600)

#for exchange page
btnback=Button(exchange,text='Back',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(start))
btnback.place(x=10,y=10)
btnEx1=Button(exchange,text='Cash to Points',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=message1)
btnEx1.place(x=300,y=250)
btnEx2=Button(exchange,text='Points to Cash',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=message2)
btnEx2.place(x=1000,y=250)

#for game menu
btnback1=Button(menu,text='Back',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(start))
btnback1.place(x=10,y=10)
btnG1=Button(menu,text='Game 1',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(game1))
btnG1.place(x=450,y=450)
btnG2=Button(menu,text='Game 2',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(game2))
btnG2.place(x=900,y=450)

#for Game 1
selectNumber=0
betamount=0
btnback2=Button(game1,text='Back',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(menu))
btnback2.place(x=10,y=10)
btnNum1=Button(game1,text='1',width=20,height=10,bg='black',fg='white',font=font.Font(size=15))
btnNum1.place(x=100,y=500)
btnNum2=Button(game1,text='2',width=20,height=10,bg='black',fg='white',font=font.Font(size=15))
btnNum2.place(x=300,y=500)
btnNum3=Button(game1,text='3',width=20,height=10,bg='black',fg='white',font=font.Font(size=15))
btnNum3.place(x=500,y=500)
btnNum4=Button(game1,text='4',width=20,height=10,bg='black',fg='white',font=font.Font(size=15))
btnNum4.place(x=700,y=500)
btnNum5=Button(game1,text='5',width=20,height=10,bg='black',fg='white',font=font.Font(size=15))
btnNum5.place(x=900,y=500)
btnNum6=Button(game1,text='6',width=20,height=10,bg='black',fg='white',font=font.Font(size=15))
btnNum6.place(x=1100,y=500)
buttons=[btnNum1,btnNum2,btnNum3,btnNum4,btnNum5,btnNum6]
inputBet=Spinbox(game1,from_=0,to=1000,bg='black',fg='white',font=font.Font(size=15))
inputBet.place(x=500,y=450)
btnstartG1=Button(game1,text='Start Rolling',bg='black',fg='white',font=font.Font(size=15),state=DISABLED)
btnstartG1.place(x=1100,y=450)
btnBetG1=Button(game1,text='BET',bg='black',fg='white',font=font.Font(size=15),state=DISABLED)
btnBetG1.place(x=750,y=450)
lblRes1=Label(game1,text='\n  O',width=10,height=5,bg='#555555',fg='white',font=font.Font(size=15))
lblRes1.place(x=500,y=100)

def selectNum1(n):
    global buttons,selectNumber
    selectNumber =n+1
    print('selected number = '+str(n+1))
    i=0
    while i<6:
        if(i != n):
            buttons[i].configure(bg='black',fg='white',state=NORMAL)
        else:
            buttons[i].configure(bg='white',fg='black',state=DISABLED)
        i+=1
    btnBetG1.configure(state=NORMAL)

def bet1():
    global betamount,buttons
    b=inputBet.get()
    if(not b.isnumeric()):
        b=0
    else:
        if(int(b)>p.total):
            mb.showerror(title='Invalid',message='Not Enough Points')
        else:
            p.total -= int(b)
            betamount = int(b)
            lblpt4.configure(text='Points - ' + str(p.total))
            btnstartG1.configure(state=NORMAL)
            btnBetG1.configure(state=DISABLED)
            for btn in buttons:
                btn.configure(state=DISABLED)

def reset1():
    global buttons,btnBetG1,btnstartG1
    lblpt4.configure(text='Points - '+str(p.total))
    for btn in buttons:
        btn.configure(bg='black',fg='white',state=NORMAL)
    btnBetG1.configure(state=DISABLED)
    btnstartG1.configure(state=DISABLED)

def startGame1():
    global lblRes1,selectNumber
    num=0
    for i in range(12):
        num = rand.randint(1, 6)
        print(num)
        if (num == 1):
            lblRes1.configure(text='\n  O')
        elif (num == 2):
            lblRes1.configure(text='    O\n\nO')
        elif (num == 3):
            lblRes1.configure(text='    O\n  O\nO')
        elif (num == 4):
            lblRes1.configure(text='O   O\n\nO   O')
        elif (num == 5):
            lblRes1.configure(text='O   O\n  O\nO   O')
        elif (num == 6):
            lblRes1.configure(text='O   O\nO   O\nO   O')
    print('SN-'+str(selectNumber))
    if(num==selectNumber):
        p.total+=betamount*5
        mb.showinfo(title='Congratulation',message='U win'+str(betamount*5))
    else:
        mb.showinfo(title='Sad',message='U lost !!')
    reset1()

btnstartG1.configure(command=startGame1)
btnBetG1.configure(command=bet1)
btnNum1.configure(command=lambda:selectNum1(0))
btnNum2.configure(command=lambda:selectNum1(1))
btnNum3.configure(command=lambda:selectNum1(2))
btnNum4.configure(command=lambda:selectNum1(3))
btnNum5.configure(command=lambda:selectNum1(4))
btnNum6.configure(command=lambda:selectNum1(5))

#for game 2
btnback3=Button(game2,text='Back',borderwidth=0,bg='black',fg='white',font=font.Font(size=15),command=lambda:changeFrame(menu))
btnback3.place(x=10,y=10)
#btnN1=Button(game2,text='1',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
#btnN1.place(x=100,y=500)
btnN2=Button(game2,text='2',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN2.place(x=200,y=500)
btnN3=Button(game2,text='3',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN3.place(x=300,y=500)
btnN4=Button(game2,text='4',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN4.place(x=400,y=500)
btnN5=Button(game2,text='5',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN5.place(x=500,y=500)
btnN6=Button(game2,text='6',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN6.place(x=600,y=500)
btnN7=Button(game2,text='7',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN7.place(x=700,y=500)
btnN8=Button(game2,text='8',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN8.place(x=800,y=500)
btnN9=Button(game2,text='9',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN9.place(x=900,y=500)
btnN10=Button(game2,text='10',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN10.place(x=1000,y=500)
btnN11=Button(game2,text='11',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN11.place(x=1100,y=500)
btnN12=Button(game2,text='12',width=10,height=5,bg='black',fg='white',font=font.Font(size=15))
btnN12.place(x=1200,y=500)
buttonsG2=[btnN2,btnN3,btnN4,btnN5,btnN6,btnN7,btnN8,btnN9,btnN10,btnN11,btnN12]
inputBet2=Spinbox(game2,from_=0,to=1000,bg='black',fg='white',font=font.Font(size=15))
inputBet2.place(x=500,y=450)
btnstartG2=Button(game2,text='Start Rolling',bg='black',fg='white',font=font.Font(size=15),state=DISABLED)
btnstartG2.place(x=1100,y=450)
btnBetG2=Button(game2,text='BET',bg='black',fg='white',font=font.Font(size=15),state=DISABLED)
btnBetG2.place(x=750,y=450)
lblRes2=Label(game2,text='\n  O',width=10,height=5,bg='#555555',fg='white',font=font.Font(size=15))
lblRes2.place(x=400,y=100)
lblRes3=Label(game2,text='\n  O',width=10,height=5,bg='#555555',fg='white',font=font.Font(size=15))
lblRes3.place(x=600,y=100)

def selectNum2(n):
    global buttonsG2, selectNumber
    selectNumber = n + 2
    print('selected number = ' + str(n + 2))
    i = 0
    while i < 11:
        if (i != n):
            buttonsG2[i].configure(bg='black', fg='white', state=NORMAL)
        else:
            buttonsG2[i].configure(bg='white', fg='black', state=DISABLED)
        i += 1
    btnBetG2.configure(state=NORMAL)

def bet2():
    global betamount,buttonsG2
    b=inputBet2.get()
    if(not b.isnumeric()):
        b=0
    else:
        if(int(b)>p.total):
            mb.showerror(title='Invalid',message='Not Enough Points')
        else:
            p.total -= int(b)
            betamount = int(b)
            lblpt5.configure(text='Points - ' + str(p.total))
            btnstartG2.configure(state=NORMAL)
            btnBetG2.configure(state=DISABLED)
            for btn in buttonsG2:
                btn.configure(state=DISABLED)

def reset2():
    global buttonsG2,btnBetG2,btnstartG2
    lblpt5.configure(text='Points - '+str(p.total))
    for btn in buttonsG2:
        btn.configure(bg='black',fg='white',state=NORMAL)
    btnBetG2.configure(state=DISABLED)
    btnstartG2.configure(state=DISABLED)

def startGame2():
    global lblRes2,lblRes3,selectNumber,betamount
    num1=0
    num2=0
    for i in range(12):
        num1 = rand.randint(1, 6)
        num2 = rand.randint(1,6)
        if (num1 == 1):
            lblRes2.configure(text='\n  0')
        elif (num1 == 2):
            lblRes2.configure(text='    O\n\nO')
        elif (num1 == 3):
            lblRes2.configure(text='    O\n  O\nO')
        elif (num1 == 4):
            lblRes2.configure(text='O   O\n\nO   O')
        elif (num1 == 5):
            lblRes2.configure(text='O   O\n  O\nO   O')
        elif (num1 == 6):
            lblRes2.configure(text='O   O\nO   O\nO   O')
        if (num2 == 1):
            lblRes3.configure(text='\n  O\t\n\t\t\t')
        elif (num2 == 2):
            lblRes3.configure(text='    O\n\nO')
        elif (num2 == 3):
            lblRes3.configure(text='    O\n  O\t\nO')
        elif (num2 == 4):
            lblRes3.configure(text='O   O\n\nO   O')
        elif (num2 == 5):
            lblRes3.configure(text='O   O\n  O\nO   O')
        elif (num2 == 6):
            lblRes3.configure(text='O   O\nO   O\nO   O')
    print('SN-'+str(selectNumber)+'\nbet - '+str(betamount))
    num=num1+num2
    if(num==selectNumber):
        p.total+=betamount*10
        mb.showinfo(title='Congratulation',message='U win '+str(betamount*10))
    else:
        mb.showinfo(title='Sad',message='U lost !!')
    reset2()

btnstartG2.configure(command=startGame2)
btnBetG2.configure(command=bet2)
#btnN1.configure(command=lambda:selectNum2(0))
btnN2.configure(command=lambda:selectNum2(0))
btnN3.configure(command=lambda:selectNum2(1))
btnN4.configure(command=lambda:selectNum2(2))
btnN5.configure(command=lambda:selectNum2(3))
btnN6.configure(command=lambda:selectNum2(4))
btnN7.configure(command=lambda:selectNum2(5))
btnN8.configure(command=lambda:selectNum2(6))
btnN9.configure(command=lambda:selectNum2(7))
btnN10.configure(command=lambda:selectNum2(8))
btnN11.configure(command=lambda:selectNum2(9))
btnN12.configure(command=lambda:selectNum2(10))

app.mainloop()