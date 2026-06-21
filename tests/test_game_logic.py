from logic_utils import check_guess

def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert result == "Win"

def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert result == "Too High"

def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert result == "Too Low"

def test_high_low_direction_not_swapped():
    # Targets the bug we fixed: high/low direction used to be backwards.
    # A guess ABOVE the secret must be "Too High" (never "Too Low"),
    # and a guess BELOW the secret must be "Too Low" (never "Too High").
    assert check_guess(75, 30) == "Too High"
    assert check_guess(10, 30) == "Too Low"
