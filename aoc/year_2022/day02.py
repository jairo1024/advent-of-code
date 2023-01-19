def part1(rounds):
    """
    Big O: O(1) / Time complexity: O(n^2)
    :param rounds: A list of the rounds
    :return: Returns the total score of the player for all of the rounds
    """
    score = 0
    for round in rounds:
        score += get_round_result(round)

    return score


def get_round_result(round):
    """
    A: Rock
    B: Paper
    C: Scissors

    X: Rock      1
    Y: Paper     2
    Z: Scissors  3

    Lose: 0
    Tie: 3
    Win: 6
                            Matrix

                            Player
                        Rock  Paper   Scissors
             Rock:       4      8       3
    Enemy    Paper:      1      5       9
             Scissors:   7      2       6


    """
    outcomes = {
        "Rock": {"Rock": 4, "Paper": 1, "Scissors": 7},
        "Paper": {"Rock": 8, "Paper": 5, "Scissors": 2},
        "Scissors": {"Rock": 3, "Paper": 9, "Scissors": 6},
    }

    table = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }

    enemy, player = round.split(" ")
    player = table[player]
    enemy = table[enemy]
    return outcomes[player][enemy]
