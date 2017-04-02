class CalculadoraImposto:
    def __init__(self, aliquota=0, *args, **kwargs):
        self.aliquota = aliquota

    def calcula_imposto(self, funcionario):
        return funcionario.salario * self.aliquota

class Funcionario:
    def __init__(self, salario, *args, **kwargs):
        self.salario = salario

        if self.salario <= 1710.78:
            calculadora = CalculadoraImposto(aliquota = 0)
        elif self.salario > 1710.78 and self.salario <= 2563.91:
            calculadora = CalculadoraImposto(aliquota = 0.075)
        elif self.salario > 2563.91 and self.salario <= 3418.59:
            calculadora = CalculadoraImposto(aliquota = 0.15)
        elif self.salario > 3418.60 and self.salario <= 4271.59:
            calculadora = CalculadoraImposto(aliquota = 0.225)
        else:
            calculadora = CalculadoraImposto(aliquota = 0.275)

        self.calculadora = calculadora

    def calcula_imposto(self):
        return self.calculadora.calcula_imposto(self)
