from .vending_machine import VM

vm = VM()
vm.suica1.charge(20000)
result = vm.manage_purchase("irohasu", 4)
print(result)
