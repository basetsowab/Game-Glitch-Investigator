from logic_utils import parse_guess, check_guess, calculate_score, reset_game


def test_parse_guess_valid():
    assert parse_guess("42") == 42


def test_parse_guess_invalid_string():
    assert parse_guess("abc") is None


def test_parse_guess_empty():
    assert parse_guess("") is None


def test_parse_guess_whitespace():
    assert parse_guess("   15   ") == 15


def test_check_guess_too_low():
    assert check_guess(25, 50) == "Too Low"


def test_check_guess_too_high():
    assert check_guess(75, 50) == "Too High"


def test_check_guess_correct():
    assert check_guess(50, 50) == "Correct"


def test_calculate_score_first_attempt():
    assert calculate_score(1) == 90


def test_calculate_score_never_negative():
    assert calculate_score(15) == 0


def test_reset_game_defaults():
    game_state = reset_game()
    assert "secret_number" in game_state
    assert game_state["attempts"] == 0
    assert game_state["score"] == 100
    assert game_state["game_over"] is False
    assert game_state["history"] == []