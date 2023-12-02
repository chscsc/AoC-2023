using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

public class P1Functional
{
    static Regex digits_rx = new(@"\d", RegexOptions.Compiled);

    public static void Run(string inputpath)
    {
        int sum = File.ReadAllLines(inputpath).Select(l => from chr in digits_rx.Matches(l)
                                                           select int.Parse(chr.Value))
                        .Select(la => la.First() * 10 + la.Last()).Sum();

        Console.WriteLine($"Part One (Functional): {sum}");

        sum = 0;
    }
}