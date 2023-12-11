import java.io.FileNotFoundException;
import java.io.FileReader;
import java.util.*;

/*
 * Java Advent of Code Template for day 2 live walkthrough
 * 
 * @author Michael McCright
 */
public class Main {
  public static void main(String[] args) throws FileNotFoundException {
    // Read input into a List<String>
    final List<String> lines = readInput("input.txt");

    HashMap<String, Integer> guess = new HashMap<>();

    guess.put("red", 12);
    guess.put("green", 13);
    guess.put("blue", 14);

    long total = 0;

    for (int i = 0; i < lines.size(); i++) {
      final int gameId = i + 1;

      String line = lines.get(i);

      line = line.split(": ")[1];

      boolean possible = true;

      for (String reveal : line.split(",|;")) {
        reveal = reveal.trim();

        String[] split = reveal.split(" ");
        int number = Integer.parseInt(split[0]);
        String color = split[1];

        if (number > guess.get(color)) {
          possible = false;
        }
      }

      if (possible) {
        total += gameId;
      }
    }

    System.out.println(total);
  }

  public static List<String> readInput(String fileName) throws FileNotFoundException {
    if (!Arrays.asList("input.txt", "sample.txt").contains(fileName))
      throw new RuntimeException("You mistyped the file name.");

    final List<String> result = new ArrayList<>();
    final Scanner scanner = new Scanner(new FileReader(fileName));

    while (scanner.hasNextLine()) {
      result.add(scanner.nextLine().trim());
    }

    if (result.size() < 5)
      throw new RuntimeException("Expected >= 5 lines of input.");

    // Verify that every line is valid
    result.forEach(line -> {
      if (!line.startsWith("Game ") || (!line.contains("red") && !line.contains("green") && !line.contains("blue"))) {
        throw new RuntimeException("Invalid line! line=" + line);
      }
    });

    return result;
  }
}
