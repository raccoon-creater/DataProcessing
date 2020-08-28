import pandas as pd
import matplotlib.pyplot as plt
import japanize_matplotlib

#CSVファイルを読み込む
df1 = pd.read_csv("csv/ファイル名.csv",index_col=0)


#グラフを作って画像ファイル出力する
df1.plot.bar(figsize=(10,8))
df1.plt.savefig("ファイル名.png")

