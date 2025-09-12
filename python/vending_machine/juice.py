# juiceクラスからペプシインスタンスを作っていくという感じ
# 属性:name: str,price: int
class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price

    # priceに外部から不適切な編集をできないよ不適切な編集をできないようにする
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, num):
        if not isinstance(num, int):
            raise TypeError("価格は整数で入力してください")

        if num < 0:
            raise ValueError("価格にマイナスの値を入れることはできません")
        self._price = num
