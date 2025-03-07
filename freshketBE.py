class Calculator:
    PRICES = {
        "Red": 50, "Green": 40, "Blue": 30,
        "Yellow": 50, "Pink": 80, "Purple": 90, "Orange": 120, 
        "Black": 500
    }
    BUNDLE_DISCOUNT_ITEMS = {"Orange", "Pink", "Green", "Black"}
    MEMBER_DISCOUNT = 0.90  # 10% off for members
    BUNDLE_DISCOUNT = 0.95  # 5% off per bundle
    SET_DISCOUNT = 0.9 # 10% off for sets

    def __init__(self, is_member=False):
        self.is_member = is_member
        self.is_set_discount = False

    def calculate_discount_item(self, item, quantity):
        discount_pairs =  quantity // 2
        price_per_item = self.PRICES[item]            
        if discount_pairs > 0:
            remainder_item_calculated = quantity % 2 * price_per_item
            calculated = discount_pairs * price_per_item * 2 * self.BUNDLE_DISCOUNT
            return calculated + remainder_item_calculated
        else: 
            return price_per_item * quantity

    def calculate_total(self, order):
        total = 0
        for item, quantity in order.items():
            print(item, quantity)
            if item in self.PRICES:
                price_per_item = self.PRICES[item]
                if item == "Black" and quantity >= 3:
                    self.is_set_discount = True
                if item in self.BUNDLE_DISCOUNT_ITEMS:
                    if item == "Black" and self.is_set_discount:
                        total += price_per_item * quantity
                    else:
                        total += self.calculate_discount_item(item, quantity)
                else:
                    total += price_per_item * quantity

        if self.is_set_discount:
            total = total * self.SET_DISCOUNT
        # Apply 10% member discount on total
        if self.is_member:
            total = total * self.MEMBER_DISCOUNT

        return round(total, 2)

# ---- Unit Tests ----
import unittest

class TestCalculator(unittest.TestCase):
    # def test_basic_order(self):
    #     calc = Calculator()
    #     self.assertEqual(calc.calculate_total({"Red": 1, "Green": 1}), 90)

    # def test_member_discount(self):
    #     calc = Calculator(is_member=True)
    #     self.assertEqual(calc.calculate_total({"Red": 1, "Green": 1}), 81) 

    # def test_bundle_discount(self):
    #     calc = Calculator()
    #     self.assertEqual(calc.calculate_total({"Orange": 2}), 228)  

    # def test_complex_order(self):
    #     calc = Calculator(is_member=True)
    #     order = {"Red": 2, "Green": 4, "Pink": 2, "Orange": 5}
    #     self.assertEqual(calc.calculate_total(order), 882)
    
    # def test_large_order(self):
    #     calc = Calculator()
    #     order = {"Red": 100, "Green": 100, "Blue": 100, "Pink": 100, "Orange": 100}
    #     self.assertEqual(calc.calculate_total(order), 30800)
    
    # def test_large_order_member(self):
    #     calc = Calculator(is_member=True)
    #     order = {"Red": 100, "Green": 100, "Blue": 100, "Pink": 100, "Orange": 100}
    #     self.assertEqual(calc.calculate_total(order), 27720)
    
    # def test_all_items_order(self):
    #     calc = Calculator()
    #     order = {"Red": 1, "Green": 1, "Blue": 1, "Yellow": 1, "Pink": 1, "Purple": 1, "Orange": 1}
    #     self.assertEqual(calc.calculate_total(order), 460)
    
    # Fail condition test cases -> If the order contains an item that is not in the price list, the function should return -1
    # def test_fail_order(self):
    #     calc = Calculator(is_member=True)
    #     order = {"Black": 1}
    #     self.assertEqual(calc.calculate_total(order), -1)
    
    # def test_skip(self):
    #     calc = Calculator()
    #     order = {"Black": 1, "Teal": 100}
    #     self.assertEqual(calc.calculate_total(order), 500)

    def test_black_set(self):
        calc = Calculator()
        order = {"Black": 1}
        self.assertEqual(calc.calculate_total(order), 500)
    
    def test_black_set2(self):
        calc = Calculator()
        order = {"Black": 3}
        self.assertEqual(calc.calculate_total(order), 1350)
    
    def test_black_set3(self):
        calc = Calculator()
        order = {"Black": 1, "Black": 2} # Black : [1, 2]
        self.assertEqual(calc.calculate_total(order), 1350)

if __name__ == "__main__":
    unittest.main()

# Challenge 1 
# If the item does not exist skip it and still calculate the total

# Challenge 2
# เพิ่ม black sets = 500 per set, ถ้าสั่ง black sets >= 3 ขึ้นไป จะลด 10% จากยอด total

# [item][quantity]