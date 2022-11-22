# Author: zmh0421@hotmail.com
# File: settings
# Created: 2022/11/21

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
DATA_FILE = SETTINGS_FILE.parent/"core/resources/data.json"

# default values
DEFAULT_EXPENSE_CALCULATORS = ["Subtotal", "Shipping", "VAT"]
DEFAULT_DISCOUNT_CALCULATORS = ["ShoesDiscount", "JacketDiscount", "ShippingDiscount"]
DEFAULT_ITEM_TYPES = ["T-shirt", "Blouse", "Pants", "Sweatpants", "Jacket", "Shoes"]

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
