# Suicaの設計図
# 属性：name,deposit,balance
# メソッド：金額をチャージする,残高を表示する


class Suica:
    # 初期値の設定
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.deposit = 500
        self.balance = balance

    # 金額をチャージするメソッド
    def charge(self, charge_amount):
        charge_limit = 100
        charge_amount = int(charge_amount)
        try:
            # 例外が発生する可能性がある処理
            if charge_amount < charge_limit:
                print(f"{charge_limit}円未満の金額をチャージすることはできません")
            else:
                self.balance += charge_amount
                print(f"{charge_amount}円チャージしました")
        except ValueError:
            # 例外が起きた時の処理(
            print(f"{charge_limit}円未満の金額をチャージすることはできません")

        return self.show_balance()

    # 残高を表示するメソッド
    def show_balance(self):
        print(f"現在の{self.user_id}の残高は{self.balance}です")


# suica1 = Suica(1, 2000)
# suica1.charge(50)


# juiceクラスからペプシインスタンスを作っていくという感じ
# 属性:name,price
class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# VendingMachineクラス
class VM:
    def __init__(self):
        # 150円のpepsiリストを作りインスタンスを5個格納する
        self.pepsi = Juice("pepsi", 150)
        self.drinks = {
            "pepsi": {"item": self.pepsi, "quantity": 5},
        }

    # 在庫数を取得するメソッド
    def get_stock(self):
        return self.drinks["pepsi"]["quantity"]
    
    # 購入できるか判断するメソッド
    # もし購入金額よりも残高の方が大きければ買える
    def purchase(self):
        if self.balance 


# vm = VM()
# print(vm.get_stock())
