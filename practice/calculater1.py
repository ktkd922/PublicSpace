import tkinter as tk
from tkinter import ttk


# ボタンの配置を二次元配列に格納。後で（）キーを追加する。
keys = [['AC', 'C', 'C', '/'],
        ['7', '8', '9', '*'],
        ['4', '5', '6', '-'],
        ['1', '2', '3', '+'],
        ['0', '0', '.', '=']]

operators = ['/', '*', '-', '+']

root_x = 360
root_y = 360
label_fontsize = 22
btn_width = 4
btn_height = 2
btn_fontsize = 18

class Application(tk.Frame):

    def __init__(self, master):     # 初期化
        super().__init__(master)    # 親クラス（tk.Frame) の__init__を実行

        self.calc_str = ''
        self.calc_var = 0
        self.master.geometry(f"{root_x}x{root_y}")
        
        # self.master.resizable(width=False, height=False)
        # 画面サイズによってはみ出すのでサイズ変更可能にする。後でウィンドウサイズで調整できるように変更する。
        
        self.master.title("Calculator")
        self.create_widgets()


    def create_widgets(self):   # ラベル、ボタンを配置
        self.grid(column=0, row=0)

        # 計算結果の表示領域
        self.label_test = ttk.Label(self)
        self.label_test.configure(text='', font=('', label_fontsize))
        self.label_test.pack()
        self.label_test.grid(column=0, row=0, columnspan=4, sticky=tk.E)

        for i in range(5):      # ボタンを配置
            for j in range(4):
                key = keys[i][j]
                button = tk.Button(self, text=key, font=('', btn_fontsize),
                                   width=btn_width, height=btn_height)
                button.bind('<1>', self.apply_key)      # tkinter.Eventインスタンスを引数として渡す
                button.grid(column=j, row=i+1, sticky=tk.NSEW)

        button_0 = tk.Button(self, text='0', font=('', btn_fontsize))
        button_0.grid(column=0, row=5, columnspan=2, sticky=tk.NSEW)
        button_0.bind('<1>', self.apply_key)


    def apply_key(self, event):     # キー操作を反映
        key = event.widget['text']      # event.widget : イベントを受け付けたウィジェット

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
                self.label_test.configure(text='Error')
                self.calc_str = ''
                self.calc_var = 0
        
        elif key == '-':    # マイナスは演算子ではなく負数の場合もあるので別扱い
            if self.calc_str == '':
                self.calc_str += '-'
            elif self.calc_str[-1] in operators:
                self.calc_str = self.calc_str[:-1] + '-'
            else:
                self.calc_var = eval(self.calc_str)
                self.calc_str += key
        
        elif key in operators:
            if self.calc_str == '':
                return
            elif self.calc_str[-1] in operators:
                self.calc_str = self.calc_str[:-1] + key
            else:
                self.calc_str += key
        
        else:
            self.calc_str += key

        self.label_test.configure(text=self.calc_str, font=('', label_fontsize))    # 表示領域を更新


def main():
    root = tk.Tk()
    app = Application(master=root)
    app.mainloop()


if __name__ == "__main__":
    main()
