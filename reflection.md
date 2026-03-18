
# Reflection

## 1. What was broken when you started?

1. I expected the game to give correct feedback based on my guess, but sometimes the hint did not match the actual value of the guess. For example, a guess lower than the secret number could still return "Too High," which made the game confusing.

2. I expected the game to handle invalid inputs such as letters or empty values, but instead the game would behave incorrectly or fail without giving a proper warning to the user.

3. I expected the game to reset completely when starting a new round, but the attempts, score, or previous guesses sometimes carried over, causing inconsistent behavior between games.

## 2. How did you use AI as a teammate?

One correct AI suggestion was to move the core game logic out of `app.py` and into a separate file called `logic_utils.py`. This made the code easier to organize and allowed me to test the logic independently using pytest. I verified this by running the tests and confirming that the game behaved correctly in the browser.

One misleading AI suggestion was to fix bugs by adding more conditional statements directly into the UI code. This made the code more complicated and harder to maintain without actually solving the root issue. I rejected this approach after reviewing the changes and instead simplified the logic by separating responsibilities between files.

## 3. Debugging and testing your fixes

I verified my fixes using both automated and manual testing. First, I created pytest test cases to check input parsing, guess evaluation, score calculation, and game reset behavior. I ran pytest to ensure all tests passed successfully. Then, I ran the Streamlit application and tested different scenarios, including valid guesses, invalid inputs, and restarting the game, to confirm that everything worked correctly in the live application.

## Final Reflection

This project showed me that AI can be a powerful tool for debugging and development, but it is not always correct. I learned that I need to carefully review AI-generated suggestions, test them, and make adjustments when necessary. The most valuable takeaway was understanding how to combine AI assistance with my own reasoning to produce reliable and maintainable code.