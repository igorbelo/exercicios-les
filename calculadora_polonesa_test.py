import unittest
from calculadora_polonesa import *

class TestCalculadora(unittest.TestCase):
    def test_should_print_result_plus_with_two_operands(self):
        view = CalculadoraView("5 5 +")
        assert view.calcular() == 10

    def test_should_print_result_minus_with_two_operands(self):
        view = CalculadoraView("5 5 -")
        assert view.calcular() == 0

    def test_should_print_result_times_with_two_operands(self):
        view = CalculadoraView("5 5 *")
        assert view.calcular() == 25

    def test_should_print_result_divide_with_two_operands(self):
        view = CalculadoraView("5 5 /")
        assert view.calcular() == 1

    def test_should_print_result_plus_with_three_operands(self):
        view = CalculadoraView("5 5 5 + +")
        assert view.calcular() == 15

    def test_should_print_result_minus_with_three_operands(self):
        view = CalculadoraView("5 5 5 - -")
        assert view.calcular() == 5

    def test_should_print_result_times_with_three_operands(self):
        view = CalculadoraView("5 5 5 * *")
        assert view.calcular() == 125

    def test_should_print_result_divide_and_plus_with_three_operands(self):
        view = CalculadoraView("5 15 5 / +")
        assert view.calcular() == 8

if __name__ == '__main__':
    unittest.main()
