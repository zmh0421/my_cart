# Author: zmh0421@hotmail.com
# File: product
# 2022/11/22 created zmh0421@hotmail.com

from dataclasses import dataclass


@dataclass
class Product:
    __slots__ = ['type', 'price', 'shipped_from', 'weight']
    type: str
    price: float
    shipped_from: str
    weight: float
    
    
class ItemType:
    TShirt = 'T-shirt'
    Blouse = 'Blouse'
    Pants = 'Pants'
    Sweatpants = 'Sweatpants'
    Jacket = 'Jacket'
    Shoes = 'Shoes'
