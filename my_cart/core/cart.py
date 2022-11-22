# Author: zmh0421@hotmail.com
# File: cart
# Created: 2022/11/21
import json
from jinja2 import Template
from typing import Iterable
from .calculator import Calculator, get_calculator
from .product import Product
from .error import ProductNotSupportError, ProductsNullError, CalculatorNotSupportError
from ..settings import TEMPLATE_FILE, DATA_FILE, DEFAULT_EXPENSE_CALCULATORS, DEFAULT_DISCOUNT_CALCULATORS, logger


class Cart:

    def __init__(self,
                 products: Iterable = None,
                 expense_calculators: [Calculator] = None,
                 discount_calculators: [Calculator] = None):
        logger.debug(f"products:{products}")
        logger.debug(f"expense_calculators: {expense_calculators}")
        logger.debug(f"discount_calculators: {discount_calculators}")
  
        self._products = self.__init_products(products)
        
        if expense_calculators is None:
            self._expense_calculators = self.__init_calculator(DEFAULT_EXPENSE_CALCULATORS)
        else:
            self._expense_calculators = self.__init_calculator(expense_calculators)
            
        if discount_calculators is None:
            self._discount_calculators = self.__init_calculator(DEFAULT_DISCOUNT_CALCULATORS)
        else:
            self._discount_calculators = self.__init_calculator(discount_calculators)
        
        logger.debug(self._expense_calculators)
        logger.debug(self._discount_calculators)
        
        self._total_price = 0
    
    @staticmethod
    def __init_products(products: [str]) -> [Product or None]:
        """deserialize products list to product instance list
        ['T-shirt', 'Blouse', ..] -> [Product('T-shirt', ..), Product('Blouse', ..), ..]
        
        Raises:
            ProductNotSupportError: product name not support currently
        """
        # validate products
        if products is None or len(products) == 0:
            raise ProductsNullError
            
        with open(DATA_FILE) as data_file:
            data = json.load(data_file)
            product_data = data["products"]
        try:
            return [Product(product, **product_data[product]) for product in products]
        except KeyError as e:
            raise ProductNotSupportError(product=e.args[0])
    
    @staticmethod
    def __init_calculator(calculators: [str]):
        try:
            return [get_calculator(calculator) for calculator in calculators]
        except AttributeError as e:
            logger.error(str(e))
            raise CalculatorNotSupportError(calculator=e.args[0])
        
    def calculate(self):
        for calculator in self._expense_calculators:
            self._total_price += calculator.calculate(self._products)
        for calculator in self._discount_calculators:
            self._total_price -= calculator.calculate(self._products)
        self._total_price = round(self._total_price, 4)
    
    @property
    def output(self):
        with open(TEMPLATE_FILE) as f:
            template = Template(f.read())
            
        return template.render(expense_calculators=self._expense_calculators,
                               discount_calculators=self._discount_calculators,
                               total_price=self._total_price)
    @property
    def total_price(self):
        return self._total_price
        
        
@logger.catch()
def create_cart(products) -> (bool, str):
    try:
        cart = Cart(products)
        cart.calculate()
        print(cart.output)
        return True, None
    except Exception as e:
        logger.error(str(e))
        return False, e.with_traceback()
