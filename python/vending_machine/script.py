from .vending_machine import VM

vm = VM()
vm.suica1.charge(20000)
result = vm.manage_purchase("pepsi", 4)
print(result)
result_stock = vm.add_stock("pepsi")
print(result_stock)
