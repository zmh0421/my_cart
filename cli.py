# Author: zmh0421@hotmail.com
# File: add_cart
# Created: 2022/11/22
import click
from my_cart.core.cart import create_cart as _create_cart


@click.command()
@click.option("--product", help="product you want to add to the cart", multiple=True)
def create_cart(product):
    _create_cart(product)
    
    
if __name__ == "__main__":
    create_cart()