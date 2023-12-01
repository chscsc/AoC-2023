import { Solution } from "../Solution";

export class Day1 extends Solution {
  constructor() {
    super();
  }

  solve1(lines) {
    let sum = 0;

    for (let line of lines) {
      // Remove non-numbers
      line = line.replace(/[^0-9]*/g, "");

      // Some lines only have letters.
      // This skips those.
      if (line.length == 0) continue;

      // Find the first and last character in our new string
      const first = line.charAt(0),
        last = line.charAt(line.length - 1);

      // Add to the sum. 10 means that the number is base-10.
      sum += parseInt(first + last, 10);
    }

    return sum;
  }

  solve2(lines) {
    let sum = 0;

    for (let line of lines) {
      // Replace text form of digits with real numbers,
      // and add the first and last letter.
      // This fixes the problem of overlapping words.
      line = line
        // Numbers
        .replace("one", "o1e")
        .replace("two", "t20")
        .replace("three", "t3e")
        .replace("four", "f4r")
        .replace("five", "f5e")
        .replace("six", "s6x")
        .replace("seven", "s7n")
        .replace("eight", "e8t")
        .replace("nine", "n9e")

        // Non-numbers that are left over
        .replace(/[^0-9]*/g, "");

      // Skip blank lines- actually not needed now.
      if (line.length == 0) continue;

      // Find the first and last digits in the new line.
      const first = line.charAt(0),
        last = line.charAt(line.length - 1);

      // Add to the sum.
      // 10 is the base of the number,
      // which is always 10.
      sum += parseInt(first + last, 10);
    }

    return sum;
  }
}