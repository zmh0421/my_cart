# 2022/11/22 created zmh0421@hotmail.com

from pathlib import Path
import unittest
import jinja2

PROJECT_ROOT = Path(__file__).parent.parent
TEMPLATE_PATH = PROJECT_ROOT/"my_cart/core/resources/output_template"


class TestTemplate(unittest.TestCase):
    def test_output_template_only_total_price(self):
        """Call template module with only total_price.
        Although it is illegal for the business, the module itself will not do the verification
        """
        total_price = 100
        with open(TEMPLATE_PATH) as f:
            template = jinja2.Template(f.read())
            output = template.render(total_price=total_price)
            self.assertEqual("Total: $100", output.strip())
        

if __name__ == '__main__':
    unittest.main()
