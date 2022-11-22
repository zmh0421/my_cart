# Author: zmh0421@hotmail.com
# File: error
# Created: 2022/11/22

"""Custom Exception module
NotSupportError: Base exception including the situation that some value from caller are not supported yet
    ProductNotSupportError: The type of product is not supported
    ExpenseCalculatorNotSupportError: The type of expense calculator is not supported
    DiscountCalculatorNotSupportError: The type of discount calculator is not supported

NullError: Base exception when some parameter is Null(make no sense) and cannot move forward

"""

from ..settings import DEFAULT_ITEM_TYPES, DEFAULT_EXPENSE_CALCULATORS, DEFAULT_DISCOUNT_CALCULATORS


class NotSupportError(Exception):
    def __init__(self, item, range_item):
        super().__init__(f"{item} not in {range_item} range")
        
        
class NullError(Exception):
    def __init__(self, name):
        super().__init__(f"{name} is Null, the process can not move forward")


class ProductNotSupportError(NotSupportError):
    def __init__(self, product):
        super().__init__(f"Product '{product}'", DEFAULT_ITEM_TYPES)
        
        
class CalculatorNotSupportError(NotSupportError):
    def __init__(self, calculator):
        super().__init__(calculator, DEFAULT_EXPENSE_CALCULATORS+DEFAULT_DISCOUNT_CALCULATORS)

        
class ProductsNullError(NullError):
    def __init__(self):
        super().__init__("Products")
