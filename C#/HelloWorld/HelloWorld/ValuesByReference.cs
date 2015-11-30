using System;

public class ValueByReference
{
	public ValueByReference()
	{
        int x = 5;
        DoSomething();
        Console.WriteLine("x = ", x);
	}
}
