OPERADORES = ('+', '-', '*', '/')

class CalculadoraModel:
    def __init__(self, *args, **kwargs):
        self.operandos = []

    def adicionar_operando(self, operando):
        self.operandos.append(operando)

    def adicionar(self):
        self.operandos.append(self.operandos.pop() + self.operandos.pop())

    def subtrair(self):
        segundo_operando = self.operandos.pop()
        primeiro_operando = self.operandos.pop()
        self.operandos.append(primeiro_operando - segundo_operando)

    def multiplicar(self):
        self.operandos.append(self.operandos.pop() * self.operandos.pop())

    def dividir(self):
        segundo_operando = self.operandos.pop()
        primeiro_operando = self.operandos.pop()
        self.operandos.append(primeiro_operando / segundo_operando)

    @property
    def resultado(self):
        return self.operandos[0]

class CalculadoraController:
    def __init__(self, view, *args, **kwargs):
        self.view = view
        self.model = CalculadoraModel()

    def calcular(self):
        for fragmento in self.view.input.split():
            if fragmento == OPERADORES[0]:
                self.model.adicionar()
            elif fragmento == OPERADORES[1]:
                self.model.subtrair()
            elif fragmento == OPERADORES[2]:
                self.model.multiplicar()
            elif fragmento == OPERADORES[3]:
                self.model.dividir()
            else:
                self.model.adicionar_operando(float(fragmento))

        return self.model.resultado

class CalculadoraView:
    def __init__(self, input = "", *args, **kwargs):
        self.input = input
        self.controller = CalculadoraController(self)

    def mostrar_resultado(self):
        print self.controller.calcular()
