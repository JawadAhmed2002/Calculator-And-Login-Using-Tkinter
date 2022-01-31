from tkinter import *

root = Tk()
root.geometry('312x324')
root.title('CALCULATOR')
root.resizable(0,0)

action=''
inputText=StringVar()

makeFrame=Frame(root, width = 312, height = 50, bd = 0, highlightbackground = "black", highlightcolor = "black", highlightthickness = 1)
makeFrame.pack(side = TOP)

fieldEntry=Entry(makeFrame, font = ('arial', 18, 'bold'), textvariable = inputText, width = 50, bg = "white", bd = 0, justify = RIGHT)
fieldEntry.grid(row = 0, column = 0)
fieldEntry.pack(ipady = 10)

frameBg=Frame(root, width= 312, height= 372.5, bg='grey')
frameBg.pack()

clearOperation = Button(frameBg, text = "Clear", fg = "red", width = 32, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clearButton()).grid(row = 0, column = 0, columnspan = 3, padx = 1, pady = 1)

divideOperation = Button(frameBg, text = "/", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton("/")).grid(row = 0, column = 3, padx = 1, pady = 1)

multiplyOperation = Button(frameBg, text = "*", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton("*")).grid(row = 1, column = 3, padx = 1, pady = 1)

minusOperation = Button(frameBg, text = "-", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton("-")).grid(row = 2, column = 3, padx = 1, pady = 1)

plusOperation = Button(frameBg, text = "+", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton("+")).grid(row = 3, column = 3, padx = 1, pady = 1)

equalsOperation = Button(frameBg, text = "=", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: equalButton()).grid(row = 4, column = 3, padx = 1, pady = 1)

Point = Button(frameBg, text = ".", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(".")).grid(row = 4, column = 2, padx = 1, pady = 1)

Zero = Button(frameBg, text = "0", fg = "black", width = 21, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(0)).grid(row = 4, column = 0, columnspan = 2, padx = 1, pady = 1)

One = Button(frameBg, text = "1", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(1)).grid(row = 3, column = 0, padx = 1, pady = 1)

Two = Button(frameBg, text = "2", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(2)).grid(row = 3, column = 1, padx = 1, pady = 1)

Three = Button(frameBg, text = "3", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(3)).grid(row = 3, column = 2, padx = 1, pady = 1)

Four = Button(frameBg, text = "4", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(4)).grid(row = 2, column = 0, padx = 1, pady = 1)

Five = Button(frameBg, text = "5", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(5)).grid(row = 2, column = 1, padx = 1, pady = 1)

Six = Button(frameBg, text = "6", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(6)).grid(row = 2, column = 2, padx = 1, pady = 1)

Seven = Button(frameBg, text = "7", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(7)).grid(row = 1, column = 0, padx = 1, pady = 1)

Eight = Button(frameBg, text = "8", fg = "black", width = 10, height = 3, bd = 0, bg = "white",
                cursor = "hand2", command = lambda: clickButton(8)).grid(row = 1, column = 1, padx = 1, pady = 1)

Nine = Button(frameBg, text = "9", fg = "black", width = 10, height = 3, bd = 0, bg = "white", 
                cursor = "hand2", command = lambda: clickButton(9)).grid(row = 1, column = 2, padx = 1, pady = 1)


def clearButton():
    global action
    action=''
    inputText.set('')

def equalButton():
    global action

    outputText=str(eval(action))
    inputText.set(outputText)
    action=''

def clickButton(element):
    global action
    action=action + str(element)
    inputText.set(action)

root.mainloop()

#________________________________________________________________________________________________________________________________#
#Completed By Jawad Ahmed