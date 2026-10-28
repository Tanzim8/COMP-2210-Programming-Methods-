using System;
using System.Collections.Generic;

class listAvg
{
    static void Main()
    {
        List<int> numbers = new List<int> {12, 7, 9, 20, 33, 18, 42};
        int total = 0;

        for(int i = 0; i<numbers.Count; i++)
        {
            total += numbers[i];
        }

        double average = (double)total/numbers.Count;

        Console.WriteLine($"The average is: {average}");
    }
}