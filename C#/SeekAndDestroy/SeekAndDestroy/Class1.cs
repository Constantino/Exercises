using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace SmartSearch
{
    class Class1
    {
        public string Clave;
        public int resp = 0;

        public Class1(string C) {
            Clave = C;
        }

        public void SmartSearch() {

            Console.WriteLine("C1 - Searching...");
            Thread.Sleep(2000);
            Console.WriteLine("C1 - Not found");
            resp = 0;
        }
    }
}
