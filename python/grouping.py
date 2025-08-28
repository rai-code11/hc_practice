# ramdomをインポートする
import random

# ６人のグループを1つのリストにまとめる
members = ["A", "B", "C", "D", "E", "F"]

# リストをランダムにしたリストを定義する
random_group = random.sample(members, 6)

# 3:3の組と4:2の組をそれぞれランダムに分ける
# 変数idxに3か4のどちらかをランダムに代入
idx = random.choice([3, 4])

# 変数idxを使ってリストを分割し、グループAとグループBに格納
group_A = random_group[:idx]
group_B = random_group[idx:]
print(sorted(group_A))
print(sorted(group_B))
