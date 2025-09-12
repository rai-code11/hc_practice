from .vending_machine import VendingMachine
from .suica import Suica

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
