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
        with self.assertRaises(CalculatorNotSupportError) as e:
            Cart(['T-shirt'], expense_calculators=['a'])

    def test_invalid_discount_calculators(self):
        with self.assertRaises(CalculatorNotSupportError) as _:
            Cart(['T-shirt'], discount_calculators=['a'])

    def test_total_price(self):
        cart = Cart(['T-shirt'])
        cart.calculate()
        self.assertEqual(39.3286, cart.total_price)
        
    def test_create_cart(self):

        create_cart(["T-shirt", "Blouse", "Pants", "Sweatpants", "Jacket", "Shoes"])
        self.assertTrue(True)
        
    def test_create_cart_error(self):
        create_cart(["aa"])
        
    
    
if __name__ == '__main__':
    unittest.main()
