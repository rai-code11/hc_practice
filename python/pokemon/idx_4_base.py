# ポケモンクラスを定義する
# 属性：name,type1,type2,hp
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp
        self.exText = f"{self.name}は{self.type1}タイプのポケモン"

    def attack(self):
        print(f"{self.name}のこうげき")

    def __del__(self):
        print(f"{self.name}が消えた！")


rizardon = Pokemon("リザードン", "ほのお", "ひこう", 100)
rizardon.attack()
text = rizardon.exText
print(text)
del rizardon
# attack = rizardon.attack()
