package chscsc.aoc.days;

import chscsc.aoc.Solution;
import chscsc.aoc.SolutionData;

import java.util.*;

@SolutionData(day = 1, parts = {1, 2})
public class Day1 implements Solution {

    @Override
    public List<String> solve(List<String> lines) {
        return Arrays.asList(solve1(lines), solve2(lines));
    }

    public String solve1(List<String> lines) {
        long answer = 0;

        for(String line : lines) {

            // Use a regular expression that only matches non-numbers to remove all letters.
            String onlyNumbers = line.replaceAll("[^0-9]*", "");

            // Sometimes removing all letters can make the length equal to zero.
            if(onlyNumbers.length() == 0) continue;

            char firstNumber = onlyNumbers.charAt(0), lastNumber = onlyNumbers.charAt(onlyNumbers.length() - 1);

            answer += (Integer.parseInt(firstNumber + "" + lastNumber));
        }

        return String.valueOf(answer);
    }

    public String solve2(List<String> lines) {
        long answer = 0;

        List<Digit> digits = Arrays.asList(
          new Digit("one", 1),
          new Digit("two", 2),
          new Digit("three", 3),
          new Digit("four", 4),
          new Digit("five", 5),
          new Digit("six", 6),
          new Digit("seven", 7),
          new Digit("eight", 8),
          new Digit("nine", 9)
        );

        for(String line : lines) {
            String digitStr = ""; // Contains all the numbers we find.

            int index = 0; // index of the line

            for(char c : line.toCharArray()) {
                // If it is a digit itself, then just add it.
                if(Character.isDigit(c)) {
                    digitStr += c;
                }

                // Try every digit.
                for(Digit digit : digits) {
                    // If the line from the index starts with the text form of the digit, then it must be there.
                    if(line.substring(index).startsWith(digit.word)) {
                        digitStr += digit.number;
                    }
                }

                // Increment the index to move to the next character.
                index ++;
            }

            answer += Integer.parseInt(digitStr.charAt(0) + "" + digitStr.charAt(digitStr.length() - 1));
        }

        return String.valueOf(answer);
    }

    public static class Digit {
        String word;
        int number;

        public Digit(String word, int number) {
            this.word = word;
            this.number = number;
        }
    }
}
