from tkinter import *


class Error(Exception):
    """Base class for other exceptions"""
    pass


class EmptyInput(Error):
    pass


class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculator app @AH 2021")
        self.entry = Entry(master, width=40, borderwidth=5)
        self.entry.grid(row=0, column=0, columnspan=4, padx=5, pady=10)

        self.add = Button(text="+", padx=19, pady=10, command=self.buttonAdd).grid(row=4, column=3)
        self.subtract = Button(text="-", padx=20, pady=10, command=self.buttonSubtract).grid(row=3, column=3)
        self.multiply = Button(text="*", padx=20, pady=10, command=self.buttonMultiply).grid(row=2, column=3)
        self.divide = Button(text="/", padx=20, pady=10, command=self.buttonDivide).grid(row=1, column=3)

        self.button1 = Button(text="1", padx=20, pady=10, command=lambda: self.buttonClick(1))
        self.button2 = Button(text="2", padx=20, pady=10, command=lambda: self.buttonClick(2))
        self.button3 = Button(text="3", padx=20, pady=10, command=lambda: self.buttonClick(3))
        self.button4 = Button(text="4", padx=20, pady=10, command=lambda: self.buttonClick(4))
        self.button5 = Button(text="5", padx=20, pady=10, command=lambda: self.buttonClick(5))
        self.button6 = Button(text="6", padx=20, pady=10, command=lambda: self.buttonClick(6))
        self.button7 = Button(text="7", padx=20, pady=10, command=lambda: self.buttonClick(7))
        self.button8 = Button(text="8", padx=20, pady=10, command=lambda: self.buttonClick(8))
        self.button9 = Button(text="9", padx=20, pady=10, command=lambda: self.buttonClick(9))
        self.button0 = Button(text="0", padx=20, pady=10, command=lambda: self.buttonClick(0))
        self.button_C = Button(text="C", padx=19, pady=10, command=self.clearEntry)
        self.button_dot = Button(text=".", padx=20, pady=10)
        self.button_equals = Button(text="=", padx=118, pady=10, command=self.buttonEqual)

        # locate buttons
        self.button1.grid(row=3, column=0)
        self.button2.grid(row=3, column=1)
        self.button3.grid(row=3, column=2)

        self.button4.grid(row=2, column=0)
        self.button5.grid(row=2, column=1)
        self.button6.grid(row=2, column=2)

        self.button7.grid(row=1, column=0)
        self.button8.grid(row=1, column=1)
        self.button9.grid(row=1, column=2)

        self.button0.grid(row=4, column=0)
        self.button_C.grid(row=4, column=2)
        self.button_dot.grid(row=4, column=1)
        self.button_equals.grid(row=5, columnspan=4)

    def buttonClick(self, number):
        current = self.entry.get()
        self.entry.delete(0, END)
        self.entry.insert(0, str(current) + str(number))

    def clearEntry(self):
        self.entry.delete(0, END)

    def buttonAdd(self):
        first_number = self.entry.get()
        global first_num
        global math
        math = "addition"
        first_num = int(first_number)
        self.entry.delete(0, END)

    def buttonSubtract(self):
        first_number = self.entry.get()
        global first_num
        global math
        math = "subtraction"
        first_num = int(first_number)
        self.entry.delete(0, END)

    def buttonMultiply(self):
        first_number = self.entry.get()
        global first_num
        global math
        math = "multiplication"
        first_num = int(first_number)
        self.entry.delete(0, END)

    def buttonDivide(self):
        first_number = self.entry.get()
        global first_num
        global math
        math = "division"
        first_num = int(first_number)
        self.entry.delete(0, END)

    def buttonEqual(self):
        try:
            if not self.entry.get():
                raise EmptyInput

            second_number = self.entry.get()
            self.entry.delete(0, END)

            if math == "addition":
                self.entry.insert(0, first_num + int(second_number))

            if math == "subtraction":
                self.entry.insert(0, first_num - int(second_number))

            if math == "multiplication":
                self.entry.insert(0, first_num * int(second_number))

            if math == "division":
                self.entry.insert(0, first_num / int(second_number))

        except ZeroDivisionError:
            self.entry.insert(0, "You cannot divide by zero!")

        except EmptyInput:
            self.entry.insert(0, "Empty input")


root = Tk()
app = Calculator(root)
root.mainloop()
