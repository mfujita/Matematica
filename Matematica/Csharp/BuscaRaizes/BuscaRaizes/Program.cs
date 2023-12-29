using System;
using System.Collections.Generic;
using System.Linq;

namespace BuscaRaizes
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                int esquerdo = Convert.ToInt32(args[0]);
                int direito = Convert.ToInt32(args[1]);

                ArmazenaSinais(esquerdo, direito);
            }
            catch
            {
                Console.WriteLine("      Use BuscaRaizes [limite_esquerdo] [limite_direito]");
                Console.WriteLine("      sendo limite_esquerdo e limite_direito números inteiros.");
                Console.WriteLine("      O propósito do programa é analisar as mudanças de sinais indicando a localização de uma raíz real dentro de intervalo.");
            }
        }

        static void ArmazenaSinais(int esq, int dir)
        {
            Dictionary<int, double> parOrdenado = new Dictionary<int, double>();
            for (int x = esq; x < dir; x++)
            {
                parOrdenado.Add(x, 1.4 * Math.Pow(x, 3) - 3.2 * Math.Pow(x, 2) - 14.8 * x + 23.6); // Equação 1,4x^3-3,2x^2-14,8x+23,6
            }

            LocalizaRaizEntre2Inteiros(parOrdenado);
        }

        static void LocalizaRaizEntre2Inteiros(Dictionary<int, double> par)
        {
            for (int i = 0; i < par.Count-1; i++)
            {
                if (par.ElementAt(i).Value > 0 && par.ElementAt(i+1).Value < 0 || par.ElementAt(i).Value < 0 && par.ElementAt(i+1).Value > 0)
                {
                    Console.WriteLine("Raiz entre " + par.ElementAt(i).Key + " e " + par.ElementAt(i+1).Key);
                }
            }
        }
    }
}
