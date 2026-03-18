# Game Glitch Investigator

## Project Overview
This project is a Streamlit-based number guessing game that I debugged and repaired as part of the Game Glitch Investigator assignment. The goal was to identify bugs in AI-generated code, refactor the logic into a separate module, and verify the fixes using automated tests.

## Demo
The game allows the user to guess a secret number between 1 and 100. After each guess, the game provides feedback indicating whether the guess is too high, too low, or correct. It also tracks the number of attempts, the player's score, and a history of guesses.

## Features
- Input validation for user guesses
- Accurate hint system (Too High / Too Low / Correct)
- Score tracking based on number of attempts
- Game reset functionality
- Guess history display
- Automated testing using pytest

## What I Fixed
During the debugging process, I identified and fixed several issues:
- Incorrect hint logic that sometimes gave wrong feedback
- Unsafe input handling that could break the game
- Game state not resetting properly between rounds
- Score inconsistencies across multiple attempts

## Refactoring
I moved core game logic from `app.py` into `logic_utils.py` to improve:
- Code readability
- Separation of concerns (UI vs logic)
- Testability

## Testing
I created automated tests using pytest to verify:
- Input parsing behavior
- Guess evaluation logic
- Score calculation
- Game reset functionality

Run tests:
```bash
pytest