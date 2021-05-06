from tkinter import *
import math 

# 25 min work, 
# 5 min Break, 
# 25 min work, 
# 5 min break, 
# 25 min work, 
# 5 min break, 
# 25 min work, 
# 20 min break
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0 
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    canvas.itemconfig(timer_text, text="00:00")
    title_label.config(text="Timer")
    check_marks.config(text="")
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1

    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60
    
    if reps % 8 ==0:
        count_down(long_break_sec)
        title_label.config(text="Break", fg=RED)

    elif reps % 2 ==0:
        count_down(short_break_sec)
        title_label.config(text="Break", fg=PINK)
    else:
        count_down(work_sec)
        title_label.config(text="Work", fg=GREEN)





# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def count_down(count):
    
    count_min = math.floor(count / 60)
    count_sec = count % 60
    if count_sec <10:
        count_sec = f"{count_sec}"
    


    canvas.itemconfig(timer_text,text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        marks = ""
        work_session = math.floor(reps/2)
        for _ in range(work_session):
            marks += "J"
        check_marks.config(text=marks)
    


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Time Mangement")
window.config(padx=100, pady=50, bg=YELLOW)


#Label
title_label = Label(text="Timer", fg=PINK, bg=YELLOW, font=(FONT_NAME, 50))
title_label.grid(column=1, row=0)


canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
apple_img = PhotoImage(file="image_file.gif")
canvas.create_image(100, 112, image=apple_img)
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


#Start Button
start_button = Button(text="Start", highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)

#Reset Button
reset_button = Button(text="Reset", highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)


check_marks = Label(fg=GREEN, bg=YELLOW)
check_marks.grid(column=1, row=3)



window.mainloop()
