# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
When I first ran it, it looked like a normal guessing game with a title, a number box, and buttons. But as soon as I started guessing, the hints didn't match the secret number, so I could tell something was broken.
- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
Two bugs I noticed: (1) the hints were backwards — it told me to go lower when my guess was already too low; (2) my score dropped to -5 after a single wrong guess, which shouldn't happen.  

**Bug Reproduction Log**

Document at least 3 bugs you found. Add rows as needed.

| Input | Expected Behavior | Actual Behavior | Console Output / Error |
|-------|-----------------  |-----------------|------------------------|
| Click "New Game" after losing | Game resets and lets me guess again | Still shows "Game over" and blocks guessing | none |
| Guessed 15 when secret was 16 | "Go HIGHER!" (15 is lower than 16) | "Go LOWER!" shown — backwards | none |
| Guessed 35 (one wrong guess), secret 42 | Score stays 0 or small penalty | Score dropped to -5 (negative) | none |



---

## 2. How did you use AI as a teammate?
- I used Claude Code inside VS code as my AI assistant

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? VS code, shell terminal, and Claude.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).  Claude explained the hints were backwards because the "Too High"/"Too Low" messages were swapped and the secret was being turned into text on some guesses. This was correct — I verified it by fixing the code and playing the game, and guessing low now correctly says "Go HIGHER". The pytest tests also passed.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result). When refactoring, Claude first made check_guess return a tuple (outcome, message), but this broke the 3 starter tests. This was misleading — I caught it by running pytest, which showed 3 tests failing. We changed check_guess back to return only the outcome string, and all tests passed again.


---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed? I decided a bug was fixed when the game behaved correctly during play AND the pytest tests passed. For example, after fixing the hints, guessing low showed "Go HIGHER" and all 4 tests passed.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code. I ran "python -m pytest" and added a test called test_high_low_direction_not_swapped. It checks that a guess above the secret returns "Too High" and a guess below returns "Too Low". It showed my high/low fix works (4 passed).
- Did AI help you design or understand any tests? How? Yes. Claude helped me write the new pytest test and explained why the starter tests failed when check_guess returned a tuple, which taught me how tests catch mistakes.


---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
