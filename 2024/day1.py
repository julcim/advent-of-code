class Day1:
    """Solution for Advent of Code 2024 Day 1."""

    def __init__(self, input_file: str = "day1_input.txt"):
        """Initialize with input file path."""
        self.input_file = input_file
        self.data = self._parse_input()

    def _parse_input(self):
        """Parse the input file and return processed data."""
        with open(self.input_file, 'r') as f:
            lines = f.read().strip().split('\n')

        left_array = []
        right_array = []

        for line in lines:
            parts = line.split()
            left_array.append(int(parts[0]))
            right_array.append(int(parts[1]))

        return left_array, right_array

    def part1(self) -> int:
        """Solve part 1 of the puzzle."""
        left_array, right_array = self.data
        left_array.sort()
        right_array.sort()
        total = 0
        for l, r in zip(left_array, right_array):
            total += abs(l - r)
        return total
    
    def part2(self) -> int:
        """Solve part 2 of the puzzle."""
        left_array, right_array = self.data
        right_numbers = {}
        # determine repeating numbers in right array
        for r in right_array:
            if r in right_numbers:
                right_numbers[r] = right_numbers[r] + 1
            else: 
                right_numbers[r] = 1
        # determine similarity score, check if l is in the right array and multiply
        # by amount of times its in the array
        similarity_score = 0
        for l in left_array:
            if l in right_numbers:
                similarity_score += l * right_numbers[l]
        return similarity_score
        



if __name__ == "__main__":
    solver = Day1()
    print(f"Part 1 Total: {solver.part1()}")
    print(f"Part 2 Similarity: {solver.part2()}")
