﻿using System;

namespace Dicotomia
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                double esquerdo = Convert.ToDouble(args[0]);
                double direito = Convert.ToDouble(args[1]);
                double precisao = Convert.ToDouble(args[2]);

                ImprimeIteracoes(esquerdo, direito, precisao);
            }
            catch
            {
                Console.WriteLine("           Use Dicotomia [limite_esquerdo] [limite_direito] [precisão]");
                Console.WriteLine("           limite_esquerdo e limite_direito representam o intervalo encontrado pelo programa BuscaRaizes.");
                Console.WriteLine("           precisão é um inteiro que informa a quantidade de casas decimais corretas.");
            }
        }

        static void ImprimeIteracoes(double a, double b, double pre)
        {
            int iteracao = 0;
            double erro = 0;
            double media = 0;

            Console.WriteLine("{0,3} {1,20} {2,20} {3,20} {4,25} {5,25} {6,25} {7,20}", "#", "Lim. esq.", "Lim. dir.", "Média lim.", "f(Lim. esq.)", "f(Média lim)", "f(Lim. dir.)", "Erro");

            while ((b - a) / 2 > 0.5 * Math.Pow(10, -pre))
            {
                erro = (b - a) / 2;
                media = (a + b) / 2;
                double ya = Math.Pow(a, 3) - 6 * a - 2; // Equação
                double yb = Math.Pow(b, 3) - 6 * b - 2; // Equação
                double yMedia = Math.Pow(media, 3) - 6 * media - 2; // Equação
                Console.WriteLine("{0,3} {1,20} {2,20} {3,20} {4,25} {5,25} {6,25} {7,20}", iteracao, a, b, media, ya, yMedia, yb, erro);
                if ((ya > 0 && yMedia < 0) || (ya < 0 && yMedia > 0))
                    b = media;

                if ((yb > 0 && yMedia < 0) || (yb < 0 && yMedia > 0))
                    a = media;

                iteracao++;
            }

            Console.Write("\nPara x = " + media + " => x^3 - 6x - 2 = "); // Equação
            Console.WriteLine(Math.Pow(media, 3) - 6 * media - 2);
        }
    }
}
