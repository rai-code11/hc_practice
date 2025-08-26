# ramdomをインポートする
import random

# ６人のグループを1つのリストにまとめる
members = ["A", "B", "C", "D", "E", "F"]

# リストをランダムにしたリストを定義する
random_group = random.sample(members, 6)

# 3:3の組と4:2の組をそれぞれランダムに分ける
if random.randint(0, 1) == 0:
    # グループから３人ランダムで選び、グループA,Bに入れる
    group_A = random_group[:3]
    group_B = random_group[3:]
    print(sorted(group_A))
    print(sorted(group_B))
else:
    # ４人と２人の組に分ける
    group_A_4 = random_group[:4]
    group_B_2 = random_group[4:]
    print(sorted(group_A_4))
    print(sorted(group_B_2))
