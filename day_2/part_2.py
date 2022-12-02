from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()


def run():
    lines = read_file('./input.txt')

    moves = ['A', 'B', 'C']
    results = {
        'X': -1,
        'Y': 0,
        'Z': 1
    }

    total_score = 0
    for line in lines:
        score = 0
        opponent_move, result = line.split(" ")

        score += (((moves.index(opponent_move) +
                  results[result]) % 3) + 1) + list(results.keys()).index(result) * 3

        total_score += score

    print(total_score)


if __name__ == '__main__':
    run()
