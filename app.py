import streamlit as st
from logic_utils import (
    generate_secret_number,
    parse_guess,
    check_guess,
    calculate_score,
    reset_game,
)

st.set_page_config(page_title="Number Guessing Game")

st.title("Number Guessing Game")
st.write("Try to guess the secret number between 1 and 100.")

# FIX: Initialized all session state values clearly so the game behaves consistently.
if "secret_number" not in st.session_state:
    st.session_state.secret_number = generate_secret_number()
if "attempts" not in st.session_state:
    st.session_state.attempts = 0
if "score" not in st.session_state:
    st.session_state.score = 100
if "game_over" not in st.session_state:
    st.session_state.game_over = False
if "history" not in st.session_state:
    st.session_state.history = []

st.subheader("Game Status")
st.write(f"Attempts: {st.session_state.attempts}")
st.write(f"Score: {st.session_state.score}")

guess_input = st.text_input("Enter your guess:")

col1, col2 = st.columns(2)

with col1:
    if st.button("Submit Guess"):
        # FIXME: Input parsing was previously unsafe in buggy versions.
        # FIX: Refactored parsing and guess checking into logic_utils.py using AI help,
        # then manually reviewed and simplified the logic.
        guess = parse_guess(guess_input)

        if st.session_state.game_over:
            st.warning("The game is already over. Click 'Play Again' to start a new round.")

        elif guess is None:
            st.error("Please enter a valid whole number.")

        elif guess < 1 or guess > 100:
            st.warning("Your guess must be between 1 and 100.")

        else:
            st.session_state.attempts += 1
            result = check_guess(guess, st.session_state.secret_number)
            st.session_state.history.append((guess, result))
            st.session_state.score = calculate_score(st.session_state.attempts)

            if result == "Too Low":
                st.info("Too Low")
            elif result == "Too High":
                st.info("Too High")
            elif result == "Correct":
                st.success(f"Correct. The secret number was {st.session_state.secret_number}.")
                st.session_state.game_over = True

with col2:
    if st.button("Play Again"):
        # FIX: Reset logic moved into logic_utils.py so state resets cleanly every round.
        new_state = reset_game()
        st.session_state.secret_number = new_state["secret_number"]
        st.session_state.attempts = new_state["attempts"]
        st.session_state.score = new_state["score"]
        st.session_state.game_over = new_state["game_over"]
        st.session_state.history = new_state["history"]
        st.success("New game started.")

st.subheader("Guess History")
if st.session_state.history:
    for i, (guess, result) in enumerate(st.session_state.history, start=1):
        st.write(f"{i}. Guess: {guess} -> {result}")
else:
    st.write("No guesses yet.")