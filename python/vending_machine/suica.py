# Suicaの設計図
# 属性：name: str,balance: int
class Suica:
    # 初期値の設定
    def __init__(self, user_id, balance=500):
        self.user_id = user_id
        self._balance = balance
        # deposit = 500
        # self.balance += deposit

    # balanceに外部から不適切な編集をできないようにする
    @property
    def balance(self):
        return self._balance

    @balance.setter
    def balance(self, num):
        if num < 0:
            raise ValueError("残高にマイナスの数値を入れることはできません")
        self._balance = num

    # 金額をチャージするメソッド
    def charge(self, charge_amount):
        charge_limit = 100
        try:
            # 例外が発生する可能性がある処理
            charge_amount = int(charge_amount)
        except ValueError:
            # 例外が起きた時の処理
            raise ValueError("数値を入力してください")

        if charge_amount < charge_limit:
            raise ValueError(
                f"{charge_limit}円未満の金額をチャージすることはできません"
            )
        else:
            self.balance += charge_amount
            return f"{charge_amount}円チャージしました\n{self.show_balance()}"

    # 残高を表示するメソッド
    def show_balance(self):
        return self.balance

    # 残高を減らすメソッド
    # 省略前
    # def reduce_balance(self, suica, item_name, purchase_qty):
    #     self.purchase_qty = purchase_qty
    #     price = self.get_price(item_name)
    #     purchase_amount = price * self.purchase_qty
    #     # 残高 = 残高 - 購入金額
    #     suica.balance -= purchase_amount
    #     return suica.balance

    # # VendingMachineクラスのget_priceメソッドを使うためのメソッド
    # def get_price(self, item_name):
    #     vm = VendingMachine()
    #     return vm.get_price(item_name)

    # 残高を減らすメソッド
    # 省略後
    def reduce_balance(self, suica, vending_machine, item_name, purchase_qty):
        price = vending_machine.get_price(item_name)
        purchase_amount = price * purchase_qty
        # 残高 = 残高 - 購入金額
        suica.balance -= purchase_amount
        return suica.balance
