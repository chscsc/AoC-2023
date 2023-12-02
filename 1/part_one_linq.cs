using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

public class P1LINQ
{
    static Regex digits_rx = new(@"\d", RegexOptions.Compiled);

    public static void Run(string inputpath)
    {
        string[] lines = File.ReadAllLines(inputpath);

        int sum = 0;

        foreach (string line in lines)
        {
            IEnumerable<int> digits =
                from chr in digits_rx.Matches(line)
                select int.Parse(chr.Value);

            sum += digits.First() * 10 + digits.Last();
        }

        Console.WriteLine($"Part One (LINQ): {sum}");

        sum = 0;
    }
}