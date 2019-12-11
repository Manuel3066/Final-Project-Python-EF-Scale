import tkinter
from tkinter import *
import datetime
from Components import file_write


def ef0():

    # Creates a new window with a window title of wind check
    m = tkinter.Tk(className="Wind Check")
    label0 = Label(m, text=str(datetime.datetime.now()), background = 'royalblue1') # Shows the current user time
    label0.grid(column=1, row=0)
    label1 = Label(m, text="You have entered a wind speed that fits within EF-0", background = 'royalblue1')# Returns to the user what their wind
    label1.grid(column=1, row=1)
    label2 = Label(m, text="This puts you in the blue zone you should expect little damage",background = 'royalblue1' )
    label2.grid(column=1, row=2)

    # Exit for the user to back out of the window and return to the main program
    exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(column=1, row=3)

    m.configure(background = 'royalblue1') # set the background to blue to match the windspeed
    m.mainloop()  # infinite loop that waits for the user to exit the window
    file_write.write_to_file(0)

def ef1():

    # Creates a new window with a window title of wind check
    m = tkinter.Tk(className="Wind Check")
    label0 = Label(m, text=str(datetime.datetime.now()), background='palegoldenrod') # Shows the current user time
    label0.grid(column=1, row=0)
    label1 = Label(m, text="You have entered a wind speed that fits within EF-1", background='palegoldenrod')# Returns to the user what their wind
    label1.grid(column=1, row=1)
    label2 = Label(m, text="This puts you in the light tan zone you should expect minor damage",background='palegoldenrod' )
    label2.grid(column=1, row=2)

    # Exit for the user to back out of the window and return to the main program
    exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(column=1, row=3)

    m.configure(background='palegoldenrod') # set the background to blue to match the windspeed
    m.mainloop()  # infinite loop that waits for the user to exit the window
    file_write.write_to_file(1)

def ef2():

    # Creates a new window with a window title of wind check
    m = tkinter.Tk(className="Wind Check")
    label0 = Label(m, text=str(datetime.datetime.now()), background='tan') # Shows the current user time
    label0.grid(column=1, row=0)
    label1 = Label(m, text="You have entered a wind speed that fits within EF-2", background='tan')# Returns to the user what their wind
    label1.grid(column=1, row=1)
    label2 = Label(m, text="This puts you in the tan zone you should expect roof damage, or for it to be gone",background='tan' )
    label2.grid(column=1, row=2)

    # Exit for the user to back out of the window and return to the main program
    exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(column=1, row=3)

    m.configure(background='tan') # set the background to blue to match the windspeed
    m.mainloop()  # infinite loop that waits for the user to exit the window
    file_write.write_to_file(2)

def ef3():

    # Creates a new window with a window title of wind check
    m = tkinter.Tk(className="Wind Check")
    label0 = Label(m, text=str(datetime.datetime.now()), background='brown') # Shows the current user time
    label0.grid(column=1, row=0)
    label1 = Label(m, text="You have entered a wind speed that fits within EF-3", background='brown')# Returns to the user what their wind
    label1.grid(column=1, row=1)
    label2 = Label(m, text="This puts you in the brown zone you should seek shelter as walls collapse in this zone",background='brown' )
    label2.grid(column=1, row=2)

    # Exit for the user to back out of the window and return to the main program
    exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(column=1, row=3)

    m.configure(background='brown') # set the background to blue to match the windspeed
    m.mainloop()  # infinite loop that waits for the user to exit the window
    file_write.write_to_file(3)


def ef4():

    # Creates a new window with a window title of wind check
    m = tkinter.Tk(className="Wind Check")
    label0 = Label(m, text=str(datetime.datetime.now()), background='orange') # Shows the current user time
    label0.grid(column=1, row=0)
    label1 = Label(m, text="You have entered a wind speed that fits within EF-4", background='orange')# Returns to the user what their wind
    label1.grid(column=1, row=1)
    label2 = Label(m, text="This puts you in the orange zone, a house can be blown down seek shelter",background='orange' )
    label2.grid(column=1, row=2)

    # Exit for the user to back out of the window and return to the main program
    exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(column=1, row=3)

    m.configure(background='orange') # set the background to blue to match the windspeed
    m.mainloop()  # infinite loop that waits for the user to exit the window
    file_write.write_to_file(4)

def ef5():

    # Creates a new window with a window title of wind check
    m = tkinter.Tk(className="Wind Check")
    label0 = Label(m, text=str(datetime.datetime.now()), background='red') # Shows the current user time
    label0.grid(column=1, row=0)
    label1 = Label(m, text="You have entered a wind speed that fits within EF-5", background='red')# Returns to the user what their wind
    label1.grid(column=1, row=1)
    label2 = Label(m, text="This puts you in the red zone you should seek shelter as houses can blown away",background='red' )
    label2.grid(column=1, row=2)

    # Exit for the user to back out of the window and return to the main program
    exit_button = tkinter.Button(m, text='Exit', width=15, command=m.destroy)
    exit_button.grid(column=1, row=3)

    m.configure(background='red') # set the background to blue to match the windspeed
    m.mainloop()  # infinite loop that waits for the user to exit the window
    file_write.write_to_file(5)




