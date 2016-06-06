using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;

namespace SmartSearch
{
    class test
    {
        private static void Main() {

            Program x = new Program();

            Console.WriteLine("CodigoRespuestaFromMain: "+ x.MultipleSearch() );
            Thread.Sleep(2000);
        }
        
    }
}
