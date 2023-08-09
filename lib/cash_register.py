#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0, total=0, items=[]):
        self.discount = discount
        self.total = total
        self.items = []
    def add_item(self, title, price, quantity=1):
        while quantity > 0:
            self.items.append(title)
            self.total += price
            self.last_price = price
            quantity -= 1
    def apply_discount(self):
        if self.discount != 0:
            self.total -= self.total * (self.discount / 100)
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")
    def void_last_transaction(self):
        last_item = self.items[-1]
        del self.items[-1]
        self.total -= self.last_price
        while self.items[-1] == last_item:
            del self.items[-1]
            self.total -= self.last_price
        print(self.total)
        
