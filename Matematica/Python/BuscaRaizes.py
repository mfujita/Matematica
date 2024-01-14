import sys

def localizaRaizes(esq, dir, eq):
    parOrdenado = []

    for x in range(esq,dir+1):
        parOrdenado.append(1.4*x**3-3.2*x**2-14.8*x+23.6)

    print('Há raizes entre os valores:')
    i=0
    while i < len(parOrdenado)-1:
        #print(parOrdenado[i])
        if float(parOrdenado[i]) > 0 and float(parOrdenado[i+1]) < 0 or parOrdenado[i] < 0 and parOrdenado[i+1] > 0:
            print(f"{esq};{esq+1}")
        i+=1
        esq+=1

def main():
    try:
        esquerdo = int(sys.argv[1])
        direito = int(sys.argv[2])
        equacao = sys.argv[3]
        
        localizaRaizes(esquerdo,direito,equacao)
    except IndexError:
        print("Use BuscaRaizes.py [limite_esquedo] [limite_direito] [equacao]")
        print("Exemplo:")
        print("BuscaRaizes.py -10 10 1.4*x**3-3.2*x**2-14.8*x+23.6")

if __name__ == "__main__":
    main()


        