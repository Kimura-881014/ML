import json
import pandas as pd
import os

json_encoding = "utf-8"  # エンコーディングを指定

dir_path = "json"
files = os.listdir(dir_path)
# print(files)

li = []

for file in files:
    with open(f'./json/{file}', encoding=json_encoding) as f:
        # 各ファイルごとにDataFrameに変換し、リストに追加
        data = json.load(f)
        # print(data)
        li.append(pd.DataFrame(data))

# リストに格納されたすべてのDataFrameを結合
df = pd.concat(li, ignore_index=True)
df.insert(1, 'input', "")
# print(df.shape)

df.to_csv('./my_data.csv',index=False)

df = pd.read_csv('./my_data.csv')
# print(df.head)
# print(type(df))
# print(df.shape)
df.to_json('my_data.json', orient='records')

print(ord('ス'))