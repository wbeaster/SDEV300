from decimal import Decimal
import unittest
import lab2
import math

class TestLab2(unittest.TestCase):

    #def test_get_yes_no(self):

    
    """
    def test_cosine_leg(self):
        #https://www.onlinemathlearning.com/law-of-cosines.html
        args = (Decimal(8), Decimal(11), Decimal(37))
        answer = Decimal(6.67)
        result = lab2.cosine_leg(args)
        self.assertAlmostEqual(result, answer)
    """

    def test_right_circular_cylindar_column(self):
        radius = 1
        height = 1
        args = radius, height
        answer = Decimal(math.pi * radius ** 2 * height)
        result = lab2.right_circular_cylindar_column(args)
        self.assertAlmostEqual(result, answer)



if __name__ == '__main__':
    unittest.main()
