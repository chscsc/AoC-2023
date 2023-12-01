import { Day1 } from "./days/Day1";

/**
 * This factory can give you solutions.
 * It also has a method which returns an array
 * of solved problems.
 */
export class SolutionProvider {
  getSolution(day) {
    switch (day) {
      case 1:
        return new Day1();

      default:
        return undefined;
    }
  }

  supportedDays() {
    let days = [];

    for (let day = 0; day <= 25; day++) {
      if (this.getSolution(day, 1) != undefined) {
        days.push(day);
      }
    }

    return days;
  }
}