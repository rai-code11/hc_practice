# ゴルフスコア判定プログラム

# 入力された規定打数str(X)を,で分割してリスト:parsに格納
# pars = list(map(int, input().split(","))
# # 入力された実際の打数str(Y)を,で分割してリスト:strokesに格納
# strokes = list(map(int, input().split(","))

# 条件:(X は3 ≤ X ≤ 5,1 ≤ Y)以外の数値を入れられたらinput文を再表示するようにする
# もし条件1,2,3が満たされない場合、再入力を要求する
# 条件1：parsに3より下の数字and5より大きい数字不可
# 条件2:strokesに1より小さい数字は不可
# 条件3:pars,strokesに数字以外は不可
limit = {"l1": 1, "l2": 3, "l3": 5}

while True:
    pars = input().split(",")
    strokes = input().split(",")
    # for文で回して数時間か否かを判断する
    if not all(p.isdigit() for p in pars):
        print("規定打数は数字で入力してください")
        continue

    if not all(s.isdigit() for s in strokes):
        print("打数は数字で入力してください")
        continue
    # str型の数字をintに変換してリストに格納
    pars = list(map(int, pars))
    strokes = list(map(int, strokes))
    # for文で回して規定打数,打数の数値が正しいかを判断する
    if not all(limit["l2"] <= p <= limit["l3"] for p in pars):
        print(f"規定打数に{"l2"}~{"l3"}以外の値を入れることはできません")
        continue

    if not all(s >= limit["l1"] for s in strokes):
        print(f"打数には{limit["l1"]}より小さい値を入れることはできません")
        continue

    break

# for文を使ってX,Yを回してスコアを判定していく
# 取り出しやすいようにdictionary:relative_scoreにまとめる
relative_scores = {
    "Par": "パー",
    "Birdie": "バーディ",
    "Eagle": "イーグル",
    "Albatross": "アルバトロス",
    "Condor": "コンドル",
    "Ace": "ホールインワン",
    "Bogey": "ボギー",
}

# スコアを格納するlist:scoresを用意する
scores = []

# スコア判定条件
# アルバトロスとコンドルとホールインワンの条件を整理

for p, s in zip(pars, strokes):
    if p == s:
        scores.append(relative_scores["Par"])
    elif p - s == 1:
        scores.append(relative_scores["Birdie"])
    elif p - s == 2 and s != 1:
        scores.append(relative_scores["Eagle"])
    elif p == 5 and s == 2:
        scores.append(relative_scores["Albatross"])
    elif p - s == 4 and p == 5:
        scores.append(relative_scores["Condor"])
    elif s == 1:
        scores.append(relative_scores["Ace"])
    elif p - s == -1:
        scores.append(relative_scores["Bogey"])
    else:
        scores.append(f"{s - p}{relative_scores["Bogey"]}")


# スコアのリストを出力
result = ",".join(scores)
print(result)
