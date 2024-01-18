import sys
import math

def main():
    try:
        equacao = sys.argv[1]
        inicio = int(sys.argv[2])
        fim = int(sys.argv[3])
        precisao = int(sys.argv[4])
        
        imprime_raizes(equacao, inicio, fim, precisao)
    except IndexError:
        print("  Use [equacao] [inicio] [fim] [precisao_casas_decimais]")
        print("  Exemplo")
        print("    Dicotomia.py 1.4*x**3-3.2*x**2-14.8*x+23.6 1 2 5")

def calculaIteracao(x, eq):
    return eval(eq)


def imprime_raizes(eq, inicio, fim, precisao):
    iteracao = 0
    erro = 0
    media = 0

    print(f"{"#":>3} {"lim. inferior":>20} {"lim. superior":>20} {"média(x)":>20} {"f(inferior)":>25} {"f(media)":>25} {"f(superior)":>25} {"erro":>25}" )
    while (fim-inicio)/2 > 0.5*math.pow(10, -precisao):
        erro = (fim-inicio)/2
        media = (inicio+fim)/2
        y_inicio = calculaIteracao(inicio, eq)
        y_fim = calculaIteracao(fim, eq)
        y_media = calculaIteracao(media, eq)
        print(f"{iteracao:>3} {inicio:>20} {fim:>20} {media:>20} {y_inicio:>25} {y_media:>25} {y_fim:>25} {erro:>25}")
        if (y_inicio > 0 and y_media < 0) or (y_inicio < 0 and y_media > 0):
            fim = media
        if (y_fim > 0 and y_media < 0) or (y_fim < 0 and y_media > 0):
            inicio = media

        iteracao+=1

    print(f'Para x={media} => {eq} = {calculaIteracao(media, eq)}')

if __name__ == "__main__":
    main()