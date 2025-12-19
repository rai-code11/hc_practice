
# hc_practice

Python / HTML / CSS の実装サンプルをまとめたリポジトリです。  
CLI（標準入力・引数処理）、条件分岐の設計、例外設計、OOP（クラス設計）、データモデリング（ERD）などを、動く形で整理しています。

---


## ディレクトリ構成

- `html_css_output_beginner/`
  - ホームページ1ページのレイアウト（HTML/CSS）

- `python/`
  - PythonのCLIツール / ミニアプリ（4本 + OOP学習）

- `twitter_erd/`
  - Twitterの主要機能を想定したデータモデリング（ER図）

---

## 実行環境

- Python 3.x（3.11以上推奨）
- macOS（カレンダー出力が `cal` 風のため）

---

# HTML/CSS

## html_css_output_beginner
HTML/CSSでホームページ1ページをレイアウトした実装です。  
（レスポンシブの余白調整なども含む）

---

# Python

## 1) Grouping（grouping.py）
### 概要
A〜Fの6人をランダムに以下どちらかへ分割し、表示はアルファベット順に整形します。
- 3人 + 3人
- 2人 + 4人

### 実行方法
```bash
python3 grouping.py
````

### 出力例

```txt
["B", "C"]
["A", "D", "E", "F"]
```

---

## 2) Calendar（calendar.py）

### 概要

macの `cal` コマンドに近い見た目でカレンダーを表示するCLIです。
※月曜始まり / `calendar` モジュール不使用
1~12以外の数字を入力した場合例外エラーを出す

### 実行方法

```bash
python3 calendar.py
python3 calendar.py -m 6
python3 calendar.py -m 22
```

---

## 3) Golf Score（golf_score.py）

### 概要

18ホール分の規定打数と打数から、各ホールのスコア（バーディ/ボギー等）を判定し、カンマ区切りで出力します。
標準入力から値を受け取る形で実装しています。

### 実行方法

```bash
cat case_1.txt | python python/golf_score.py
```

---

## 4) Vending Machine（vending_machine/）

### 概要

Suica / ジュース / 自販機 をクラスで設計し、購入・在庫・売上・補充を扱うミニドメインモデルです。
メソッド内で input/print を行わず、戻り値と例外で扱う設計を意識しています。

---

## 5) OOP学習（ポケモンで学ぶ！クラスとオブジェクト指向）

参考リンクをPythonで書き直しながら学習した内容です。

* [https://zenn.dev/m_coder/books/oop-learning-with-pokemon](https://zenn.dev/m_coder/books/oop-learning-with-pokemon)

---

# Twitter ERD（データモデリング）

## twitter_erd

Twitterの主要機能を想定して、ER図（データモデリング）を作成したものです。
命名規約・制約（uniq）・外部キー表現など、ルールに沿った設計を意識しています。

### ER図の生成

BurntSushi/erd を使用（`.er` → `.pdf`）

```bash
docker run -i ghcr.io/burntsushi/erd:latest < sample.er >| out.pdf
```

* [https://github.com/BurntSushi/erd](https://github.com/BurntSushi/erd)

```

