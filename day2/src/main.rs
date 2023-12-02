use std::collections::HashMap;
use std::fs::File;
use std::io;

fn main() {
    let ftxt = io::read_to_string(File::open("./input.txt").expect("Error opening input.txt"))
        .expect("Error reading input.txt");
    let input = ftxt
        .lines()
        .map(|l| {
            let mut gs = l.split(": ");
            let gid = gs
                .next()
                .unwrap()
                .split(' ')
                .nth(1)
                .unwrap()
                .parse::<u32>()
                .unwrap();
            let bag = gs
                .next()
                .unwrap()
                .split("; ")
                .map(|rev| {
                    rev.split(", ")
                        .map(|cubes| cubes.split(' ').collect::<Vec<_>>())
                        .map(|cv| (cv[1].to_owned(), cv[0].parse::<u32>().unwrap()))
                        .collect::<HashMap<String, u32>>()
                })
                .collect::<Vec<_>>();

            (gid, bag)
        })
        .collect::<Vec<_>>();

    let maxes = HashMap::from([("red", 12), ("green", 13), ("blue", 14)]);

    let p1: u32 = input
        .iter()
        .filter_map(|(gid, bag)| {
            if (bag.iter().all(|rev| {
                maxes
                    .iter()
                    .all(|(color, max)| rev.get(*color).unwrap_or(&0) <= max)
            })) {
                Some(gid)
            } else {
                None
            }
        })
        .sum();

    println!("Part One: {p1}");

    let p2: u32 = input
        .iter()
        .map(|(_, bag)| {
            maxes
                .keys()
                .map(|color| {
                    bag.iter()
                        .map(|rev| rev.get(*color).unwrap_or(&0))
                        .max()
                        .unwrap()
                })
                .product::<u32>()
        })
        .sum();

    println!("Part Two: {p2}");
}
