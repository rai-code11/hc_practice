# カプセル化
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self._name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, pokemon_name):
        if pokemon_name == "うんこ":
            raise ValueError("不適切な名前です")
        self._name = pokemon_name


rizardon = Pokemon("リザードン", "ほのお", "ひこう", 100)
rizardon.name = "うんこ"
print(rizardon)
