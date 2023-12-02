using System.Linq;
using System.Collections.Generic;
using System.IO;
using System.Text.RegularExpressions;

Regex game_rx = new(@"Game (\d+): (.+)", RegexOptions.Compiled);

string[] lines = File.ReadAllLines("./input.txt");

var games = lines
.Select(g => game_rx.Matches(g).ToArray())
.Select(ms => (
	int.Parse(ms[0].Groups[1].Value),
	ms[0].Groups[2].Value.Split("; ")
		.Select(rev => new Dictionary<string, int>(
			rev.Split(", ").Select(s => s.Split(' ').ToArray()).ToDictionary(e => e[1], e => int.Parse(e[0]))
		)
	)
));

Dictionary<string, int> maxcubes = new() {
	{"red", 12},
	{"green", 13},
	{"blue", 14}
};

int p1 = 0;

foreach (var (gid, revs) in games)
{
	bool valid = revs.All(r => maxcubes.All(entry => r.GetValueOrDefault(entry.Key, 0) <= entry.Value));

	if (valid)
		p1 += gid;
}

Console.WriteLine($"Part One: {p1}");

int p2 = 0;
foreach (var (gid, revs) in games)
{
	Dictionary<string, int> maxes = maxcubes.Keys.Select(color =>
		(color, revs.Select(rev => rev.GetValueOrDefault(color, 0)).Max())
	).ToDictionary(e => e.Item1, e => e.Item2);
	p2 += maxes["red"] * maxes["green"] * maxes["blue"];
}

Console.WriteLine($"Part Two: {p2}");