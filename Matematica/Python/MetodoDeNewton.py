import sys
import math

class Funcoes:
    def __init__(self, pri, der1, der2):
        self.primitiva = pri
        self.derivada1a = der1
        self.derivada2a = der2
    def retorna_primitiva(self):
        return self.primitiva
    def retorna_derivada1a(self):
        return self.derivada1a
    def retorna_derivada2a(self):
        return self.derivada2a
    
    def calcula_funcao_primitiva(self,x):
        return eval(self.primitiva(x))

    def calcula_derivada1a(self, x):
        return eval(self.derivada1a(x))

    def calcula_derivada2a(self,x):
        return eval(self.derivada2a(x))
    


def main():
    try:
        primitiva = sys.argv[1]
        derivada1a = sys.argv[2]
        derivada2a = sys.argv[3]
        inicio = int(sys.argv[4])
        fim = int(sys.argv[5])
        precisao = int(sys.argv[6])

        funcoes = Funcoes(primitiva, derivada1a, derivada2a)
        print(funcoes.retorna_primitiva())
        print(funcoes.retorna_derivada1a())
        print(funcoes.retorna_derivada2a())

        x0 = escolher_ponto_partida(inicio, fim, funcoes)
        x_proximo = 0
        if x0 == inicio:
            x_proximo = fim
        else:
            x_proximo = inicio
        calcula_raiz(x0, x_proximo, precisao, funcoes)
    except IndexError:
        print("  Use [equacao_primitiva] [derivada_1a] [derivada_2a] [inicio] [fim] [precisao]")
        print("  Exemplo")
        print("     MetodoDeNewton.py 1.4*x**3-3.2*x**2-14.8*x+23.6 4.2*x**2-6.4*x-14.8 8.4*x-6.4 1 2 5")


def calcula_erro(x0, x1):
    return abs(x0-x1)


def escolher_ponto_partida(esquerdo, direito, funcoes):
    ponto_partida = esquerdo
    if funcoes.calcula_funcao_primitiva(esquerdo) * funcoes.calcula_derivada2a(esquerdo) > 0:
        ponto_partida = esquerdo
    elif funcoes.calcula_funcao_primitiva(direito) * funcoes.calcula_derivada2a(direito) > 0:
        ponto_partida = direito
    return ponto_partida

def calcula_raiz(x0, xn, precisao, funcao):
    xn = 0

    while (True):
        xn = x0 - eval(funcao.retorna_primitiva(x0)/funcao.retorna_derivada1a(x0))
        print(x0, xn, calcula_erro(x0, xn))
        if calcula_erro(x0, xn) < 0.5*math.pow(10, -precisao):
            break
        x0 = xn

    print(f'Para x={xn} => {funcao.retorna_primitiva()} = eval({funcao.calcula_funcao_primitiva(xn)})')


main()
