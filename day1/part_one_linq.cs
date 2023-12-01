using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

public class Program
{
    static Regex digits_rx = new(@"\d", RegexOptions.Compiled);

    public static void Main()
    {
        String[] lines = File.ReadAllLines("./input.txt");

        int sum = 0;

        foreach (String line in lines)
        {
            IEnumerable<int> digits =
                from chr in digits_rx.Matches(line)
                select int.Parse(chr.Value);

            sum += digits.First() * 10 + digits.Last();
        }

        Console.WriteLine($"Part One: {sum}");

        sum = 0;
    }
}