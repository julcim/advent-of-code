class Day1:
    """solution for advent of code 2025 Day 1."""

    def __init__(self, input_file: str = "inputs/day1_2025_input.txt"):
        self.input_file = input_file
        self.data = self._parse_input()
        self.dial = 50

    def _parse_input(self):
        """parse input file"""
        with open(self.input_file, 'r') as f:
            lines = f.read().strip().split('\n')

        input_array = []

        for line in lines:
           input_array.append(line)

        return input_array

    def find_password(self) -> int:
        """solve part1 of the puzzle"""
        input_array = self.data
        password = 0
        amount_of_full_rotations = 0
        for i in input_array:
            new_dial, rotations = self.rotate_dial(i)
            if new_dial == 0:
                password += 1
            amount_of_full_rotations += rotations
        return password, amount_of_full_rotations
    
    def rotate_dial(self, dial_twist):
        """rotates dial and returns the number the dial is at after rotating"""
        dial = self.dial
        twist = int(dial_twist[1:])
        direction = dial_twist[0]
        # check for full rotations
        amount_of_full_rotations = twist // 100
        remaining_rotation = twist % 100
        if direction == "L":
            # partial rotation passes 0, if dial = 0, we have just rotated
            if dial == 0 or dial < remaining_rotation:
                amount_of_full_rotations += 1
            # amount of times we hit 0 exactly      
            self.dial = (dial - twist) % 100
        else:
            # amount of times we hit 0 exactly    
            self.dial = (dial + twist) % 100  
            # partial rotation passes 0, if dial = 0, we have just rotated
            if dial == 0 or dial + remaining_rotation > 100:
                amount_of_full_rotations += 1
        return self.dial, amount_of_full_rotations


if __name__ == "__main__":
    solver = Day1()
    password, amount_of_rotations = solver.find_password()
    print(f"Part 1 Password: {password}")
    print(f"Part 2 Password: {amount_of_rotations}")
