import sys

"""
def localizaRaizEntre2Inteiros(Y):
    i=0
    for item in Y.keys():
        print (item[i], item[i+1])
"""

def armazenaSinais(esq, dir):
    
    parOrdenado = {}

    for x in range(esq,dir+1):
        parOrdenado[x] = 1.4*x**3 - 3.2*x**2 - 14.8*x + 23.6
    
    for y in parOrdenado.keys():
        print(y)
    
    print()
    for y in parOrdenado.values():
        print(y)
    print()

    #localizaRaizEntre2Inteiros(parOrdenado)

def main():
    try:
        esquerdo = int(sys.argv[1])
        direito = int(sys.argv[2])
        
        armazenaSinais(esquerdo,direito)
    except IndexError:
        print("Use BuscaRaizes.py [limite_esquedo] [limite_direito]")

if __name__ == "__main__":
    main()


        