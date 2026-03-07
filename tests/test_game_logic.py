#FIX: Put proper imports for proper detection in launch
import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))

from logic_utils import check_guess

#FIX: Compare correct value in Copilot Agent mode
def test_winning_guess():
    # If the secret is 50 and guess is 50, it should be a win
    result = check_guess(50, 50)
    assert "Win" in result

#FIX: Compare correct value in Copilot Agent mode
def test_guess_too_high():
    # If secret is 50 and guess is 60, hint should be "Too High"
    result = check_guess(60, 50)
    assert "Too High" in result

#FIX: Compare correct value in Copilot Agent mode
def test_guess_too_low():
    # If secret is 50 and guess is 40, hint should be "Too Low"
    result = check_guess(40, 50)
    assert "Too Low" in result


# Bug fix tests: check_guess returns (outcome, message) tuple.
# The bug was that "Too High" and "Too Low" outcome labels were swapped —
# guess < secret incorrectly returned "Too High" instead of "Too Low",
# and guess > secret incorrectly returned "Too Low" instead of "Too High".
# The hints (Go HIGHER / Go LOWER) were correct throughout.
#FIX: Compare correct value in Copilot Agent mode
def test_too_low_outcome_label_is_correct():
    """guess < secret means the guess was too low — outcome must be 'Too Low'."""
    outcome, _ = check_guess(40, 50)
    assert outcome == "Too Low", (
        f"guess=40 < secret=50: expected outcome 'Too Low', got '{outcome}'"
    )

def test_too_low_hint_says_go_higher():
    """When guess is too low, hint must direct the player to go HIGHER."""
    _, message = check_guess(40, 50)
    assert "HIGHER" in message, (
        f"guess=40 < secret=50: expected hint with 'HIGHER', got '{message}'"
    )

def test_too_high_outcome_label_is_correct():
    """guess > secret means the guess was too high — outcome must be 'Too High'."""
    outcome, _ = check_guess(60, 50)
    assert outcome == "Too High", (
        f"guess=60 > secret=50: expected outcome 'Too High', got '{outcome}'"
    )

def test_too_high_hint_says_go_lower():
    """When guess is too high, hint must direct the player to go LOWER."""
    _, message = check_guess(60, 50)
    assert "LOWER" in message, (
        f"guess=60 > secret=50: expected hint with 'LOWER', got '{message}'"
    )

def test_win_outcome_and_message():
    """Exact match returns 'Win' outcome and a congratulatory message."""
    outcome, message = check_guess(50, 50)
    assert outcome == "Win"
    assert "Correct" in message
