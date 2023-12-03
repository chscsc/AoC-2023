using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

Regex number_rx = new(@"\d+", RegexOptions.Compiled);

string[] lines = File.ReadAllLines("./input.txt");


Dictionary<(int, int), char> symbols = new();
for (int row = 0; row < lines.Length; ++row)
{
	for (int col = 0; col < lines[row].Length; ++col)
	{
		if (!"1234567890.".Contains(lines[row][col])) symbols.Add((row, col), lines[row][col]);
	}
}

var numbers = new List<(int row, int left, int len)>();
for (int row = 0; row < lines.Length; ++row)
{
	var matches = number_rx.Matches(lines[row]);
	foreach (Match m in matches)
	{
		numbers.Add((row, m.Index, m.Length));
	}
}

var numbers_with_bounds = new List<(int number, List<(int, int)> surrounds)>();
foreach ((int row, int left, int len) in numbers)
{
	var surrounds = new List<(int, int)>();
	foreach (int ro in new int[] { -1, 0, 1 })
	{
		for (int col = left - 1; col <= (left + len); ++col)
		{
			surrounds.Add((row + ro, col));
		}
	}
	numbers_with_bounds.Add((int.Parse(lines[row].Substring(left, len)), surrounds));
}

int p1 = numbers_with_bounds
	.Select(n => n.surrounds.Any(bc => symbols.ContainsKey(bc)) ? n.number : 0) // Select all numbers that overlap at least one symbol
	.Sum(); // Sum it

Console.WriteLine($"Part One: {p1}");

// Find the coordinates of all asterisks
List<(int, int)> asterisks = symbols.Where(e => e.Value == '*').Select(e => e.Key).ToList();

int p2 = asterisks
	.Select(e => numbers_with_bounds.Where(n => n.surrounds.Contains(e)).ToArray()) // Select numbers that overlap this asterisk
	.Select(nsurr => (nsurr.Length == 2) ? nsurr[0].number * nsurr[1].number : 0) // If there are two overlapping numbers, take the product, otherwise zero
	.Sum(); // Sum it

Console.WriteLine($"Part Two {p2}");