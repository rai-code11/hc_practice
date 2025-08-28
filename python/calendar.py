# sysモジュールをインポート
import sys

# datetimeモジュールをインポート
import datetime as dt

# 入力した文字列をリスト化する
print(sys.argv)

# 現在の日時を取得し、now変数に代入
now = dt.datetime.now()

# もし"-m"が入力されたらそれをindexとして指定、その後に入れたstringをintegerに変換して変数monthとして定義する
month = now.month
if "-m" in sys.argv:
    idx = sys.argv.index("-m")
    # "-m"の次に数字が入っているかを確認し、入っていなかったら現在の月をmonthとして定義する
    if idx + 1 < len(sys.argv):
        month = int(sys.argv[idx + 1])
        if month < 1 or month > 12:
            print(f"{month} is neither a month number (1..12) nor a name")
    else:
        month = now.month


# 年と月を取得し、フォーマットでビジュアルを中央に整える
cell = 4
calender_title = f"{month}月 {now.year}"
width = cell * 7
print(f"{calender_title:^{width}}")

# 曜日をリストに格納する
weekdays = ["月", "火", "水", "木", "金", "土", "日"]

# 曜日の幅を整えるために、weekdaysの各要素に幅を追加しjoinして表示
week_width = cell - 1

# 省略前
# week_parts = []
# for w in weekdays:
#     parts.append(f"{w:>{week_width}}")

# print("".join(week_parts))

# 　省略後(内包表記を使用)
print("".join(f"{w:>{week_width}}" for w in weekdays))

# 日付が入ったリストを作る(リスト内包表記を使用)
days = [d for d in range(1, 32)]

# 該当月の初日を求める
first_day = days[0]

# 該当月の最終日を求める

## 日付の数を精査するために月のリストを作る
month_days_31 = [1, 3, 5, 7, 8, 10, 12]
month_days_30 = [4, 6, 9, 11]


### うるう年を求める関数を定義する
def leap_year(year):
    return year % 4 == 0 and (year % 100 != 0 or year % 400 == 0)


#### 該当月の最終日を求める
if now.month in month_days_31:
    last_day = days[30]
elif now.month in month_days_30:
    last_day = days[29]
else:
    if leap_year(now.year):
        last_day = days[28]
    else:
        last_day = days[27]


# 初日~最終日までの日付部分を出す
total_days = days[:last_day]

# カレンダーのどの曜日から表示するかを求める
## ⚪︎曜日(数値判定)の数字分、1日をセットバックする
### 該当月の1日とセットバック数を求める
today = dt.date.today()
first = dt.date(today.year, month, 1)
setback = first.weekday()

# 1日を入れる場所を決めるためにsetbackの数値分を月の日付(total_days)の前に追加する
# month_startが7の倍数になったら改行するためにリストにする
month_start = (["   "] * setback) + total_days

# month_startのindexを0からスタートするとkeyの値がズレるため、1からスタートさせてindexが7の倍数の次のindexに\nをappendする
# month_startにfor文でappendしていくとkeyがズレるため新しくmonth_start_line_breakを作成する

# 修正前
month_start_line_break = []
for key, value in enumerate(month_start, start=1):
    month_start_line_break.append(value)
    if key % 7 == 0:
        month_start_line_break.append("\n")

# 文字の整形を行う
## \nに対して整形を行わないようにする

# 修正前
# formatted = []
# for v in month_start_line_break:
#     if v != "\n":
#         formatted.append(f"{v:>{cell}}")
#     else:
#         formatted.append("\n")

# 修正後(リスト内包表記を使用)
formatted = [f"{v:>{cell}}" if v != "\n" else "\n" for v in month_start_line_break]

### 文字列として表示するためにjoinする
#### month_start_line_breakを文字列に変換する

# 修正前
# parts = []
# for v in formatted:
#     parts.append(str(v))

# joined_month_start_line_break = "".join(parts)

# 修正後(リスト内包表記を使用)
joined_month_start_line_break = "".join(str(v) for v in formatted)
print(joined_month_start_line_break)
