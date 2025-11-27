class Day2:
    """Solution for Advent of Code 2024 Day 2."""

    def __init__(self, input_file: str = "day2_input.txt"):
        """Initialize with input file path."""
        self.input_file = input_file
        self.data = self._parse_input()

    def _parse_input(self):
        """Parse the input file and return processed data."""
        with open(self.input_file, 'r') as f:
            lines = f.read().strip().split('\n')

        input_array = []

        for line in lines:
            parts = line.split()
            row = [int(part) for part in parts]
            input_array.append(row)

        return input_array

    def solve(self) -> int:
        """Solve part 1 of the puzzle."""
        input_array = self.data
        total_safe_reports = 0
        for i in input_array:
            if self.check_array(i):
                total_safe_reports += 1

        return total_safe_reports
    
    def solve_part2(self) -> int:
        """Solve part 2 of the puzzle with Problem Dampener."""
        input_array = self.data
        safe_reports_with_dampener = 0
        for i in input_array:
            if self.check_array_with_dampener(i):
                safe_reports_with_dampener += 1

        return safe_reports_with_dampener


    def check_array(self, a) -> bool:
        # Check if all increasing or all decreasing
        is_increasing = a == sorted(a)
        is_decreasing = a == sorted(a, reverse=True)
        if not (is_increasing or is_decreasing):
            return False

        # Check if all differences are between 1 and 3
        for i in range(len(a) - 1):
            diff = abs(a[i + 1] - a[i])
            if not (1 <= diff <= 3):
                return False

        return True
    
    def check_array_with_dampener(self, a) -> bool:
        """Check if array is safe, or can be made safe by removing one level."""
        # First check if it's already safe without removing anything
        if self.check_array(a):
            return True

        # Try removing each level one at a time
        for i in range(len(a)):
            modified_array = a[:i] + a[i+1:]
            if self.check_array(modified_array):
                return True

        return False


if __name__ == "__main__":
    solver = Day2()
    print(f"Part 1 - Safe Reports: {solver.solve()}")
    print(f"Part 2 - Safe Reports with Dampener: {solver.solve_part2()}")
