import tkinter as tk
from tkinter import ttk


keys = [['AC', 'C', 'C', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '0', '.', '=']]

operators = ['/', '*', '-', '+']

btn_width = 4
btn_height = 2
root_x = 248
root_y = 360


class Application(tk.Frame):
    def __init__(self,master):
        super().__init__(master)
        self.pack()

        self.calc_str = ''
        self.calc_var = 0
        self.master.geometry(f"{root_x}x{root_y}")
        self.master.resizable(width=False, height=False)
        self.master.title("Calculator")
        self.create_widgets()

        self.grid(column=0, row=0)

        # 計算結果の表示領域
        self.label_test = ttk.Label(self)
        self.label_test.configure(text='', font=('', 22))
        self.label_test.pack()
        self.label_test.grid(column=0, row=0, columnspan=4, sticky=tk.E)

        def return_key(event):
            key = event.widget['text']

            if key == 'AC':
                self.calc_str = ''
                self.calc_var = 0
            
            elif key == 'C':
                self.calc_str = self.calc_str[:-1]

            elif key == '=':
                try:
                    self.calc_var = eval(self.calc_str)
                    self.calc_str = str(self.calc_var)
                except:
                    # print('Error')
                    self.label_test.configure(text='Error', font=('', 22))
                    self.calc_str = ''
                    self.calc_var = 0
                    return
            
            elif key == '-':    # マイナスは負数の場合もあるので別扱い
                if self.calc_str and (self.calc_str[-1] in operators):
                    return
                elif self.calc_str == '':
                    self.calc_str += '-'
                else:
                    self.calc_var = eval(self.calc_str)
                    self.calc_str += key
                
            elif key in operators:
                if self.calc_str and (self.calc_str[-1] not in operators):
                    self.calc_var = eval(self.calc_str)
                    self.calc_str += key
                
            else:
                self.calc_str += key
            
            # print(self.calc_str, ',', self.calc_var)
            self.label_test.configure(text=self.calc_str, font=('', 22))

        # ボタンを配置
        for i in range(5):
            for j in range(4):
                key = keys[i][j]
                button = tk.Button(self, text=key, font=('', 18),
                width=btn_width, height=btn_height)
                button.bind('<1>', return_key)
                button.grid(column=j, row=i+1, sticky=tk.NSEW)

        button_0 = tk.Button(self, text='0', font=('', 18))
        button_0.grid(column=0, row=5, columnspan=2, sticky=tk.NSEW)
        button_0.bind('<1>', return_key)


    def create_widgets(self):
        pass

    



def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
