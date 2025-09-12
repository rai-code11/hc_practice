from .suica import Suica
from .juice import Juice


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
