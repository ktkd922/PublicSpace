'''
2022/06/17 kitakado
日立のDSCで出力されるexcelファイルを読み込み、数値部分をcsvとして出力
-pでplot

<必要要件>
python
pandas
openpyxl
xlrd (?)
matplotlib

<実行方法>
pyファイルを生データと同じフォルダに入れ、コマンドライン上で
python dsc_format.py ***.xlsx
python dsc_format.py ***.xlsx -p

'''

import pandas as pd
import sys
import matplotlib.pyplot as plt

args = sys.argv
filename = args[1]
df = pd.read_excel(filename)

start_point = 0
for i in range(100):
    if df.iloc[i, 0] == 'Time':
        start_point = i + 2
        break

data = df.drop(df.index[:start_point])
data.columns = df.iloc[start_point-2, :]
data = data.drop(data.columns[4:], axis=1)
data.to_csv(filename.removesuffix('.xlsx') + '.csv', index=False)

if '-p' in args:
    plt.plot(data.iloc[:, 1], data.iloc[:, 2], color='blue')
    plt.xlabel('Temperature / ºC')
    plt.ylabel('Exotherm / µW')
    plt.savefig(filename.removesuffix('.xlsx') + '.png',
                bbox_inches="tight", pad_inches=0.05)
    plt.clf()

print('finished')
