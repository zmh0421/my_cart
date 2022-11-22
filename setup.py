# Author: zmh0421@hotmail.com
# File: setup.py
# Created: 2022/11/22
from setuptools import setup, find_packages

setup(
    name='my_cart',
    version='0.1.0',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'Click',
        'Jinja2',
        'loguru'
    ],
    entry_points={
        'console_scripts': [
            'createCart = cli:create_cart',
        ],
    },
)