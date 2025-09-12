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


# VendingMachineクラス
# 属性：stock: Dict[Juice, int],sales_amount: int
class VendingMachine:
    def __init__(self):

        self.stock = {
            Juice("pepsi", 150): 5,
            Juice("monster", 230): 5,
            Juice("irohasu", 120): 5,
        }

        self._sales_amount = 0

    # 在庫数を取得するメソッド
    def get_stock(self, item_name):
        self.item_name = item_name
        for juice, qty in self.stock.items():
            if item_name == juice.name:
                if self.stock[juice] >= 0:
                    return qty
                else:
                    raise ValueError(f"{item_name}の在庫がありません")
        raise ValueError(f"{item_name}は取り扱っていません")

    # 購入できるか判断するメソッド
    # 購入金額よりも残高の方が大きいand購入個数より在庫が多い
    # purchase_qty:購入個数
    # ユーザーが作成したsuicaインスタンスを引数にとる
    def can_purchase(self, suica, item_name, purchase_qty):
        self.purchase_qty = purchase_qty

        # 購入金額 = 値段 × 購入個数
        # item_nameの変数で取得できるようにする
        price = self.get_price(item_name)
        purchase_amount = price * self.purchase_qty

        # if文は真偽値なのでそのまま返す
        return purchase_amount <= suica.balance and self.purchase_qty <= self.get_stock(
            item_name
        )

    # 購入判断のための商品の価格を取ってくるメソッド
    def get_price(self, item_name):
        for juice in self.stock:
            if juice.name == item_name:
                return juice.price
        raise ValueError(f"{item_name}は取り扱っていません")

    # 購入処理をまとめる
    # 購入処理：①在庫を減らす②売上金額を増やす
    # もしmanage_purchaseがTrueだったら購入処理を実行する
    def manage_purchase(self, suica, item_name, purchase_qty):

        if not self.can_purchase(suica, item_name, purchase_qty):
            raise ValueError(f"在庫がないかチャージ金額が足りません")

        reduce_after = self.reduce_stock(item_name)
        amount = self.add_to_sales_amount(item_name)

        return reduce_after, amount

    # 在庫を減らすメソッド
    def reduce_stock(self, item_name):
        # 在庫数 = 在庫数 - 購入数
        for juice in self.stock:
            if item_name == juice.name:
                if self.stock[juice] < self.purchase_qty:
                    raise ValueError(f"{item_name}の在庫が足りません")
                self.stock[juice] -= self.purchase_qty
                return self.stock[juice]

    # 売上金額を増やしていくメソッド
    def add_to_sales_amount(self, item_name):
        price = self.get_price(item_name)
        purchase_amount = price * self.purchase_qty
        # 売上金額 = 売上金額 + 購入金額
        self._sales_amount += purchase_amount
        return self._sales_amount

    # 購入可能なドリンクのリストを取得するメソッド
    def get_purchase_list(self):
        # 購入可能:在庫が０ではない
        # itemとpurchase_qtyを同時にfor文で回してitemをリストに追加する

        # 省略前
        # purchase_qty_list = []
        # for juice, qty in self.stock.items():
        #     if qty > 0:
        #         purchase_qty_list.append(juice.name)
        # return purchase_qty_list

        # 省略後
        purchase_qty_list = [juice.name for juice, qty in self.stock.items() if qty > 0]
        return purchase_qty_list

    # 在庫を追加するメソッド
    # 購入された分、在庫数に足してその値をdict:stockに代入する

    def add_stock(self, item_name):
        for juice, qty in self.stock.items():
            if item_name == juice.name:
                self.stock[juice] = qty + self.purchase_qty
        return self.stock[juice]


suica1 = Suica("user1")
show_balance = suica1.show_balance()
print(show_balance)
charge = suica1.charge(2000)
print(charge)

vm = VendingMachine()
manage_purchase = vm.manage_purchase(suica1, "pepsi", 5)
print(manage_purchase)
purchsae_l = vm.get_purchase_list()
print(purchsae_l)
result_stock = vm.add_stock("pepsi")
print(result_stock)
purchsae_l = vm.get_purchase_list()
print(purchsae_l)
got_stock = vm.get_stock("pepsi")
print(got_stock)
got_price = vm.get_price("pepsi")
print(got_price)

reduced_balance = suica1.reduce_balance(suica1, vm, "pepsi", 5)
print(reduced_balance)
