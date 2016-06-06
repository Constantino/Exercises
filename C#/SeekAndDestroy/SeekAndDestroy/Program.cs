using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Threading;
using System.Timers;

namespace SmartSearch
{
    class Program
    {
        int CodigoRespuesta;
        Class1 c1;
        Class2 c2;

        string Clave = "123";

        Thread s1;
        Thread s2;
        Thread s3;

        bool TimeOut = false;

        System.Timers.Timer TimerClock;
        
        private void Hunter() {

            c1 = new Class1(Clave);
            c2 = new Class2(Clave);

            c1.Clave = Clave;
            c2.Clave = Clave;

            s1 = new Thread(new ThreadStart(c1.SmartSearch));
            s2 = new Thread(new ThreadStart(c2.SmartSearch));
            //s3 = new Thread(new ThreadStart(Hunter));

            s1.Start();
            s2.Start();
            //s3.Start();

        }

        public int MultipleSearch() {

            int resp = -1;
            
            TimerClock = new System.Timers.Timer(5000);
            TimerClock.Elapsed += OnTimedEvent;
            TimerClock.Enabled = true;

            Hunter();

            while (resp < 0 && !TimeOut) {

                if (c1.resp > 0)
                {
                    resp = c1.resp;
                }
                else if (c2.resp > 0)
                {
                    resp = c2.resp;
                }

            }

            CodigoRespuesta = resp;
            Console.WriteLine("CodigoRespuesta: "+CodigoRespuesta+" - Encontrado en Class"+resp);
            s1.Abort();
            s2.Abort();
            //s3.Abort();
            return CodigoRespuesta;
        }

        private void OnTimedEvent(Object source, ElapsedEventArgs e) {
            
            TimeOut = true;
            Console.WriteLine("Timeout...");

        }

    }
}
