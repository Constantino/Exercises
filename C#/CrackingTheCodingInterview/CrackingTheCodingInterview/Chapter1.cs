using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace CrackingTheCodingInterview
{
    class Chapter1
    {
        static void MultipleDeclarationFor() {
            for (int i = 0, j = 0; i < 5; i++, j = j + 2)
            {
                Console.WriteLine("i: " + i + " j: " + j);
            }

            Console.Read();
        }

        static int Factorial(int n) {
            return n == 0 ? 1 : n * Factorial(n - 1);
        }
        
        static int Fibo(int n) {
            int r = n == 0 ? 0 : n == 1 ? 1 : Fibo(n-2) + Fibo(n-1);
            
            return r;
        }

        static int Fibonacci(int n) {
            
            int f0 = 0;
            int f1 = 1;
            int fx = 0;

            for (int i=0; i <= n; i++) {
                fx = i == 0 ? f0 : (i == 1) ? f1 :( f0 + f1);
                if (i!=0 && i!=1)
                {
                    f0 = f1;
                    f1 = fx;
                }     
            }

            return fx;
        }

        static void TestingFibo()
        {
            int n = 6;
            DateTime StartTime = DateTime.Now;
            int v = Fibonacci(n);
            Console.WriteLine("Fibonacci type 1, CPU(s): " + (DateTime.Now - StartTime).Milliseconds);

            DateTime StartTime2 = DateTime.Now;
            for (int i = 0; i <= n; i++)
            {
                v = Fibo(i);
                //Console.WriteLine("fibonacci(" + i + ") = " +v);

            }
            Console.WriteLine("Fibonacci type 2, CPU(s): " + (DateTime.Now - StartTime2).Milliseconds);

            Console.ReadLine();
        }

        static void TestingFactorial() {
            int n = 4;
            Console.WriteLine("factorial(" + n + ") = " + Factorial(n));
            Console.Read();

        }

        static bool HasUnique(string MyString) {
            List<char> CharList = new List<char>();
            foreach (var Character in MyString)
            {
                if (CharList.Contains(Character))
                {
                    return false;
                }
                CharList.Add(Character);
            }

            return true;
        }

        static bool HasUnique2(string MyString) {
            for (int i = 0; i < MyString.Length; i++)
            {
                for (int j = 0; j < MyString.Length; j++)
                {
                    if (MyString[i] == MyString[j] && i != j)
                    {
                        return false;
                    }
                }
            }
            return true;
        }

        static void TestHasUnique() {
            Console.WriteLine(HasUnique("Consta"));
            Console.Read();
        }

        static void TestHasUnique2()
        {
            Console.WriteLine(HasUnique2("consta"));
            Console.ReadLine();

        }

        static bool IsPermutation(string String1, string String2)
        {
            if (String1.Length != String2.Length)
            {
                return false;
            }

            bool IsIn;

            for (int i = 0; i < String1.Length; i++)
            {
                IsIn = false;
                for (int j = 0; j < String2.Length; j++)
                {
                    if (String1[i] == String2[j])
                    {
                        IsIn = true;
                    }
                }
                if (!IsIn)
                {
                    return false;
                }
            }

            return true;
        }

        static void TestIsPermutation()
        {
            Console.WriteLine(IsPermutation("consta","cnsota"));
            Console.WriteLine(IsPermutation("constan", "consta"));
            Console.WriteLine(IsPermutation("consta", "consts"));
            Console.Read();

        }

        static string URLify(string InputString) {
            string OutputString = String.Empty;
            InputString = InputString.Trim();
            foreach (var ch in InputString)
            {

                OutputString += String.IsNullOrWhiteSpace(ch.ToString()) ? "%20" : ch.ToString();
                
            }

            return OutputString;
        }
        static void TestURLify()
        {
            Console.WriteLine(URLify("Jon Targaryen Stark   "));
            Console.Read();

        }

        static bool PalindromPermutation(string MyString) {



            return true;
        }

        static void Main(string[] args) {
            //TestingFibo();
            //TestHasUnique();
            //TestHasUnique2();
            //TestIsPermutation();
            TestURLify();
        }
    }
}
