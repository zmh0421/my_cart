# 2022/11/22 created zmh0421@hotmail.com

import unittest
from my_cart.core.cart import Cart, create_cart
from my_cart.core.error import ProductNotSupportError, CalculatorNotSupportError, ProductsNullError


class CartTestCase(unittest.TestCase):
    def test_invalid_product(self):
        with self.assertRaises(ProductNotSupportError) as _:
            Cart(['T-shirt', 'K'])
            
    def test_null_product(self):
        with self.assertRaises(ProductsNullError) as _:
            Cart([])
        
    def test_none_product(self):
        with self.assertRaises(ProductsNullError) as _:
            Cart(None)
            
    def test_invalid_expense_calculators(self):
        with self.assertRaises(CalculatorNotSupportError) as _:
            Cart(['T-shirt'], expense_calculators=['a'])

    def test_invalid_discount_calculators(self):
        with self.assertRaises(CalculatorNotSupportError) as _:
            Cart(['T-shirt'], discount_calculators=['a'])

    def test_total_price(self):
        cart = Cart(['T-shirt'])
        cart.calculate()
        self.assertEqual(39.3286, cart.total_price)
        
    def test_create_cart(self):
        success, _ = create_cart(["T-shirt", "Blouse", "Pants", "Sweatpants", "Jacket", "Shoes"])
        self.assertTrue(success)
        
    def test_create_cart_error(self):
        success, _ = create_cart(["aa"])
        self.assertFalse(success)

    def test_discount_not_shown(self):
        success, output = create_cart(["T-shirt"])
        self.assertTrue(True, success)
        self.assertNotIn('Discounts', output)

    def test_discount_item_not_shown(self):
        success, output = create_cart(["Shoes"])
        self.assertTrue(True, success)
        self.assertNotIn('50% off jacket', output)
        self.assertNotIn('$10 of shipping', output)
        
        
if __name__ == '__main__':
    unittest.main()
