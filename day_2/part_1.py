from typing import List


def read_file(filename: str) -> List[str]:
    with open(filename, 'r') as f:
        return f.read().splitlines()


def run():
    lines = read_file('./input.txt')

    move_point = {
        'X': 1,
        'Y': 2,
        'Z': 3,
    }

    moves_match = {
        'X': 'A',
        'Y': 'B',
        'Z': 'C',
    }

    me_winning_scenarios = [
        ('A', 'Y'),
        ('B', 'Z'),
        ('C', 'X'),
    ]

    total_score = 0
    for line in lines:
        score = 0
        opponent_move, my_move = line.split(" ")

        score += move_point[my_move]

        if moves_match[my_move] == opponent_move:
            score += 3

        elif (opponent_move, my_move) in me_winning_scenarios:
            score += 6

        total_score += score

    print(total_score)


if __name__ == '__main__':
    run()
