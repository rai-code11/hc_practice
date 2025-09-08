# 継承
from idx_4_base import Pokemon


class Pikachu(Pokemon):
    def __init__(self, name, type1, type2, hp):
        super().__init__(name, type1, type2, hp)

    def main(self):
        print(pika.name)
        print(pika.attack())

    # オーバーライド
    def attack(self):
        # 子クラスから親クラスのメソッドを呼ぶ
        super().attack()
        print(f"{pika.name}の１０万ボルト！")


pika = Pikachu("ピカチュウ", "でんき", "", 100)
pika.main()
pika.attack()
