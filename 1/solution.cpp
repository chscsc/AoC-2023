#include <algorithm>
#include <vector>
#include <string>
#include <iostream>
#include <fstream>
#include <map>
#include <regex>
#include <sstream>

std::map<std::string, std::string> numbers = {
	{"one","o1e"},
	{"two", "t2o"},
	{"three", "t3e"},
	{"four", "f4r"},
	{"five", "f5e"},
	{"six", "s6x"},
	{"seven","s7n"},
	{"eight", "e8t"},
	{"nine", "n9e"},
};

int main() {
	int p1 = 0;
	int p2 = 0;

	std::ifstream input("./input.txt");

	std::string line;
	while (std::getline(input, line)) {
		char fd = 0x00, ld = 0x00;
		for (int i = 0; i < line.length(); ++i) {
			if ((line[i] >= '0') and (line[i] <= '9')) {
				if (fd == 0x00) fd = line[i];
				ld = line[i];
			}
		}

		for (const auto& entry : numbers) {
			line = std::regex_replace(
				line,
				std::regex(entry.first),
				entry.second
			);
		}

		char f2d = 0x00, l2d = 0x00;
		for (int i = 0; i < line.length(); ++i) {
			if ((line[i] >= '0') and (line[i] <= '9')) {
				if (f2d == 0x00) f2d = line[i];
				l2d = line[i];
			}
		}

		p1 += 10 * (fd - '0') + (ld - '0');
		p2 += 10 * (f2d - '0') + (l2d - '0');
	}

	std::cout << "Part One: " << p1 << std::endl;
	std::cout << "Part Two: " << p2 << std::endl;
	return 0;
}