using System;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;
using System.Linq;

public class P2
{
	static Regex w_and_digits_rx = new(@"(?=((one|two|three|four|five|six|seven|eight|nine)|\d))", RegexOptions.Compiled | RegexOptions.IgnoreCase);
	static Regex digits_rx = new(@"\d", RegexOptions.Compiled);

	static List<String> numbers = new List<String>()
	{
		"one", "two", "three", "four", "five", "six", "seven", "eight", "nine"
	};

	public static void Run(string inputpath)
	{
		string[] lines = File.ReadAllLines(inputpath);

		int sum = 0;

		foreach (string line in lines)
		{
			List<int> digits = new();
			foreach (Match m in w_and_digits_rx.Matches(line))
			{
				string token = m.Groups[1].ToString();
				if (digits_rx.IsMatch(token))
					digits.Add(int.Parse(token));
				else
					digits.Add(numbers.IndexOf(m.Groups[1].ToString()) + 1);
			}
			// IEnumerable<int> digits =
			// 	from m in w_and_digits_rx.Matches(line)
			// 	select (digits_rx.IsMatch(m.Groups[1].ToString()) ? int.Parse(m.Groups[1].ToString()) : numbers.IndexOf(m.Groups[1].ToString()) + 1);
			sum += digits.First() * 10 + digits.Last();
		}

		Console.WriteLine($"Part Two: {sum}");

		sum = 0;
	}
}