# Author: zmh0421@hotmail.com
# File: calculator
# 2022/11/21 created zmh0421@hotmail.com

"""This module contains different strategy of price calculation

It has a abstract class Calculator,
and any other class in this package inherit from Calculator
"""

import abc
import sys
import math
from .product import Product, ItemType
from ..settings import VAT_RATE, SHOE_DISCOUNT, JACKET_DISCOUNT, DECIMAL_PLACES, SHIPPING_RATES, DEFAULT_PRODUCTS


class Calculator(abc.ABC):
    
    def __init__(self):
        self._price = 0  # the price should be added or minus (by callers)
    
    @abc.abstractmethod
    def calculate(self, products: [Product]):
        """calculate the price with different rules
        """
    
    @property
    @abc.abstractmethod
    def name(self):
        """used for output
        """

    @property
    def price(self):
        return round(self._price, DECIMAL_PLACES)


class Subtotal(Calculator):
    
    @property
    def name(self) -> str:
        return "Subtotal"
    
    def calculate(self, products: [Product]) -> float:
        self._price = sum([item.price for item in products])
        return self.price


class Shipping(Calculator):
    
    @property
    def name(self) -> str:
        return "Shipping"
    
    def calculate(self, products: [Product]) -> float:
        # Each country has a shipping rate per 100 grams
        self._price = sum([math.ceil(item.weight * 10) * SHIPPING_RATES[item.shipped_from] for item in products])
        return self.price


class VAT(Calculator):
    """There is a 14% VAT (before discounts) applied to all products, whatever the shipping country is
    """

    @property
    def name(self) -> str:
        return "VAT"
    
    def calculate(self, products: [Product]) -> float:
        self._price = sum([item.price * VAT_RATE for item in products])
        return self.price


class ShoesDiscount(Calculator):
    """Shoes are 10% off.
    """

    @property
    def name(self) -> str:
        return "10% off shoes"
    
    def calculate(self, products: [Product]) -> float:
        self._price = sum([item.price * SHOE_DISCOUNT
                           for item in products
                           if item.type == ItemType.Shoes])
        return self.price


class JacketDiscount(Calculator):
    """Buy any two tops (t-shirt or blouse) and get any jacket at half its price.
    """

    @property
    def name(self) -> str:
        return "50% off jacket"
    
    def calculate(self, products: [Product]) -> float:
        top_count = 0
        jacket_price = 0
        
        for item in products:
            if item.type in [ItemType.TShirt, ItemType.Blouse]:
                top_count += 1
            if item.type == ItemType.Jacket:
                jacket_price += item.price
        
        if top_count >= 2:
            self._price = jacket_price * JACKET_DISCOUNT
        else:
            self._price = 0
        
        return self.price


class ShippingDiscount(Calculator):
    """Buy any two items or more and get a maximum of $10 off shipping fees
    """
    @property
    def name(self) -> str:
        return "$10 of shipping"
    
    def calculate(self, products: [Product]) -> float:
        if len(products) >= 2:
            self._price = min(10, Shipping.calculate(Shipping(), products))
        else:
            self._price = 0
        return self.price


def get_calculator(name: str) -> Calculator:
    return getattr(sys.modules[__name__], name)()

