# simple calculator
import tkinter as tk

calculation = ""

def addToCalaculator(symbol):
    global calculation
    
    # Prevent multiple operators in a row
    if calculation and symbol in "+-*/" and calculation[-1] in "+-*/":
        return

    calculation += str(symbol)
    textResult.delete(1.0, "end")
    textResult.insert(1.0, calculation)

def evaluateCalculation(symbol):
    global calculation
    
    try:
        result = str(eval(calculation)) 
        clearField() 
        calculation = result  
        textResult.insert(1.0, calculation)  
    except:
        clearField()
        textResult.insert(1.0, "Error")

def clearField():
    global calculation
    calculation = ""
    textResult.delete(1.0, "end")

def disableTextInput(event):
    return "break"

root = tk.Tk()

root.geometry("265x370")
root.title("Simple Calculator")
textResult = tk.Text(root, height=2, width=15, font=("Arial", 24))
textResult.grid(columnspan=5)

textResult.bind("<Key>", disableTextInput)

btn1 = tk.Button(root, text="1", command=lambda: addToCalaculator("1"), height=2, width=5, font=("Times New Roman", 14))
btn1.grid(row=4, column=0)

btn2 = tk.Button(root, text="2", command=lambda: addToCalaculator("2"), height=2, width=5, font=("Times New Roman", 14))
btn2.grid(row=4, column=1)

btn3 = tk.Button(root, text="3", command=lambda: addToCalaculator("3"), height=2, width=5, font=("Times New Roman", 14))
btn3.grid(row=4, column=2)

btn4 = tk.Button(root, text="4", command=lambda: addToCalaculator("4"), height=2, width=5, font=("Times New Roman", 14))
btn4.grid(row=3, column=0)

btn5 = tk.Button(root, text="5", command=lambda: addToCalaculator("5"), height=2, width=5, font=("Times New Roman", 14))
btn5.grid(row=3, column=1)

btn6 = tk.Button(root, text="6", command=lambda: addToCalaculator("6"), height=2, width=5, font=("Times New Roman", 14))
btn6.grid(row=3, column=2)

btn7 = tk.Button(root, text="7", command=lambda: addToCalaculator("7"), height=2, width=5, font=("Times New Roman", 14))
btn7.grid(row=2, column=0)

btn8 = tk.Button(root, text="8", command=lambda: addToCalaculator("8"), height=2, width=5, font=("Times New Roman", 14))
btn8.grid(row=2, column=1)

btn9 = tk.Button(root, text="9", command=lambda: addToCalaculator("9"), height=2, width=5, font=("Times New Roman", 14))
btn9.grid(row=2, column=2)

btn0 = tk.Button(root, text="0", command=lambda: addToCalaculator("0"), height=2, width=5, font=("Times New Roman", 14))
btn0.grid(row=5, column=1)

btnAdd = tk.Button(root, text="+", command=lambda: addToCalaculator("+"), height=2, width=5, font=("Times New Roman", 14))  
btnAdd.grid(row=2, column=3)

btnSub = tk.Button(root, text="-", command=lambda: addToCalaculator("-"), height=2, width=5, font=("Times New Roman", 14))
btnSub.grid(row=3, column=3)

btnMul = tk.Button(root, text="*", command=lambda: addToCalaculator("*"), height=2, width=5, font=("Times New Roman", 14))
btnMul.grid(row=4, column=3)

btnDiv = tk.Button(root, text="/", command=lambda: addToCalaculator("/"), height=2, width=5, font=("Times New Roman", 14))
btnDiv.grid(row=5, column=3)

btnRightBracket = tk.Button(root, text=")", command=lambda: addToCalaculator(")"), height=2, width=5, font=("Times New Roman", 14))
btnRightBracket.grid(row=5, column=2)

btnLeftBracket = tk.Button(root, text="(", command=lambda: addToCalaculator("("), height=2, width=5, font=("Times New Roman", 14))
btnLeftBracket.grid(row=5, column=0)

btnEqual = tk.Button(root, text="=", command=lambda: evaluateCalculation("="), height=2, width=25, font=("Times New Roman", 14))
btnEqual.grid(row=6, columnspan=4)

btnClear = tk.Button(root, text="C", command=lambda: clearField(), height=2, width=5, font=("Times New Roman", 14))
btnClear.grid(row=6, column=0)

root.mainloop()
