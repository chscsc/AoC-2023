package chscsc.aoc.days;

import chscsc.aoc.Solution;
import chscsc.aoc.SolutionData;

import java.util.Arrays;
import java.util.HashMap;
import java.util.List;

@SolutionData(day = 2, parts = {1, 2})
public class Day2 implements Solution {

    public String solve1(List<String> lines) {
        HashMap<String, Integer> guess = new HashMap<>();
        guess.put("red", 12);
        guess.put("green", 13);
        guess.put("blue", 14);
        long solution = 0;

        for(int i = 0; i < lines.size(); i++) {
            final int gameNumber = i + 1;

            String line = lines.get(i);

            // Remove 'Game x: '
            line = line.split(": ")[1];

            boolean gamePossible = true;

            for(String reveal : line.split(",|;")) {
                reveal = reveal.trim();

                gamePossible = gamePossible && (Integer.parseInt(reveal.split(" ")[0]) <= guess.get(reveal.split(" ")[1]));
            }

            if(gamePossible) {
                solution += gameNumber;
            }
        }

        return String.valueOf(solution);
    }

    public String solve2(List<String> lines) {
        long sum = 0;

        for(String line : lines) {
            HashMap<String, Integer> minimum = new HashMap<>();

            line = line.split(": ")[1];

            for(String reveal : line.split(",|;")) {
                reveal = reveal.trim();

                final String color = reveal.split(" ")[1];

                final int number = Integer.parseInt(reveal.split(" ")[0]);

                minimum.put(color, Math.max(number, minimum.getOrDefault(color, 0)));

            }
            int power = minimum.getOrDefault("red", 0) * minimum.getOrDefault("green", 0) * minimum.getOrDefault("blue", 0);

            sum += power;
        }

        return String.valueOf(sum);
    }


    @Override
    public List<String> solve(List<String> lines) {
        return Arrays.asList(solve1(lines), solve2(lines));
    }
}
