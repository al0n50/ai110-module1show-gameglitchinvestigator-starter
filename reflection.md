# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").

  When I first ran the game, the UI looked completely normal and playable, but the underlying logic was deeply flawed. First, the hints were completely backwards; if I guessed too high, the game told me to "Go HIGHER!". Second, the game would crash on every even-numbered attempt because the code deliberately converted the secret number into a string, breaking the math comparisons. Finally, guessing incorrectly on those even attempts actually added points to my score instead of penalizing me.

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).

I used VS Code Copilot to help explain the codebase and generate fixes. One correct AI suggestion was identifying that the strings inside the if guess > secret: block were mismatched, which I verified by reading the code and testing the new logic in the browser. However, an incorrect/misleading suggestion was when the AI tried to fix the string conversion crash by wrapping the comparison in a complex try/except block. I verified this was the wrong approach because the root cause was a sabotage line (if attempts % 2 == 0: secret = str(secret)) that needed to be deleted entirely, not just worked around.
---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
- Did AI help you design or understand any tests? How?

I knew a bug was really fixed when I could play the game end-to-end in the Streamlit browser without any errors and win with an accurate score. To verify the underlying logic, I ran pytest on test_game_logic.py, which included tests like test_guess_too_high() to ensure the hint logic returned the correct string. AI helped me design tests by generating the specific pytest syntax needed to assert that my refactored update_score function correctly deducted 5 points.
---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

If I were explaining this to a friend, I'd say that Streamlit is a bit like a goldfish—every time you click a button or enter text, it forgets everything and runs your entire script from top to bottom again. Because of this "rerun" behavior, we have to use st.session_state. Session state is basically a backpack the app wears to safely hold onto important variables (like your current score, attempt count, and the secret number) so they survive the page reloading.
---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.

One habit I want to reuse is separating my core game logic (into logic_utils.py) away from my UI code (in app.py), which made it much easier to isolate and test bugs. Next time I work with AI, I will spend more time reading the code it generates before running it, rather than assuming it works right away. This project changed the way I think about AI-generated code because it proved that AI can write code that looks clean and "production-ready" on the surface, but still contains major logical flaws that require human intuition to solve.