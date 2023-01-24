from aoc.year_2022 import day02


class TestPlayerVsEnemyRound:
    def test_paper_beats_rock(self):
        expected_score = 8
        round = "A Y"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_paper_loses_to_scissors(self):
        expected_score = 2
        round = "C Y"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_paper_vs_paper_is_tie(self):
        expected_score = 5
        round = "B Y"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_scissors_beats_paper(self):
        expected_score = 9
        round = "B Z"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_scissors_loses_to_rock(self):
        expected_score = 3
        round = "A Z"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_scissors_vs_scissors_is_tie(self):
        expected_score = 6
        round = "C Z"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_rock_beats_scissors(self):
        expected_score = 7
        round = "C X"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_rock_loses_to_paper(self):
        expected_score = 1
        round = "B X"

        score = day02.get_round_result(round)

        assert score == expected_score

    def test_rock_vs_rock_is_tie(self):
        expected_score = 4
        round = "A X"

        score = day02.get_round_result(round)

        assert score == expected_score


class TestPart1:
    def test_score_of_one_round(self):
        expected_score = 4
        rounds = ["A X"]

        score = day02.part1(rounds)

        assert score == expected_score

    def test_score_of_multiple_rounds(self):
        expected_score = 15
        rounds = ["A Y", "B X", "C Z"]

        score = day02.part1(rounds)

        assert score == expected_score


class TestPart2:
    def test_score_of_tie_round(self):
        expected_score = 4
        rounds = ["A Y"]

        score = day02.part2(rounds)

        assert score == expected_score

    def test_score_of_player_losses_round(self):
        expected_score = 1
        rounds = ["B X"]

        score = day02.part2(rounds)

        assert score == expected_score

    def test_score_of_player_wins_round(self):
        expected_score = 7
        rounds = ["C Z"]

        score = day02.part2(rounds)

        assert score == expected_score

    def test_score_of_multiple_rounds(self):
        expected_score = 12
        rounds = ["A Y", "B X", "C Z"]

        score = day02.part2(rounds)

        assert score == expected_score
