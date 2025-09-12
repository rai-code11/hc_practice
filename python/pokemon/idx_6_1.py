# カプセル化
class Pokemon:
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        pass

    def change_name(self, new_name):
        if new_name == "うんこ":
            return "不適切な名前です"
        self.name = new_name


rizardon = Pokemon("リザードン", "ほのお", "ひこう", 100)
rizardon.name = "うんこ"
print(rizardon.change_name("ゼニガメ"))
