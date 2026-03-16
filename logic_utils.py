# logic_utils.py

def get_range_for_difficulty(difficulty: str):
    """Return (low, high) inclusive range for a given difficulty."""
    if difficulty == "Easy":
        return 1, 20
    if difficulty == "Normal":
        return 1, 100
    if difficulty == "Hard":
        return 1, 200 # Fixed this from 50 so Hard actually makes sense!
    return 1, 100

def parse_guess(raw: str):
    """Parse user input into an int guess."""
    if raw is None or raw == "":
        return False, None, "Enter a guess."
    try:
        if "." in raw:
            value = int(float(raw))
        else:
            value = int(raw)
    except Exception:
        return False, None, "That is not a number."
    return True, value, None

# FIX: Used Copilot to identify and fix the reversed hint strings 
# so 'Too High' properly tells the user to go lower.
def check_guess(guess, secret):
    """Compare guess to secret and return (outcome, message)."""
    # FIXED: Hint logic is now pointing in the correct direction
    if guess == secret:
        return "Win", "🎉 Correct!"
    if guess > secret:
        return "Too High", "📉 Go LOWER!"
    else:
        return "Too Low", "📈 Go HIGHER!"

def update_score(current_score: int, outcome: str, attempt_number: int):
    """Update score based on outcome and attempt number."""
    if outcome == "Win":
        points = 100 - 10 * (attempt_number + 1)
        if points < 10:
            points = 10
        return current_score + points
    
    # FIXED: Incorrect guesses now consistently deduct 5 points
    if outcome == "Too High" or outcome == "Too Low":
        return current_score - 5
    
    return current_score