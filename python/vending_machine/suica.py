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
        return f"ユーザー{self.user_id}の残高は{self.__balance}円です"
