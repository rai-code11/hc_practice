# sysモジュールをインポート
import sys

# datetimeモジュールをインポート
import datetime

# 　現在の日時を取得し、now変数に代入
now = datetime.datetime.now()

# 年を取得
print("年:", now.year)

# 月を取得
print("月:", now.month)

# 年と月をまとめて取得
print(f"{now.month}月 {now.year}")

# 曜日をリストに格納する
weekdays = ["月", "火", "水", "木", "金", "土", "日"]

# リストの中の文字列を連結して表示

print(" ".join(weekdays))
