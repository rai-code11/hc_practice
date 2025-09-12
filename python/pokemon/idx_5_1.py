# 抽象クラスの使い方
# ポケモンクラスを定義する
# 属性：name,type1,type2,hp
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        pass


# 継承
class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    # オーバーライド
    def attack(self):
        # 子クラスから親クラスのメソッドを呼ぶ
        super().attack()
        print(f"{pika.name}の１０万ボルト！")

    def main(self):
        print(pika.name)
        pika.attack()


pika = Pikachu("ピカチュウ", "でんき", "", 100)
pika.main()
