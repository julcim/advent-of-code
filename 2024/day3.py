import re

class Day3:
    """Solution for Advent of Code 2024 Day 3."""

    def __init__(self, input_file: str = "day3_input.txt"):
        """Initialize with input file path."""
        self.input_file = input_file
        self.data = self._parse_input()
        self.data_part2 = self._parse_input_part2()

    def _parse_input(self):
        """Parse the input file and return processed data."""
        with open(self.input_file, 'r') as f:
            text = f.read().strip()
            pattern = r'mul\((\d+),(\d+)\)'
            matches = re.findall(pattern, text)

        return matches
    
    def _parse_input_part2(self):
        """Parse the input file and return processed data for part 2."""
        with open(self.input_file, 'r') as f:
            text = f.read().strip()

            pattern = r"(do\(\)|don't\(\)|mul\((\d+),(\d+)\))"
            matches = re.finditer(pattern, text)

            enabled = True  # mul instructions are enabled at start
            valid_muls = []

            for match in matches:
                instruction = match.group(1)

                if instruction == "do()":
                    enabled = True
                elif instruction == "don't()":
                    enabled = False
                elif instruction.startswith("mul") and enabled:
                    valid_muls.append((match.group(2), match.group(3)))

            return valid_muls

    def solve(self) -> int:
        """Solve part 1 of the puzzle."""
        input_array = self.data
        total = 0
        for i in input_array:
            total += int(i[0]) * int(i[1])
        return total

    def solve_part2(self) -> int:
        """Solve part 2 of the puzzle."""
        input_array = self.data_part2
        total = 0
        for i in input_array:
            total += int(i[0]) * int(i[1])
        return total


if __name__ == "__main__":
    solver = Day3()
    print(f"Part 1: {solver.solve()}")
    print(f"Part 2: {solver.solve_part2()}")
