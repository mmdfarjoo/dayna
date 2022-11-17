from tkinter import *
from tkinter import messagebox
import random
import subprocess
import time
import os
from datetime import datetime
import webbrowser





username = ['user']



def commands ():
    #hello command
    if (en_terminal.get() == "hello" or en_terminal.get()== 'hi') or (en_terminal.get() == 'ey' or en_terminal.get() == 'yao') :
        for i in username :
            name = i
        lb_show.configure(text=f"hi {name}",font=18)
    # end hello command



    # sest username command
    elif en_terminal.get() == 'call me' :
        
        def setusername ():
                username.pop()
                username.append(en_username.get())
                lb_show_username.configure(text='A new username has been set \n ---close window---',bg='green',fg='white',font=18)
        
        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(text="run call me",font=18,fg="white")
        top_set_user=Toplevel()
        top_set_user.title("set username ")
        Label(top_set_user,text="Enter new user name",font=18).pack()

        en_username = Entry(top_set_user)
        en_username.pack()

        btn_username = Button(top_set_user,text="ENTER",command=setusername,font=18)
        btn_username.pack()

        lb_show_username = Label(top_set_user,text='')
        lb_show_username.pack(side=BOTTOM)


        top_set_user.resizable(False,False)
        top_set_user.geometry("230x130")
        top_set_user.mainloop()
    #end set username 

    # roll command
    elif en_terminal.get() == 'roll' : 

        def roll ():
            
            number_list = []
            number_en = int(en_roll.get())
            for i in range(1,number_en):
                number_list.append(i)
            number_roll = random.choice(number_list)
            lb_show_roll.configure(text=f"number roll {number_roll}",bg='green',fg='white',font=18)
            

        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(text="run roll",font=18,fg="white")
        top_roll=Toplevel()
        top_roll.title("ROLL")
        Label(top_roll,text="Enter number for roll",font=18).pack()

        en_roll = Entry(top_roll)
        en_roll.pack()

        btn_roll = Button(top_roll,text="roll me",command=roll,font=18)
        btn_roll.pack()

        lb_show_roll= Label(top_roll,text='')
        lb_show_roll.pack(side=BOTTOM)


        top_roll.resizable(False,False)
        top_roll.geometry("200x130")
        top_roll.mainloop()
    # end def roll

    # start def speed test 
    elif en_terminal.get() == 'speed test':
        
        def run_st ():
            ret_text=subprocess.check_output("speedtest-cli",shell=True,universal_newlines=True)
            lb_show_st.configure(text=ret_text)


        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(text="run speed test",font=18,fg="white")
        top_st = Toplevel()
        top_st.title("speed test internet")


        Label(top_st,text="\nAfter clicking start\n wait a few moments  \n depends on your internet spee",font=18).pack(side=TOP)

        btn_st = Button(top_st,text="RUN",font=18,width=7,command=run_st)
        btn_st.pack()
        lb_f_st = LabelFrame(top_st,text='show test speed',font=18)
        lb_f_st.pack(fill='both',expand='yes')

        lb_show_st=Label(lb_f_st,text='',font=20)
        lb_show_st.pack()

        

        top_st.resizable(False,False)
        top_st.geometry("700x400")
        top_st.mainloop()
    # end code speed test

    # start code calculator
    elif en_terminal.get() == 'cal' or en_terminal.get() == 'calculator':
        
        def sum ():
            number1 = int(en_number1.get())
            number2 = int(en_number1.get())
            result = (number1 + number2)
            Lb_show_cal.configure(text=f"SUM : {number1} + {number2} = {result}",font=50)
        
        
        def minus ():
            number1 = int(en_number1.get())
            number2 = int(en_number1.get())
            result = (number1 - number2)
            Lb_show_cal.configure(text=f"MINUS : {number1} - {number2} = {result}",font=50)

        def Division ():
            number1 = int(en_number1.get())
            number2 = int(en_number1.get())
            result = (number1 / number2)
            Lb_show_cal.configure(text=f"DIVISION : {number1} / {number2} = {result}",font=50)

        def multi ():
            number1 = int(en_number1.get())
            number2 = int(en_number1.get())
            result = (number1 * number2)
            Lb_show_cal.configure(text=f"MULTI  : {number1} * {number2} = {result}",font=50)

        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(text="run calculator",font=18,fg="white")
        top_cal = Toplevel()
        top_cal.geometry('490x270')

        lb_f_cal_show=LabelFrame(top_cal,text="Display the result",font=18)
        lb_f_cal_show.pack(expand='yes',fill='both')

        Lb_show_cal = Label(lb_f_cal_show,text="")
        Lb_show_cal.pack(anchor=CENTER)

        lb_f_en= LabelFrame(top_cal,text='Numbers',font=18)
        lb_f_en.pack(expand='yes',fill= 'both')
        

        Label(lb_f_en,text="number 1 ->",font=18).pack(side=LEFT)
        en_number1 = Entry(lb_f_en)
        en_number1.pack(side=LEFT)


        Label(lb_f_en,text="<- number 2",font=18).pack(side=RIGHT)
        en_number2=Entry(lb_f_en)
        en_number2.pack(side=RIGHT)


        
        lb_f_bts = LabelFrame(top_cal,text="Buttons",font=18)
        lb_f_bts.pack(expand='yes',fill='both')
        
        btn_sum = Button(lb_f_bts,text="+",font=18,width=15,command=sum)
        btn_sum.pack(anchor=CENTER , side=BOTTOM)

        btn_minus = Button(lb_f_bts,text="-",font=18,width=15,command=minus)
        btn_minus.pack(side=LEFT)

        btn_Division = Button(lb_f_bts,text="/",font=18,width=15,command=Division)
        btn_Division.pack(side=RIGHT)

        btn_multi = Button(lb_f_bts,text="*",font=18,width=15,command=multi)
        btn_multi.pack(side=BOTTOM)    


        top_cal.resizable(False,False)
        top_cal = mainloop()
        
    #end code calculator


    #start code open app
    elif en_terminal.get() == "open app":

        def openapp ():
            
            appname = str(en_app.get())

            os.system(appname)
            lb_app.configure(text=f'open app {appname}',font=18)



        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(text="run open app",font=18,fg="white")
        top_app= Toplevel()
        top_app.geometry('200x100')

        lb_f_app = LabelFrame(top_app,text="ENTER APP NAME",font=18)
        lb_f_app.pack(expand="yes",fill='both')


        en_app = Entry(lb_f_app,width=10)
        en_app.pack(side=TOP)

        btn_app = Button(lb_f_app,text="open",command=openapp)
        btn_app.pack()

        lb_app = Label(lb_f_app,text="enter name app and wait",font=18)
        lb_app.pack(side=BOTTOM)


        top_app.resizable(False,False)
        top_app.mainloop()
    #end code open app
    

    #start code date and time 
    elif en_terminal.get() == 'date' or en_terminal.get() == 'time' or en_terminal.get() == 'datetime':

        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(font=18,fg="white")
        now = datetime.now()

        dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
            
        lb_show.configure(text=f'date and time is :  {dt_string}')
    #end code date and time

    #start google and mail  
    elif en_terminal.get() == 'search' or en_terminal.get() == 'mail':
        



        class MyApp:
            def __init__(self, parent):
                    self.myParent = parent
                    self.myContainer1 = LabelFrame(parent, text="Search by github.com/hushaboom ")
                    self.myContainer2 = Frame(parent)
                    self.myContainer1.grid()
                    self.myContainer2.grid()
                    

                    self.label1 = Message(self.myContainer1, text="")
                    
                    self.label1.pack()

                    self.entryVariable = StringVar()
                    self.textbox = Entry(self.myContainer1)
                    self.textbox.pack(side=TOP)
                    self.textbox.bind("<Return>",self.submitclick)
                    self.textbox.focus_set()

                    self.label2 = Label(self.myContainer1)
                    self.label2["text"] =""
                    self.label2.pack(side=BOTTOM)

                    self.label3 = Message(self.myContainer1, text="")
                    self.label3.pack()
                    

                    self.button1 = Button(self.myContainer2)
                    self.button1["text"]= "Go"
                    self.button1.pack(side=BOTTOM)
                    self.button1.bind("<Button-1>", self.submitclick)
                    textbox=self.textbox

                    self.button2 = Button(self.myContainer2)
                    self.button2["text"] = "Mail"
                    self.button2.pack(side=BOTTOM)
                    self.button2.bind("<Button-1>", self.getmail)

                    
            def submitclick(self, event):

                    browser_path = '/usr/bin/firefox %s'
                    textin = self.textbox.get()
                    webbrowser.get(browser_path).open("http://www.google.ca/search?q="+textin)
                    
                    self.myParent.destroy()
                    
            def getmail(self, event):
                    browser_path = '/usr/bin/firefox %s'
                    webbrowser.get(browser_path).open("https://gmail.google.com/inbox/")
                    self.myParent.destroy()


        en_terminal.configure(highlightcolor="darkgreen")
        lb_show.configure(text="run search",font=18,fg="white")
        
        top_sh = Toplevel()
        
        myapp = MyApp(top_sh)

        
        top_sh.title('Search')
        
        top_sh.resizable(False,False)                
        top_sh.mainloop()











# your code this 















    else:
        en_terminal.configure(highlightcolor="darkred")
        lb_show.configure(text="false command",font=18,fg="red")

        






win = Tk()
win.title('DAYNA')

#label frame 1

lf_1=LabelFrame(win,text='DAYNA assist v 0.01(beta)',font=18,bg='gray',fg='white')
lf_1.pack(expand='yes',fill='both')

en_terminal = Entry(lf_1,width=35,highlightbackground='gray',highlightcolor='darkgreen',highlightthickness=7)
en_terminal.pack(side=LEFT)

btn_select = Button(lf_1,text='Enter',command=commands,font=18,width=20,fg='white',bg='gray',highlightbackground='gray',highlightthickness=7)
btn_select.pack(side=RIGHT)

#label frame 1 end


lf_2=LabelFrame(win,text='SHOW COMMAND',font=18,bg='black',fg='white')
lf_2.pack(expand='yes',fill='both')

lb_show = Label(lf_2,text=" ------nothing------ ",font="bold,Times",fg='white',bg='black')
lb_show.pack(anchor=CENTER,expand=True)







win.resizable(False,False)
win.geometry("390x295")
win.mainloop()