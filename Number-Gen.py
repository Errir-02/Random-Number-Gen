from tkinter import *
#
master = Tk()
#
#
master.title("Random Number Gen")
master.config(bg='white')
master.geometry('300x300')
#
# Main
import random
def range10():
  num = random.randint(0,10)
  Label(text='Number: ' + str(num),
     fg="black", bg="white",
     font=("Calibri", 15),
     padx=12, pady=10
     ).grid(row=0,
           sticky="N")
def range100():
  num = random.randint(0,100)
  Label(text='Number: ' + str(num),
     fg="black", bg="white",
     font=("Calibri", 15),
     padx=12, pady=10
     ).grid(row=0,
           sticky="N")
def range1000():
  num = random.randint(0,1000)
  Label(text='Number: ' + str(num),
     fg="black", bg="white",
     font=("Calibri", 15),
     padx=12, pady=10
     ).grid(row=0,
           sticky="N")
##
Label(text="Choose number range",
     fg="grey", bg="white",
     font=("Calibri", 15)
     ).place(relx=0.13, rely=0.4)
#
button1 = Button(text="0-10",
      fg="blue", bg="grey",
      activeforeground="red", activebackground="black",
      bd=5,
      command=range10,
      width=4, height=2).place(relx=0.079,rely=0.5)
button2 = Button(text="0-100",
      fg="blue", bg="grey",
      activeforeground="red", activebackground="black",
      bd=5,
      command=range100,
      width=4, height=2).place(relx=0.379,rely=0.5)
button3 = Button(text="0-1000",
      fg="blue", bg="grey",
      activeforeground="red", activebackground="black",
      bd=5,
      command=range1000,
      width=4, height=2).place(relx=0.679,rely=0.5)
#
Label(text="OR:  Choose Range:",
     fg='black', bg='white',
     font=("Calibri", 12)
     ).place(relx=0.01, rely=0.7)
Label(text="0-",
     fg="black", bg="white",
     font=("Calibri", 15)).place(relx=0.1, rely=0.79)
# Choose range
inputtxt = Text(master,
           width=16, height=1.4,
           font=("Calibri", 15),
           fg="black")
inputtxt.place(relx=0.2,rely=0.79)

def printInput():
  inp = inputtxt.get(1.0, "end-1c")
  try:
    inp = int(inp)
    num = random.randint(0,inp)
    Label(text='Number: ' + str(num),
          fg="black", bg="white",
          font=("Calibri", 15),
          padx=12, pady=10
         ).grid(row=0,
                sticky="N")
  except:
    print("You may have entered a string, or float(decimal), Please enter a positive integer.")
  
b = Button(master,
      text="Get",
      bg="#e1dfd9", fg="black",
      width=5,
      bd = 3,
      command=printInput)
b.place(relx=0.6,rely=0.68)




master.mainloop()