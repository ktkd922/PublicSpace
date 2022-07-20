# 2022/7/20
# 電卓機能をもつGUIアプリを作成

# tkinterのimportでエラーが出た。python-tkをインストールすると解決。
import tkinter as tk


root_x = 280
root_y = 380

root = tk.Tk()
root.geometry(f'{root_x}x{root_y}')
root.title('Calculater.py')

frame = tk.Frame(root)
frame.grid(column=0, row=0)

keys = [['AC', 'C', '%', '÷'],
        [7, 8, 9, '×'],
        [4, 5, 6, '−'],
        [1, 2, 3, '+'],
        [0, 0, '.', '=']]

btn_width = 3
btn_height = 3

for i in range(5):
    for j in range(4):
        key = keys[i][j]
        button = tk.Button(frame, text=key, font=('', 18), width=btn_width, height=btn_height)
        button.grid(column=j, row=i, sticky=tk.NSEW)

button_0 = tk.Button(frame, text=0, font=('', 18))
button_0.grid(column=0, row=4, columnspan=2, sticky=tk.NSEW)

root.mainloop()
