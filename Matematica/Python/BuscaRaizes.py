import sys

def main():
    try:
        equacao = sys.argv[1]
        esquerdo = int(sys.argv[2])
        direito = int(sys.argv[3])
        
        localizaRaizes(equacao,esquerdo,direito)
    except IndexError:
        print("  Use BuscaRaizes.py [equacao] [limite_esquerdo] [limite_direito] ")
        print("  Exemplo:")
        print("     BuscaRaizes.py 1.4*x**3-3.2*x**2-14.8*x+23.6 -10 10")

def localizaRaizes(eq, esq, dir):
    parOrdenado = []

    for x in range(esq,dir+1):
        parOrdenado.append(eval(eq))

    print('Há raizes entre os valores:')
    i=0
    while i < len(parOrdenado)-1:
        if float(parOrdenado[i]) > 0 and float(parOrdenado[i+1]) < 0 or parOrdenado[i] < 0 and parOrdenado[i+1] > 0:
            print(f"{esq};{esq+1}")
        i+=1
        esq+=1

if __name__ == "__main__":
    main()


        