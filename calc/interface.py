import tkinter
import fn

class Window:

    def __init__(self):
        self.root = tkinter.Tk()
        self.enter = tkinter.Entry()
        self.bufer = []
        

    def draw(self):
        BUTTON_VALUE = ((1, 2, 3, '+'), (4, 5, 6, '-'), (7, 8, 9, '*'), (0, 'C', '=', '/'))
        self.root.wm_attributes("-topmost", 1)
        
        self.enter.grid(row=0, column=0, columnspan=4)

        for r, values in enumerate(BUTTON_VALUE, 1):
            for c, value in enumerate(values):
                if isinstance(value, int):
                    button = tkinter.Button(text=str(value), highlightbackground='#3E4149', command=lambda x = value: self.enter.insert(tkinter.END, x))
                elif value == 'C':
                    button = tkinter.Button(text=str(value), highlightbackground='#3E4149', command=self.clear)
                else:
                    button = tkinter.Button(text=value, highlightbackground='#3E4149', command=lambda x = value: self.calc(x))
                button.grid(row=r, column=c)

        
        self.root.mainloop()

    

    def clear(self):
        self.bufer.clear()
        self.enter.delete(0, tkinter.END)

    def calc(self, operator):      
        if self.enter.get():
            self.bufer.append(self.enter.get())
            if operator == '=':
                result = fn.equals(self.bufer)
                self.clear()
                self.enter.insert(tkinter.END, result)
            else:
                self.bufer.append(operator)
                self.enter.delete(0, tkinter.END)

    