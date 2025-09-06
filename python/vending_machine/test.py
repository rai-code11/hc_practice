# Suicaの設計図
# 属性：name,deposit,balance
# メソッド：金額をチャージする,残高を表示する


class Suica:
    # 初期値の設定
    def __init__(self, user_id, balance):
        self.user_id = user_id
        self.__balance = balance
        deposit = 500
        self.__balance += deposit

    # VMクラスからbalanceを呼べるようにするためにgetterを設定する
    @property
    def balance(self):
        return self.__balance

    # VMクラスから変更できるようにするためにsetterを設定する
    @balance.setter
    def balance(self, num):
        if num < 0:
            raise ValueError("残高にマイナスの数値を入れることはできません")
        self.__balance = num

    # 金額をチャージするメソッド
    def charge(self, charge_amount):
        charge_limit = 100
        try:
            # 例外が発生する可能性がある処理
            charge_amount = int(charge_amount)
        except ValueError:
            # 例外が起きた時の処理(
            raise ValueError("数値を入力してください")

        if charge_amount < charge_limit:
            raise ValueError(
                f"{charge_limit}円未満の金額をチャージすることはできません"
            )
        else:
            self.__balance += charge_amount
            return f"{charge_amount}円チャージしました\n{self.show_balance()}"

    # 残高を表示するメソッド
    def show_balance(self):
        return self.__balance


# juiceクラスからペプシインスタンスを作っていくという感じ
# 属性:name,price
class Juice:
    def __init__(self, name, price):
        self.name = name
        self.price = price


# VendingMachineクラス
class VM:
    def __init__(self):
        # 1種類1インスタンスでドリンクを作成してリスト化する
        self.pepsi_l = [Juice("pepsi", 150) for _ in range(5)]
        self.monster_l = [Juice("monster", 230) for _ in range(5)]
        self.irohasu_l = [Juice("irohasu", 120) for _ in range(5)]
        # 取り出しやすいようにdict:self.drinksに格納
        self.drinks = {
            "pepsi": self.pepsi_l,
            "monster": self.monster_l,
            "irohasu": self.irohasu_l,
        }

        # Suicaインスタンスの情報を格納しておく
        self.suica1 = Suica(1, 0)
        self.suicas = {
            "suica1": {"item": self.suica1},
        }

        self.__sales_amount = 0

        # 在庫を補充のためのリスト作成
        # 初期の在庫数を格納するリスト
        self.base_stock_num = {}
        for name, l in self.drinks.items():
            self.base_stock_num[name] = len(l)

        # 在庫補充の際にインスタンスを作るための商品価格表
        self.price_list = {"pepsi": 150, "monster": 230, "irohasu": 120}

    # 在庫数を取得するメソッド
    def get_stock(self, item_name):
        self.item_name = item_name
        self.stock_num = len(self.drinks[self.item_name])
        return self.stock_num

    # 購入できるか判断するメソッド
    # 購入金額よりも残高の方が大きいand購入個数より在庫が多い
    # purchase_qty:購入個数
    def can_purchase(self, item_name, purchase_qty):
        self.item_name = item_name
        self.purchase_qty = purchase_qty
        # 購入金額 = 値段 × 購入個数
        # item_nameの変数で取得できるようにする
        price = self.price_list[item_name]
        self.purchase_amount = price * self.purchase_qty
        # Suicaクラスからインスタンスを作成してそのbalanceを持ってこないとけない？
        # if文は真偽値なのでそのまま返す
        return (
            self.purchase_amount <= self.suica1.balance
            and self.purchase_qty <= self.get_stock(self.item_name)
        )

    # 購入処理をまとめる
    # 購入処理：①在庫を減らす②売上金額を増やす③Suicaのチャージ残高を減らす
    # もしmanage_purchaseがTrueだったら購入処理を実行する
    def manage_purchase(self, item_name, purchase_qty):
        self.item_name = item_name
        self.purchase_qty = purchase_qty
        if self.can_purchase(item_name, purchase_qty):
            reduce_after = self.reduce_stock(item_name, purchase_qty)
            amount = self.calculate_sales_amount()
            balance_after = self.reduce_balance()

            return reduce_after, amount, balance_after
        else:
            raise ValueError(f"在庫がないかチャージ金額が足りません")

    # 在庫を減らすメソッド
    def reduce_stock(self, item_name, purchase_qty):
        self.item_name = item_name
        self.purchase_qty = purchase_qty
        # 在庫数 = 在庫数 - 購入数
        # list:drinksからitem_nameを指定してpurchase_qty回リストから削除を繰り返す
        # 変数stockにitem_name対象インスタンスのリストを格納
        stock = self.drinks[item_name]
        for _ in range(purchase_qty):
            stock.pop()
        return len(stock)

    # 売上金額を増やしていくメソッド
    def calculate_sales_amount(self):
        # 売上金額 = 売上金額 + 購入金額
        self.__sales_amount += self.purchase_amount
        return self.__sales_amount

    # Suicaのチャージ残高を減らすメソッド
    def reduce_balance(self):
        # 残高 = 残高 - 購入金額
        self.suica1.balance -= self.purchase_amount
        return self.suica1.balance

    # 購入可能なドリンクのリストを取得するメソッド
    def get_purchase_list(self):
        # 購入可能:在庫が０ではない
        # itemとpurchase_qtyを同時にfor文で回してitemをリストに追加する

        # 省略前
        # purchase_qty_list = []
        # for k, v in self.drinks.items():
        #     if len(v) > 0:
        #         purchase_qty_list.append(k)
        # return purchase_qty_list

        # 省略後(リスト内包表記)
        purchase_qty_list = [k for k, v in self.drinks.items() if len(v) > 0]
        return purchase_qty_list

    # 在庫を追加するメソッド
    # 基準在庫数をを設定して補充メソッドを呼び出した時に基準在庫数になる
    # 基準在庫数はget_stock(item_name)で取得する
    def add_stock(self, item_name):
        base = self.base_stock_num[item_name]
        current = self.get_stock(item_name)
        diff = base - current

        for _ in range(diff):
            self.drinks[item_name].append(Juice(item_name, self.price_list[item_name]))
        return len(self.drinks[item_name])


vm = VM()
vm.suica1.charge(20000)
result = vm.manage_purchase("pepsi", 4)
print(result)
result_stock = vm.add_stock("pepsi")
print(result_stock)
