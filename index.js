const fs = require("fs");

const fileName = "input.txt";

const inputContents = fs.readFileSync(fileName, "utf-8");

// Answer vars
let sum1 = 0,
  sum2 = 0;

// Loop through every line
inputContents.split(/\r?\n/).forEach((line) => {
  // Remove non-numbers from the line.
  const numbersOnly = line.replace(/[^0-9]/g, "");

  // Sometimes a line will only have letters.
  if (numbersOnly.length == 0) return;

  // Get the first and last number as a number.
  const n = parseInt(
    numbersOnly.charAt(0) + numbersOnly.charAt(numbersOnly.length - 1),
    10
  );

  // Add it to our answer
  sum1 += n;
});

console.log("Day 1 Part 1 = " + sum1);

// A list of every text-form of every digit.
const digits = [
  ["one", 1],
  ["two", 2],
  ["three", 3],
  ["four", 4],
  ["five", 5],
  ["six", 6],
  ["seven", 7],
  ["eight", 8],
  ["nine", 9],
];

// Loop through input line by line
inputContents.split(/\r?\n/).forEach((line) => {
  let updatedLine = ""; // Maintain an 'updated line', which contains the numbers we find, both text and digit.

  // Loop through every character in the line with an index.
  for (let i = 0; i < line.length; i++) {
    // Add normal numbers to updated line
    if (/[0-9]/.test(line.charAt(i))) {
      updatedLine += line.charAt(i);
    }

    // Try every digit, and if the substring from our index starts with the text-digit append it to the updated line.
    digits.forEach((digit) => {
      if (line.substring(i).startsWith(digit[0])) {
        updatedLine += digit[1];
      }
    });
  }

  // Parse first and last.
  const n = parseInt(
    updatedLine.charAt(0) + updatedLine.charAt(updatedLine.length - 1),
    10
  );

  // Add it to the solution.
  sum2 += n;
});

console.log("Day 1 Part 2 = " + sum2);