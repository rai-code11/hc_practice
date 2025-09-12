# カプセル化とinterface
class InterfaceNameService:

    def change_name(self, new_name):
        raise NotImplementedError("サブクラスで定義してください")

    def get_name(self):
        raise NotImplementedError("サブクラスで定義してください")


class Pokemon(InterfaceNameService):
    def __init__(self, name, type1, type2, hp):
        self.name = name
        self.type1 = type1
        self.type2 = type2
        self.hp = hp

    def attack(self):
        return f"{self.name}のかえんほうしゃ！"

    def change_name(self, new_name):
        if new_name == "うんこ":
            raise ValueError("不適切な名前です")
        self.name = new_name

    def get_name(self):
        return self.name


class Player(InterfaceNameService):
    def change_name(self, new_name):
        if new_name == "うんこ":
            raise ValueError("不適切な名前です")
        self.name = new_name

    def get_name(self):
        return self.name


poke = Pokemon("リザードン", "ほのお", "ひこう", 100)
poke.change_name("ヒトカゲ")
print(poke.get_name())
poke.change_name("うんこ")
print(poke.get_name())
