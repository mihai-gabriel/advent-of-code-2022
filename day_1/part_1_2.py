from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()


def run():
    lines = read_file('./input.txt')
    elves_bags: List[int] = []

    accumulator = 0
    for idx in range(len(lines)):
        if lines[idx] == '' or idx - 1 == len(lines):
            elves_bags.append(accumulator)
            accumulator = 0
            continue

        accumulator += int(lines[idx])

    sorted_bags = sorted(elves_bags, reverse=True)
    print(f"Part 1: {sorted_bags[0]}")
    print(f"Part 2: {sorted_bags[0] + sorted_bags[1] + sorted_bags[2]}")


if __name__ == '__main__':
    run()
