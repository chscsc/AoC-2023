package chscsc.aoc;

import chscsc.aoc.days.Day1;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        List<String> lines = new ArrayList<>();

        Scanner scanner = new Scanner(new FileReader("sample.txt"));
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine().trim());
        }

        Solution day1 = new Day1();

        List<String> solutions = day1.solve(lines);

        for(int partNumber = 0; partNumber < day1.getClass().getAnnotation(SolutionData.class).parts().length; partNumber++) {
            System.out.println("Day 1 Part " + partNumber + ": " + solutions.get(partNumber));
        }
    }
}
