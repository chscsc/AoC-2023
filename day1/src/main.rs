use std::fs::File;
use std::io;

const NUMBERS: [&str; 9] = [
    "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
];

fn main() {
    let input = io::read_to_string(File::open("./input.txt").expect("Error opening input.txt"))
        .expect("Error reading input.txt");

    let p1: u32 = input
        .lines()
        .map(|l| l.chars().filter(|c| c.is_ascii_digit()).collect::<String>())
        .map(|mut ds| {
            ds.chars().next().unwrap().to_digit(10).unwrap() * 10
                + ds.pop().unwrap().to_digit(10).unwrap()
        })
        .sum();

    let p2: u32 = input
        .lines()
        .map(|l| {
            l.chars()
                .enumerate()
                .filter_map(|(i, c)| {
                    if c.is_ascii_digit() {
                        Some(c.to_digit(10).unwrap())
                    } else {
                        for (i2, n) in NUMBERS.iter().enumerate() {
                            if l[i..].starts_with(n) {
                                return Some(i2 as u32 + 1);
                            }
                        }
                        None
                    }
                })
                .collect::<Vec<_>>()
        })
        .map(|ds| ds.first().unwrap() * 10 + ds.last().unwrap())
        .sum();

    println!("Part One: {p1}");
    println!("Part Two: {p2}");
}
