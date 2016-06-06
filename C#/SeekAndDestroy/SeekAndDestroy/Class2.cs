using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace SmartSearch
{
    class Class2
    {

        public string Clave;
        public int resp = 0;

        public Class2(string C)
        {
            Clave = C;
        }

        public void SmartSearch()
        {

            Console.WriteLine("C2 - Searching...");
            Thread.Sleep(1000);
            Console.WriteLine("C2 - Clave: " + Clave);
            resp = 2;

        }
    }
}
