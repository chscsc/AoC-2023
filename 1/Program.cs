class Day1
{
	public static void Main(string[] argv)
	{
		if (argv.Length < 1)
		{
			Console.WriteLine("Error, input must be specified");
			return;
		}

		P1Functional.Run(argv[0]);
		P1LINQ.Run(argv[0]);
		P2.Run(argv[0]);
	}
}