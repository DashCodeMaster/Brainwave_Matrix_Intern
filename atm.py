from tkinter import *
import tkinter.font as font
import random

win = Tk()
win.title('ATM')
win.geometry('460x390')
tim40 = font.Font(family='Times', size=40, weight='bold', slant='italic', underline=1)
cour20 = font.Font(family='Courier', size=20, weight='bold')
cour15 = font.Font(family='Courier', size=15, weight='bold')
glob_count = 0

def display_func():
    question_func.question_win.withdraw()
    display_win = Toplevel(win)
    display_win.geometry('460x390')
    message = Message(display_win, text='\n\nYour transaction has been successful\n\nThank you for using our',
                      font=cour20, fg='blue')
    message.pack()
    text = Label(display_win, text='ATM', font=tim40, fg='red')
    text.pack()
    exit_button = Button(display_win, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)

def question_func():
    global glob_count
    glob_count += 1
    withdrawal_func.withdrawal_win.withdraw()
    question_func.question_win = Toplevel(win)
    question_func.question_win.geometry('460x390')
    bf = Frame(question_func.question_win)
    bf.pack(side=BOTTOM)
    msg_box = Message(question_func.question_win,
                      text='\nYour transaction has been successful\n\nPlease collect your money\n\nYou can remove your'
                           ' card\n\nDo you want to check your balance?',font=cour20, fg='blue')
    msg_box.pack()
    yes_btn = Button(bf, text='YES', font=cour15, fg='green', command=balance_func)
    yes_btn.pack(side=LEFT, pady=10)
    no_btn = Button(bf, text=' NO ', font=cour15, fg='red', command=display_func)
    no_btn.pack(pady=10, padx=10)


def withdrawal_func():
    option_func.option_win.withdraw()
    withdrawal_func.withdrawal_win = Toplevel(win)
    withdrawal_func.withdrawal_win.geometry('460x390')
    enter_lbl = Label(withdrawal_func.withdrawal_win, text='\nPlease enter amount\n', font=cour20, fg='red')
    enter_lbl.pack()
    money_entry = Entry(withdrawal_func.withdrawal_win, font=cour15, justify='center')
    money_entry.pack()
    bf = Frame(withdrawal_func.withdrawal_win)
    bf.pack(side=BOTTOM)
    bf4 = Frame(withdrawal_func.withdrawal_win)
    bf4.pack(side=BOTTOM)
    bf3 = Frame(withdrawal_func.withdrawal_win)
    bf3.pack(side=BOTTOM)
    bf3 = Frame(withdrawal_func.withdrawal_win)
    bf3.pack(side=BOTTOM)
    bf2 = Frame(withdrawal_func.withdrawal_win)
    bf2.pack(side=BOTTOM)
    bf1 = Frame(withdrawal_func.withdrawal_win)
    bf1.pack(side=BOTTOM)
    b1 = Button(bf1, text='1', font=cour15, command=lambda: money_entry.insert('end', '1'))
    b1.pack(side=LEFT, pady=10)
    b2 = Button(bf1, text='2', font=cour15, command=lambda: money_entry.insert('end', '2'))
    b2.pack(side=LEFT, padx=10)
    b3 = Button(bf1, text='3', font=cour15, command=lambda: money_entry.insert('end', '3'))
    b3.pack(side=LEFT)
    b4 = Button(bf2, text='4', font=cour15, command=lambda: money_entry.insert('end', '4'))
    b4.pack(side=LEFT)
    b5 = Button(bf2, text='5', font=cour15, command=lambda: money_entry.insert('end', '5'))
    b5.pack(side=LEFT, padx=10)
    b6 = Button(bf2, text='6', font=cour15, command=lambda: money_entry.insert('end', '6'))
    b6.pack(side=LEFT)
    b7 = Button(bf3, text='7', font=cour15, command=lambda: money_entry.insert('end', '7'))
    b7.pack(side=LEFT, pady=10)
    b8 = Button(bf3, text='8', font=cour15, command=lambda: money_entry.insert('end', '8'))
    b8.pack(side=LEFT, padx=10)
    b9 = Button(bf3, text='9', font=cour15, command=lambda: money_entry.insert('end', '9'))
    b9.pack(side=LEFT)
    btn = Button(bf4, text=' ', font=cour15)
    btn.pack(side=LEFT)
    b0 = Button(bf4, text='0', font=cour15, command=lambda: money_entry.insert('end', '0'))
    b0.pack(side=LEFT, padx=10)
    btn_ = Button(bf4, text=' ', font=cour15)
    btn_.pack(side=LEFT)
    enter_btn = Button(bf, text='ENTER', font=cour15, fg='green', command=question_func)
    enter_btn.pack(side=LEFT, pady=10)
    clear_btn = Button(bf, text='CLEAR', font=cour15, fg='orange', command=lambda: money_entry.delete(1))
    clear_btn.pack(side=LEFT, padx=10)

def balance_func():
    global glob_count
    if glob_count == 1:
        question_func.question_win.withdraw()
    option_func.option_win.withdraw()
    balance_win = Toplevel(win)
    balance_win.geometry('460x390')
    # balance_win.grab_set()
    balance = random.randrange(1000, 1000000)
    message = Message(balance_win, text='\nYour transaction is successful\n\nAvailable Balance: ' + str(
        balance) + '\n\nThank you for using our', font=cour20, fg='blue')
    message.pack()
    text = Label(balance_win, text='ATM', font=tim40, fg='red')
    text.pack()
    exit_button = Button(balance_win, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)

def message_func():
    change_pin_func.change_pin_win.withdraw()
    win2 = Toplevel(win)
    win2.geometry('460x390')
    message = Message(win2,text='\nYour transaction is successful\n\nYour PIN has been successfully changed\n\nThank you'
                                ' for using our',font=cour20, fg='blue')
    message.pack()
    text = Label(win2, text='ATM', font=tim40, fg='red')
    text.pack()
    exit_button = Button(win2, text='EXIT', font=cour15, fg='red', command=lambda: win.destroy())
    exit_button.pack(side=BOTTOM, pady=10)

def change_pin_func():
    option_func.option_win.withdraw()
    change_pin_func.change_pin_win = Toplevel(win)
    change_pin_func.change_pin_win.geometry('460x420')
    pin_lbl = Label(change_pin_func.change_pin_win, text='\nEnter new-PIN', font=cour15, fg='red')
    pin_lbl.pack()
    pin_entry = Entry(change_pin_func.change_pin_win, font=cour15, justify='center', show='*')
    pin_entry.pack()
    re_entry_lbl = Label(change_pin_func.change_pin_win, text='\nRe-enter new-PIN', font=cour15, fg='red')
    re_entry_lbl.pack()
    re_entry = Entry(change_pin_func.change_pin_win, font=cour15, justify='center', show='*')
    re_entry.pack()
    bf = Frame(change_pin_func.change_pin_win)
    bf.pack(side=BOTTOM)
    bf4 = Frame(change_pin_func.change_pin_win)
    bf4.pack(side=BOTTOM)
    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)
    bf3 = Frame(change_pin_func.change_pin_win)
    bf3.pack(side=BOTTOM)
    bf2 = Frame(change_pin_func.change_pin_win)
    bf2.pack(side=BOTTOM)
    bf1 = Frame(change_pin_func.change_pin_win)
    bf1.pack(side=BOTTOM)
    b1 = Button(bf1, text='1', font=cour15, command=lambda: [pin_entry.insert('end', '1'), re_entry.insert('end', '1')])
    b1.pack(side=LEFT, pady=10)
    b2 = Button(bf1, text='2', font=cour15, command=lambda: [pin_entry.insert('end', '2'), re_entry.insert('end', '2')])
    b2.pack(side=LEFT, padx=10)
    b3 = Button(bf1, text='3', font=cour15, command=lambda: [pin_entry.insert('end', '3'), re_entry.insert('end', '3')])
    b3.pack(side=LEFT)
    b4 = Button(bf2, text='4', font=cour15, command=lambda: [pin_entry.insert('end', '4'), re_entry.insert('end', '4')])
    b4.pack(side=LEFT)
    b5 = Button(bf2, text='5', font=cour15, command=lambda: [pin_entry.insert('end', '5'), re_entry.insert('end', '5')])
    b5.pack(side=LEFT, padx=10)
    b6 = Button(bf2, text='6', font=cour15, command=lambda: [pin_entry.insert('end', '6'), re_entry.insert('end', '6')])
    b6.pack(side=LEFT)
    b7 = Button(bf3, text='7', font=cour15, command=lambda: [pin_entry.insert('end', '7'), re_entry.insert('end', '7')])
    b7.pack(side=LEFT, pady=10)
    b8 = Button(bf3, text='8', font=cour15, command=lambda: [pin_entry.insert('end', '8'), re_entry.insert('end', '8')])
    b8.pack(side=LEFT, padx=10)
    b9 = Button(bf3, text='9', font=cour15, command=lambda: [pin_entry.insert('end', '9'), re_entry.insert('end', '9')])
    b9.pack(side=LEFT)
    btn = Button(bf4, text=' ', font=cour15)
    btn.pack(side=LEFT)
    b0 = Button(bf4, text='0', font=cour15, command=lambda: [pin_entry.insert('end', '0'), re_entry.insert('end', '0')])
    b0.pack(side=LEFT, padx=10)
    btn_ = Button(bf4, text=' ', font=cour15)
    btn_.pack(side=LEFT)
    enter_btn = Button(bf, text='ENTER', font=cour15, fg='green', command=message_func)
    enter_btn.pack(side=LEFT, pady=10)
    clear_btn = Button(bf, text='CLEAR', font=cour15, fg='orange',
                       command=lambda: [pin_entry.delete(0), re_entry.delete(0)])
    clear_btn.pack(side=LEFT, padx=10)

def option_func():
    enter_pin.new_win.withdraw()
    option_func.option_win = Toplevel(win)
    option_func.option_win.geometry('460x390')
    text_title = Label(option_func.option_win, text='\nATM', font=tim40)
    text_title.pack()
    rf = Frame(option_func.option_win)  # right frame
    rf.pack(side=RIGHT)
    lf = Frame(option_func.option_win)  # left frame
    lf.pack(side=LEFT)
    withdrawal_btn = Button(rf, text=' WITHDRAWAL ', font=cour15, fg='blue', command=withdrawal_func)
    withdrawal_btn.pack(padx=40, pady=10)
    balance_btn = Button(rf, text='BALANCE INQ', font=cour15, command=balance_func)
    balance_btn.pack(padx=40, pady=10)
    change_pin_btn = Button(lf, text='CHANGE PIN', font=cour15, command=change_pin_func)
    change_pin_btn.pack(padx=40, pady=10)
    exit_btn = Button(lf, text='   EXIT   ', font=cour15, fg='red',
                      command=lambda: [option_func.option_win.destroy(), enter_pin.new_win.deiconify()])
    exit_btn.pack(padx=40, pady=10)

def enter_pin():
    win.withdraw()
    enter_pin.new_win = Toplevel(win)
    enter_pin.new_win.geometry('460x390')

    def setInputText(text):
        entry_box.insert('end', text)

    def text_delete():
        entry_box.delete(0)

    lbl = Label(enter_pin.new_win, text='Enter your PIN', font=cour20, fg='red')
    lbl.pack(pady=20)
    entry_box = Entry(enter_pin.new_win, font=cour15, show='*', justify='center')
    entry_box.pack()
    bf = Frame(enter_pin.new_win)
    bf.pack(side=BOTTOM)
    bf0 = Frame(enter_pin.new_win)
    bf0.pack(side=BOTTOM)
    bf1 = Frame(enter_pin.new_win)
    bf1.pack(side=BOTTOM)
    bf2 = Frame(enter_pin.new_win)
    bf2.pack(side=BOTTOM)
    bf3 = Frame(enter_pin.new_win)
    bf3.pack(side=BOTTOM)
    bf4 = Frame(enter_pin.new_win)
    bf4.pack(side=BOTTOM)
    rf = Frame(enter_pin.new_win)
    rf.pack(side=RIGHT)
    btn1 = Button(bf4, text='1', font=cour15, command=lambda: setInputText('1'))
    btn1.pack(side=LEFT, pady=10)
    btn2 = Button(bf4, text='2', font=cour15, command=lambda: setInputText('2'))
    btn2.pack(side=LEFT, padx=10)
    btn3 = Button(bf4, text='3', font=cour15, command=lambda: setInputText('3'))
    btn3.pack(side=LEFT)
    btn4 = Button(bf3, text='4', font=cour15, command=lambda: setInputText('4'))
    btn4.pack(side=LEFT)
    btn5 = Button(bf3, text='5', font=cour15, command=lambda: setInputText('5'))
    btn5.pack(side=LEFT, padx=10)
    btn6 = Button(bf3, text='6', font=cour15, command=lambda: setInputText('6'))
    btn6.pack(side=LEFT)
    btn7 = Button(bf2, text='7', font=cour15, command=lambda: setInputText('7'))
    btn7.pack(side=LEFT, pady=10)
    btn8 = Button(bf2, text='8', font=cour15, command=lambda: setInputText('8'))
    btn8.pack(side=LEFT, padx=10)
    btn9 = Button(bf2, text='9', font=cour15, command=lambda: setInputText('9'))
    btn9.pack(side=LEFT)
    btn = Button(bf1, text=' ', font=cour15)
    btn.pack(side=LEFT)
    btn0 = Button(bf1, text='0', font=cour15, command=lambda: setInputText('0'))
    btn0.pack(side=LEFT, padx=10)
    btn_ = Button(bf1, text=' ', font=cour15)
    btn_.pack(side=LEFT)
    enter_btn = Button(bf0, text='ENTER', font=cour15, fg='green', command=option_func)
    enter_btn.pack(side=LEFT, pady=10, padx=10)
    exit_btn = Button(bf0, text='EXIT', font=cour15, fg='red', command=lambda: [enter_pin.new_win.destroy(),
                                                                                win.deiconify()])
    exit_btn.pack(side=RIGHT, padx=10)
    clear_btn = Button(bf0, text='CLEAR', font=cour15, fg='orange', command=text_delete)
    clear_btn.pack(side=LEFT)
    note = Label(bf, text='Note:Enter pin either from keyboard or keypad', fg='red')
    note.pack()


title_label = Label(win, text='ATM', font=tim40, fg='red')
title_label.pack(pady=10)
user_id = random.randrange(1000, 10000)
intro = Label(win, text='\nWelcome User ' + str(user_id), font=cour20, fg='green')
intro.pack()
option_label = Label(win, text='\nSelect your account type', font=cour15, fg='grey')
option_label.pack()

bottom_frame = Frame(win)
bottom_frame.pack(side=BOTTOM)
right_frame = Frame(win)
right_frame.pack(side=RIGHT)

note = Label(bottom_frame, text='NOTE:Use only EXIT button to exit', font=cour15, fg='red')
note.pack(pady=10)
saving = Button(right_frame, text='Savings', font=cour15, bg='sky blue', fg='red', command=enter_pin)
saving.pack(padx=30, pady=10)
current = Button(right_frame, text="Current", font=cour15, bg='sky blue', fg='red', command=enter_pin)
current.pack(padx=30, pady=10)

win.mainloop()
