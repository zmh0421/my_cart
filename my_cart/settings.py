# Author: zmh0421@hotmail.com
# File: settings
# 2022/11/21 created zmh0421@hotmail.com

"""This module contains basic settings of the program and
simulates the settings that the actual business would get from external systems(files).

For simplification, It uses python syntax.
"""

import sys
from pathlib import Path
import loguru

# file path settings
SETTINGS_FILE = Path(__file__).absolute()
TEMPLATE_FILE = SETTINGS_FILE.parent/"core/resources/output_template"

# default values
DEFAULT_EXPENSE_CALCULATORS = ["Subtotal", "Shipping", "VAT"]
DEFAULT_DISCOUNT_CALCULATORS = ["ShoesDiscount", "JacketDiscount", "ShippingDiscount"]
DEFAULT_ITEM_TYPES = ["T-shirt", "Blouse", "Pants", "Sweatpants", "Jacket", "Shoes"]
DEFAULT_PRODUCTS = {
    "T-shirt": {
      "price": 30.99,
      "shipped_from": "US",
      "weight": 0.2
    },
    "Blouse": {
      "price": 10.99,
      "shipped_from": "UK",
      "weight": 0.3
    },
    "Pants": {
      "price": 64.99,
      "shipped_from": "UK",
      "weight": 0.9
    },
    "Sweatpants": {
      "price": 84.99,
      "shipped_from": "CN",
      "weight": 1.1
    },
    "Jacket": {
      "price": 199.99,
      "shipped_from": "US",
      "weight": 2.2
    },
    "Shoes": {
      "price": 79.99,
      "shipped_from": "CN",
      "weight": 1.3
    }
  }

# numeric value settings
VAT_RATE = 0.14  # There is a 14% VAT (before discounts) applied to all products, whatever the shipping country is.
SHOE_DISCOUNT = 0.1  # Shoes are 10% off.
JACKET_DISCOUNT = 0.5  # Buy any two tops (t-shirt or blouse) and get any jacket at half its price.
DECIMAL_PLACES = 4  # For each price
SHIPPING_RATES = {
    "US": 2,
    "UK": 3,
    "CN": 2
}

# logger settings
logger = loguru.logger
logger.remove()
logger.add('logs', level="DEBUG")
logger.add(sys.stdout, level="INFO")
