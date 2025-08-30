# ゴルフスコア判定プログラム

# ゴルフの規定打数(X)を受け取りリストに格納
pars = list(map(int, input().split(",")))
# プレイヤーの打数(Y)を受け取りリストに格納
strokes = list(map(int, input().split(",")))

# for文を使ってX,Yを回してスコアを判定していく
relative_scores = {
    "Par": "パー",
    "Birdie": "バーディ",
    "Eagle": "イーグル",
    "Albatross": "アルバトロス",
    "Condor": "コンドル",
    "Ace": "ホールインワン",
    "Bogey": "ボギー",
}
scores = []

for x, y in zip(pars, strokes):
    if y - x == 0:
        scores.append(relative_scores["Par"])
    elif y - x == -1:
        scores.append(relative_scores["Birdie"])
    elif y - x == -2:
        scores.append(relative_scores["Eagle"])
    elif y == 5 and y == 2:
        scores.append(relative_scores["Albatross"])
    elif y == 2 and y == 5:
        scores.append(relative_scores["Condor"])
    elif y == 1:
        scores.append(relative_scores["Ace"])
    elif y - x == 1:
        scores.append(relative_scores["Bogey"])
    else:
        scores.append(f"{y - x}ボギー")
# スコアのリストを出力
result = ",".join(scores)
print(result)


# X-Yの形式でスコアを出力する
