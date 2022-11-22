# Requirements
This program is based on Python 3.7, so I would like to recommend you using python 3.7+

After cloning the repo, it is better to create a virtual environment
```shell script
# in the project root
python3 -m venv venv
. venv/bin/activate
```

The following commands will be executed in **venv** by default.

# Installation
## Install by setup.py
If you just want to run the program with command line, you can install it with the following command
```shell script
pip install --editable .
```
Then you can run the following command to get the result
```shell script
createCart --product='T-shirt' --product='Blouse' --product='Pants' --product='Shoes' --product='Jacket'
```
And the output shoule be
```shell script
Subtotal: $386.95
Shipping: $110
VAT: $54.173
Discounts:
        10% off shoes: -$7.999
        50% off jacket: -$99.995
        $10 of shipping: -$10
Total: $433.129
```

## Install by pip
If you want to run testcase or run some source code, you can run
```shell script
pip install -r requirements.txt
```
Then you can run
```shell script
python cli.py --product='T-shirt' --product='Blouse' --product='Pants' --product='Shoes' --product='Jacket'
```
It is as same as the command **createCart** above.

Or if you want to run the test cases, you can run
```shell script
coverage run -m unittest discover testcases

# check the coverage for each module
coverage report --omit="*/test*"
```

#Architecture
The architecture would be like as the following picture

![architecture](https://user-images.githubusercontent.com/49432155/203373852-9eba3173-29e8-4873-be88-46c549e076cb.png)

THe file structure would be like this
```shell script
������ README.md
������ cli.py  # command line interface for user
������ my_cart
��?? ������ core
��?? ��?? ������ calculator.py  # calculator module
��?? ��?? ������ cart.py  # cart module
��?? ��?? ������ error.py  # custom exception
��?? ��?? ������ product.py # product module
��?? ��?? ������ resources
��?? ��??     ������ output_template  # for command line output
��?? ������ settings.py  # default(global) settings or config
������ requirements.txt
������ setup.py
������ testcases
    ������ data.json
    ������ test_cart.py
    ������ test_template.py
```

## Modules
All the modules are in the **PROJECT_ROOT/my_cart/core** folder
### Product
Define the product data and the relative data structure
### Calculator
Provide different rules of calculating the price of products
Divided into EXPENSE calculator and DISCOUNT calculator
### Cart
Main logic of the program, it will call functions of Product and Calculator, then generate the result for users. 