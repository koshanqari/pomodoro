from tkinter import *
import math
import time 
import tkinter.messagebox as tmb
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
# RED = "#e7305b"
RED = 'red'
GREEN = "green"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
BORDER_COLOR = "white"

# ---------------------------- TIMER RESET ------------------------------- # 
def stop_fxn():
    ans = tmb.askyesno(title="EXIT", message="Oooo Padna wadna nae hay kya ? \n Baday hokay reda chalana hay ?")
    print(ans)
    if ans == True:
        reset_rep()
        root.after_cancel(rep)
        root.destroy()

def auto_stop_fxn():
        reset_rep()

# ---------------------------- TIMER MECHANISM ------------------------------- #



#rep mechanism------------------------------
rep = 1
def reset_rep():
    global rep
    rep = 1
    print("rep resetted")
    rep_upgrade_fxns(rep)
def rep_upgrade():
    global rep
    rep +=1
    print(f"rep upgraded to: {rep}" )
    rep_upgrade_fxns(rep)
#--------------------------------------------


#pop_up mechanism------------------------
def popup(rep):
    if rep%2 != 0:
        if rep !=1:
            tmb.showinfo(title="POMODORO", message="Break session Completed")
    else:
        tmb.showinfo(title="POMODORO", message="Work session Completed")

#label mechanism --------------------------
def rep_upgrade_fxns(rep):
    '''takes rep and dicides accordingtly which label to keep'''

    if rep == 1 or rep == 3 or rep == 5 or rep == 7:
        canvas.itemconfigure(canvas_text_up, text= f"WORK", fill = RED)
        checkmark(rep)
        canvas.itemconfigure(canvas_text, text= f"25 min",)
        popup(rep)
    elif rep == 8:
        canvas.itemconfigure(canvas_text_up, text= f"TAKE REST", fill = GREEN)
        checkmark(rep)
        canvas.itemconfigure(canvas_text, text= f"20 min",)
        popup(rep)
    else: 
        canvas.itemconfigure(canvas_text_up, text= f"BREAK", fill= GREEN)
        checkmark(rep)
        canvas.itemconfigure(canvas_text, text= f"5 min",)
        popup(rep)
#------------------------------------------


def start_timmer():
    global rep





    if rep> 8:
        reset_rep()

    elif rep == 1 or rep == 3 or rep == 5 or rep == 7:
        if rep == 1:
            rep_upgrade_fxns(rep)
        time = WORK_MIN*60
        count_down(time)
        root.after(1000*time, rep_upgrade)

    elif rep == 8:
        time = LONG_BREAK_MIN*60
        count_down(time)
        root.after(1000*time, auto_stop_fxn)

    
    else:
        time = SHORT_BREAK_MIN*60
        count_down(time)
        root.after(1000*time, rep_upgrade)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 
def count_down(num):
    c_min = math.floor(num /60)
    c_sec = num%60
    if c_sec < 10:
        c_sec = f"0{c_sec}"


    if num>=0:
        root.after(1000, count_down, num-1) #after 1000ms, pass n-1 parameter to count_down
        if num!=0:
            canvas.itemconfigure(canvas_text, text= f"{c_min}:{c_sec}")        
    











# ---------------------------- UI SETUP ------------------------------- #
root = Tk()
# root.geometry("500x500")
root.title("K.Qari's Pomodoro")
root.wm_iconbitmap("Graphicloads-Food-Drink-Tomato.ico")
root.config(background="white")
root.config(padx=20, pady=50)


#Frame 
# _f = Frame(root, bg= BORDER_COLOR, borderwidth=4)
# _f.grid(row=2, column=0, padx=30)


#setting up canvas
canvas_f = Frame(root, bg= BORDER_COLOR, borderwidth=4)
canvas = Canvas(canvas_f, width= 270, height= 300)
canvas.config(background="white", highlightbackground="white")
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(130, 170, image = tomato_img)

canvas_text = canvas.create_text(130, 190, text="25 min", fill="white", font=(FONT_NAME, 32, "bold"))
canvas_text_up = canvas.create_text(130, 30, text="WORK", fill=GREEN, font=(FONT_NAME, 32, "bold"))
canvas.pack()
canvas_f.grid(column=1, row=1)



#Setting up START
start_f = Frame(root, bg= BORDER_COLOR, borderwidth=4)
start = Button(start_f, text="START", bg="white", borderwidth=0, font=(FONT_NAME, 16, "bold"), foreground=GREEN, command=start_timmer)
start.pack()
start_f.grid(row=2, column=0, padx=30)

#setting up STOP 
stop_f = Frame(root, bg= BORDER_COLOR, borderwidth=4)
stop = Button(stop_f, text="STOP", bg="white", borderwidth=0 , font=(FONT_NAME, 16, "bold"), foreground=RED, command=stop_fxn)
stop.pack()
stop_f.grid(row=2, column=2, padx=30 ,pady=30)

#setting up checkmark

def checkmark(rep):
    '''resets checkmark, according to the rep'''
    if rep == 1:
        label.config(text="Work for 25 min \n With 5 min break \n Repeat the session for 2 hours", foreground=GREEN)

    elif rep%2 == 0:
        label_v = ""
        for i in range(int(rep/2)):
            label_v += "✔ "
            label.config(text= label_v, foreground=GREEN)
    else:
        label_v = ""
        for i in range(int((rep+1)/2)):
            label_v += "✔ "
            label.config(text= label_v, foreground=RED)
    
    




check_f = Frame(root, bg= BORDER_COLOR, borderwidth=4)
label = Label(check_f, text="Work for 25 min \n With 5 min break \n Repeat the session for 2 hours",font=(FONT_NAME, 11, "bold"), bg="white", foreground=GREEN)
label.pack()
check_f.grid(row=2, column=1, padx=30)



root.mainloop()