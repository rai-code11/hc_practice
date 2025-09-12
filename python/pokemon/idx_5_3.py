# 抽象クラスの使い方余談
# ポケモンクラスを定義する
# インターフェース/多重継承
class PokemonAttack:
    def attack(self):
        raise NotImplementedError("サブクラスでattackを実装してください")


class PokemonProtect:
    def protect(self):
        raise NotImplementedError("サブクラスでprotectを実装してください")


class PokemonRunAway:
    def run_away(self):
        raise NotImplementedError("サブクラスでrun_awayを実装してください")


# 多重継承
class Pikachu(PokemonAttack, PokemonProtect, PokemonRunAway):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    # オーバーライド
    def attack(self):
        print(f"{self.name}の１０万ボルト！")

    def protect(self):
        print(f"{self.name}はかみなりで身を守った！")

    def run_away(self):
        print(f"{self.name}は電光石火で逃げた！")

    def main(self):
        print(self.name)
        self.attack()
        self.protect()
        self.run_away()


# 多重継承
class Lizardon(PokemonAttack, PokemonProtect, PokemonRunAway):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    # オーバーライド
    def attack(self):
        print(f"{self.name}のかえんほうしゃ")

    def protect(self):
        print(f"{self.name}は翼で身を守った！")

    def run_away(self):
        print(f"{self.name}は空を飛んで逃げた！")

    def main(self):
        print(self.name)
        self.attack()
        self.protect()
        self.run_away()


pika = Pikachu("ピカチュウ", "でんき", "", 100)
pika.main()
Liza = Lizardon("リザードン", "ほのお", "ひこう", 100)
Liza.main()
