import unittest
from imposto_renda import *

class TestImpostoRenda(unittest.TestCase):
    def test_aliquota_tem_que_ser_0_quando_funcionario_recebe_171078(self):
        salario = 1710.78
        funcionario = Funcionario(salario=salario)
        assert funcionario.calcula_imposto() == 0

    def test_aliquota_tem_que_ser_0075_quando_funcionario_recebe_mais_que_171078_e_menos_que_256392(self):
        salario = 2563.91
        funcionario = Funcionario(salario=salario)
        assert funcionario.calcula_imposto() == salario * 0.075

    def test_aliquota_tem_que_ser_015_quando_funcionario_recebe_mais_que_256392_e_menos_que_341860(self):
        salario = 3418.59
        funcionario = Funcionario(salario=salario)
        assert funcionario.calcula_imposto() == salario * 0.15

    def test_aliquota_tem_que_ser_0225_quando_funcionario_recebe_mais_que_341860_e_menos_que_427160(self):
        salario = 4271.59
        funcionario = Funcionario(salario=salario)
        assert funcionario.calcula_imposto() == salario * 0.225

    def test_aliquota_tem_que_ser_0275_quando_funcionario_recebe_mais_que_427159(self):
        salario = 4271.60
        funcionario = Funcionario(salario=salario)
        assert funcionario.calcula_imposto() == salario * 0.275

if __name__ == '__main__':
    unittest.main()
