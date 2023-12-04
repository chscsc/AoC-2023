package chscsc.aoc;

import chscsc.aoc.days.Day2;

import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.ArrayList;
import java.util.List;
import java.util.Scanner;

public class Main {
    public static void main(String[] args) throws FileNotFoundException {
        List<String> lines = new ArrayList<>();

        Scanner scanner = new Scanner(new FileReader("input.txt"));
        while (scanner.hasNextLine()) {
            lines.add(scanner.nextLine().trim());
        }

        Solution day = new Day2();

        List<String> solutions = day.solve(lines);

        for(int partNumber = 0; partNumber < day.getClass().getAnnotation(SolutionData.class).parts().length; partNumber++) {
            System.out.println("Part " + (partNumber + 1) + ": " + solutions.get(partNumber));
        }
    }
}
