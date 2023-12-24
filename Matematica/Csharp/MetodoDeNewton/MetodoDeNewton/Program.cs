using System;

namespace MetodoDeNewton
{
    class Program
    {
        static void Main(string[] args)
        {
            try
            {
                double direito = Convert.ToDouble(args[0]);
                double esquerdo = Convert.ToDouble(args[1]);
                double precisao = Convert.ToDouble(args[2]);

                double x0 = EscolherPontoDePartida(esquerdo, direito);
                double x1 = direito == x0 ? esquerdo : x0;
                Calculos(x0, x1, precisao);
            }
            catch
            {
                Console.WriteLine("    Use MetodoDeNewton [limite_esquerdo] [limite_direito] [precisão]");
                Console.WriteLine("    limite_esquerdo e limite_direito representam o intervalo que contém uma raíz");
                Console.WriteLine("    precisão é a quantidade de casas decimais desejada");
            }
        }

        static double FuncaoPrimitiva(double x)
        {
            return Math.Pow(x, 3) - 6 * x + 2;
        }

        static double DerivadaPrimeira(double x)
        {
            return 3 * Math.Pow(x, 2) - 6;
        }

        static double DerivadaSegunda(double x)
        {
            return 6 * x;
        }

        static double Erro1(double x0, double x1)
        {
            return Math.Abs(x0 - x1);
        }

        static double EscolherPontoDePartida(double a, double b)
        {
            double pontoDePartida = a;
            if (FuncaoPrimitiva(a) * DerivadaSegunda(a) > 0)
                pontoDePartida = a;
            else if (FuncaoPrimitiva(b) * DerivadaSegunda(b) > 0)
                pontoDePartida = b;
            return pontoDePartida;
        }

        static void Calculos(double x0, double x1, double n)
        {
            double xn = 0;

            Console.WriteLine("{0,20} {1,25} {2,26}", "x0", "xn", "Erro");
            while (true)
            {
                xn = x0 - FuncaoPrimitiva(x0) / DerivadaPrimeira(x0);
                Console.WriteLine("{0,20} {1,25} {2,26}", x0, xn, Erro1(x0, xn));
                if (Erro1(x0, xn) < 0.5 * Math.Pow(10, -n))
                    break;
                x0 = xn;
            }

            Console.Write("\nPara x = " + xn + " => x^3 - 6x + 2 = "); // Equação
            Console.WriteLine(Math.Pow(xn, 3) - 6 * xn + 2);
        }
    }
}
