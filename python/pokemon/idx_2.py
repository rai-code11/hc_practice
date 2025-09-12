# Pokemonクラス
# プロパティ
class Pokemon:
    def __init__(self):
        self.name = "リザードン"
        self.type1 = "ほのお"
        self.type2 = "ひこう"
        self.hp = 100
        self.mp = 10

    # メソッドの実装
    def attack(self):
        print(f"{self.name}のこうげき")

    # def main(self):
    #     poke = Pokemon()
    #     print(poke.name)
    #     print(poke.type1)
    #     poke.attack()

    def createPokemon100(self):
        self.pokemons = []
        for _ in range(100):
            poke = Pokemon()
            self.pokemons.append(poke)
        return self.pokemons

    def main(self):
        self.createPokemon100()

        print(self.pokemons[0].name)
        print(self.pokemons[9].type1)
        self.pokemons[99].attack()


poke = Pokemon()
poke.main()
print(poke.mp)
