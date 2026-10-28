using System;
using System.Collections.Generic;

class LetterCount
{
    static void Main()
    {
        Console.WriteLine("Enter First name: ");
        string fName = Console.ReadLine();
        // Console.WriteLine(fName);

        Console.WriteLine("Enter Last name: ");
        string lName = Console.ReadLine();

        Console.WriteLine("Enter Std ID: ");
        string stdID = Console.ReadLine();

        Console.WriteLine("Enter Birth year: ");
        string birthyear = Console.ReadLine();

        Console.WriteLine("Enter birth country: ");
        string birthCountry = Console.ReadLine();

        string fullInfo = String.Concat(fName,lName,stdID,birthyear,birthCountry);

        Console.WriteLine(fullInfo);

        int letterCount = 0;
        for(int i = 0; i<fullInfo.Length; i++)
        {
            if(!char.IsDigit(fullInfo[i])){
                letterCount+=1;
            }
        }
        Console.WriteLine($"Total letters: {letterCount}");
    }
}