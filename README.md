# Requirements
This program is based on Python 3.7, so I would like to recommend you using python 3.7+
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

![architecture](https://user-images.githubusercontent.com/49432155/203371632-7c0fbc58-8fc4-4630-9b09-cd566ce607c6.png)