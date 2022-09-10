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

2022/09/10
µW/mg単位に変換

'''

import pandas as pd
import sys
import matplotlib.pyplot as plt

args = sys.argv
filename = args[1]
df = pd.read_excel(filename)

start_point = 0
for i in range(100):
    if df.iloc[i, 0] == 'Sample Weight':
        sample_weight = df.iloc[i, 1]
        print('sample weight =', sample_weight, ' mg')
    elif df.iloc[i, 0] == 'Time':
        start_point = i + 2
        break

data = df.drop(df.index[:start_point])
data.columns = df.iloc[start_point-2, :]
data = data.drop(data.columns[4:], axis=1)

# 単位の変換
data['DSC'] = data['DSC'] / sample_weight
data['DDSC'] = data['DDSC'] / sample_weight
data.set_axis(['Time / min', 'DSC / µW mg-1', 'Temp / dC',
              'DDSC / µW mg-1min-1'], axis='columns', inplace=True)

# 保存
data.to_csv(filename.removesuffix('.xlsx') + '.csv', index=False)

# pyplot
if '-p' in args:
    plt.plot(data.iloc[:, 1], data.iloc[:, 2], color='blue')
    plt.xlabel('Temperature / ºC')
    plt.ylabel('Exotherm / µW•mg-1')
    plt.savefig(filename.removesuffix('.xlsx') + '.png',
                bbox_inches="tight", pad_inches=0.05)
    plt.clf()

print('finished')
