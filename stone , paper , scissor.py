from tkinter import *
from tkinter import messagebox as msg
import random
#main
app=Tk()
app.title("Stone | Paper | Scissor")
try:
    logo=PhotoImage(file="C:\\Program Files (x86)\\Arul Games\\pylogo.png")
    app.iconphoto(False,logo)
except:pass


#function
respect=None
global times
times=0
def inputgender(gen):
    global respect
    respect=gen
    
def submit():


    if name.get()=="" or respect==None :
        msg.showerror("Arul Games","Must fill this : \n\n1.Fill your name\n2.Select your gender\n3.Enter how many life you want (given in number)")
    
    else:
        
        getplay=playtime.get()
        global life
        life=int(getplay)
        global resetlife
        resetlife=life
        aname=name.get()
        global playername
        playername=str(aname)    
        
        msg.showinfo("Arul Games",f"\tArul Games Present\n\nHi {respect} {playername}\n\nThis is Stone , Paper and Scissor game you know that\n\nRules : \n\t1.You have {life} chance to finish this game\n\n\tAll the best")



        global currentuser
        global currentcom
        global you
        global result
        global computer

        app["bg"]="pink"
       
        stone=Button(app,text="Stone",padx=40,pady=50,font=("lemon",30),fg="gray30",activebackground="gray30",activeforeground="white",command=lambda:algo("s"),state="disable")
        papper=Button(app,text="Paper",padx=40,pady=50,font=("lemon",30),fg="deep sky blue",activebackground="deep sky blue",activeforeground="white",command=lambda:algo("p"),state="disable")
        sis=Button(app,text="Scissor",padx=28,pady=50,font=("lemon",30),fg="red",activebackground="red",activeforeground="white",command=lambda:algo("sis"),state="disable")
        you=Label(app,text="You",font=("russo one",20),bg="yellow",width=14)
        result=Label(app,text="Equal",font=("russo one",20),bg="yellow",width=15)
        computer=Label(app,text="Computer",font=("russo one",20),bg="yellow",width=15)
        currentuser=Label(app,text="You = None",bg="orange",font=("russo one",20),width=14)
        currentcom=Label(app,text="Com = None",bg="orange",font=("russo one",20),width=15)

        global currenresult
        currenresult=Label(app,text="Current Result",font=("russo one",20),bg="yellow",width=15)

        #packing
        stone.grid(row=8,column=0)
        papper.grid(row=8,column=1)
        sis.grid(row=8,column=2)
        space1.grid(row=13,column=0)
       

        space3.grid(row=11,column=0)
        you.grid(row=12,column=0)
        result.grid(row=12,column=1)
        computer.grid(row=12,column=2)
        

        if respect=="Mr":
            gen="Male"
        elif respect=="Mrs":
            gen="Female"
        username=f"Name : {name.get()}   ||   Gender : {gen}"

        prinname.destroy()
        name.destroy()
        sub.destroy()
        gender.destroy()
        prinmale.destroy()
        prinfemale.destroy()
        howmanytimeslabel.destroy()
        playtime.destroy()
        

        global userscore
        global comscore
        global space2
        demo=f"Life Left = {life}"
        space2=Label(app,width=46,text=demo,font=("russo one",20),bg="green2",fg="white")
        userscore=Label(app,text="User Score = 0",font=("russo one",20),width=14,bg="grey")
        comscore=Label(app,text="Com Score = 0",font=("russo one",20),width=15,bg="grey")
        

        stone.config(state="normal")
        papper.config(state="normal")
        sis.config(state="normal")
        printusername=Label(app,text=username,font=("sigmar one",20),width=37,pady=5,fg="blue",bg="cyan")
        space4=Label(app,height=0,bg="pink")
        space5=Label(app,bg="pink")
        
        #packing
        printusername.grid(row=0,column=0,columnspan=3)
        space4.grid(row=1,column=0)
        userscore.grid(row=4,column=0)
        comscore.grid(row=4,column=2)
        space2.grid(row=2,column=0,columnspan=3)
        space5.grid(row=3,column=0)

#algorithm
usergamescore=0
comgamescore=0
precom="s"
resetclicked=0
def algo(user):
    
    global times    
    if life-times>5 and 9>life-times:
        space2.config(bg="yellow",fg="black")
    elif life-times<5:
        space2.config(bg="red",fg="white")
    times=times+1
    if times>life:
        if resetclicked==0:
            msg.showwarning("Arul Game","\tOut of life\n\n\tTo play again click reset button")
    else:
    
    
        global usergamescore
        global comgamescore

        if user=="s":
            you.config(text="You = Stone")
        elif user=="p":
            you.config(text="You = Paper")
        else:
            you.config(text="You = Scissor")

        com=random.choice(["s","p","sis"])

        if com=="s":
            computer.config(text="Com = Stone")
        elif com=="p":
            computer.config(text="Com = Paper")
        else:
            computer.config(text="Com = Scissor")
        
        #stone
        if com=="s" and user=="s":
            action="equal"
        elif com=="s" and user=="p":
            action="comded"
        elif com=="s" and user=="sis":
            action="userded"
        #paper
        elif com=="p" and user=="s":
            action="userded"
        elif com=="p" and user=="p":
            action="equal"
        elif com=="p" and user=="sis":
            action="comded"
        #Scissor
        elif com=="sis" and user=="s":
            action="comded"
        elif com=="sis" and user=="p":
            action="userded"
        elif com=="sis" and user=="sis":
            action="equal"


        if action=="userded":
            comgamescore=comgamescore+1
            you.config(bg="red",)
            result.config(text="You smash")
            computer.config(bg="green2")
        elif action=="comded":
            usergamescore=usergamescore+1
            you.config(bg="green2")
            result.config(text="Com smash")
            computer.config(bg="red")
        elif action=="equal":
            you.config(bg="yellow")
            result.config(text="Equal")
            computer.config(bg="yellow")
        
        global userscorestring
        global comgamestring
        userscorestring=f"User = {usergamescore}"
        comgamestring=f"Com = {comgamescore}"

        userscore.config(text=userscorestring)
        comscore.config(text=comgamestring)


        if usergamescore>comgamescore:
            userscore.config(bg="green2")
            comscore.config(bg="red")
        elif usergamescore<comgamescore:
            userscore.config(bg="red")
            comscore.config(bg="green2")
        elif usergamescore==comgamescore:
            comscore.config(bg="yellow")
            userscore.config(bg="yellow")


        timelabel=f"Life Left = {life-times}"
        space2.config(text=timelabel)

        
        def resetfunc():
            outputscreen.destroy()
            global life
            global resetlife
            global times
            times=0
            life=resetlife
            global usergamescore
            global comgamescore
            usergamescore=0
            comgamescore=0
            space2.config(text=f"Life Left = {life}")
            space2.config(bg="green2")
            userscore.config(text="User = 0")
            comscore.config(text="Com = 0")
            reset.destroy()
            global resetclicked
            resetclicked=1
            


        if times==life:
            if usergamescore>comgamescore:
                winner=f"{playername}"
                mess=f"Congratulation {respect} {playername} : )"
            elif usergamescore<comgamescore:
                winner="Computer"
                mess=f"Nice try better luck next time {respect} {playername} :("
            else:
                winner="Draw"
                mess=f"!Wow Both are get equal scores.Try again... :-"

            outputresult=f"\tGame Over | Out of life\n\n\t{playername} = {usergamescore}\n\tComputer = {comgamescore}\n\n\tWinner : {winner}\n\n\t{mess}\n\nTo play again click reset button ...\n\nDeveloped by M.Arul Selvam (Programmer)"
            reset=Button(app,text="Reset",font=("russo one",20),command=resetfunc,fg="blue",bg="black",activebackground="blue",activeforeground="black")

            
            if winner==playername:
                outputbg="green2"
                outputstring=f"Congratulation {respect} {playername} you got {usergamescore}"
            elif winner=="Computer":
                outputbg="red"
                outputstring=f"Better luck next time {respect} {playername} you got {usergamescore}"
            else:
                outputstring=f"! WOW both are get equal scores..."
                outputbg="yellow"

            outputscreen=Label(app,text=outputstring,bg=outputbg,font=("lemon",20),width=41)
            outputscreen.grid(row=14,column=0,columnspan=3)
            
            msg.showinfo("Arul Game",outputresult)

            reset.grid(row=4,column=1)



    


#functions and variables

aname=StringVar()

#body
prinname=Label(app,text="Enter your name : ",font=("roboto",20),width=15,pady=10,fg="dark orange1")
name=Entry(app,width=16,font=("roboto",20),textvariable=aname,fg="orange")
sub=Button(app,text="SUBMIT",pady=10,width=12,height=0,bg="cyan3",fg="white",command=submit,font=("russo one",20))
gender=Label(app,text="Select Gender : ",font=("roboto",20),width=15,fg="blue")
prinmale=Radiobutton(app,value=1,text="Male",command=lambda:inputgender("Mr"),font=("roboto",20),width=15,fg="dodger blue")
prinfemale=Radiobutton(app,value=2,text="Femal",command=lambda:inputgender("Mrs"),font=("roboto",20),width=15,fg="maroon1")
howmanytimeslabel=Label(app,text="How many life you want   (in numbers)",font=("roboto",20),width=30,pady=10,fg="magenta2")
play=IntVar()
playtime=Entry(app,width=16,font=("roboto",20),fg="purple1")



space1=Label(app,text="",bg="pink")
space3=Label(app,text="",bg="pink")

#packing
prinname.grid(row=0,column=0)
name.grid(row=0,column=1)
sub.grid(row=0,column=2)
gender.grid(row=3,column=0)
prinmale.grid(row=3,column=1)
prinfemale.grid(row=3,column=2)
howmanytimeslabel.grid(row=4,column=0,columnspan=2)
playtime.grid(row=4,column=2)



app.mainloop()
