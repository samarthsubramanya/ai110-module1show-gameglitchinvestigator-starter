# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?

The game launched without any hiccups and had a basic interface. It was a number guessing game with 3 levels of difficulty to choose from. The page also had attempts remaining and a secret developer section to assist us with debugging and finding internal states so as to track the bugs efficiently. After experimenting with the game, I found multiple issues which I have listed below in the next question. 

- List at least two concrete bugs you noticed at the start  
  (for example: "the hints were backwards").
  1. The suggestions/hints were inverted. While the guess was lower than secret number, instead of showing HIGHER it showed LOWER and vice versa.
  2. The New Game button was not working. Although the secret number refreshed to a different one, the UI did not update and I was not able to input any new number into the input box.
  3. I also observed that the attempts remaining was going negative (below 0) on this occassion when trying to switch difficulty level.
  4. Also, when trying to switch the difficulty level, the secret number was not changing even though the range and number of attempts were changing.
  5. Easy (1 to 20), Normal (1 to 100) and Hard (1 to 50) was the preset. But considering the level, it would be better to have Normal as (1 to 50) and Hard (1 to 100) as it would be more difficult to guess.
  6. Enter button on submitting the guess in input box had no effect. I had to click on the "Submit Guess" button to submit the guess. It would be better if the Enter button also worked for submitting the guess as it would be more intuitive and user friendly.
  7. Initially attempt is 1 instead of 0.


---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)?
  I used Claude for this project. I used it in the "Agent" mode which allowed me to give it access to the codebase and it was able to read through the code and suggest changes based on the bugs that I mentioned above. I also used it in the "Chat" mode to ask specific questions about the code and get explanations for certain parts of the code that I did not understand.
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result).
  One example was the bug where pressing New Game button had no effect in the UI. I mentioned this bug to the AI and it suggested that the issue was with the way the secret number was being stored in the session state. It suggested that I should make sure that the secret number is being updated in the session state when the New Game button is pressed. I verified this by checking the code and seeing that the secret number was indeed being updated in the session state, but the UI was not reflecting this change. After making some changes to the code based on the AI's suggestion, I was able to fix the issue and now pressing the New Game button updates the UI with a new secret number.
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
  One example was the bug where the hints were inverted. I mentioned this bug to the AI and it suggested that the issue was with the way the check_guess function was implemented. It initially suggested that the issue was with parsing the guess in the app.py file and that I should make sure that the guess is being parsed as an integer. While this was a valid suggestion, it did not directly address the issue of the hints being inverted. After making some changes to the code based on the AI's suggestion, I was still seeing the same issue with the hints. I then had to do some more debugging on my own and found that the issue was actually with the logic in the check_guess function where the conditions for checking if the guess is too high or too low were inverted. After fixing this logic, I was able to get the correct hints to show up.

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
  I decided that a bug was really fixed when I was able to reproduce the steps that caused the bug before the fix, and then after the fix, those same steps no longer caused the bug. For example, for the New Game button issue, I would press the New Game button and check if the secret number in the UI updated to a new number. If it did, then I considered that bug to be fixed. For the hints being inverted issue, I would make a guess that was lower than the secret number and check if the hint showed "Go Higher" instead of "Go Lower". If it showed the correct hint, then I considered that bug to be fixed. I also ran the tests to detect any programmatic errors based on the logic if so.
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I ran the Inverted hints test which I had written in the test_game_logic.py file. This test was designed to check if the hints were showing up correctly based on whether the guess was too high or too low compared to the secret number. When I ran this test before fixing the issue, it failed because the hints were inverted. After I fixed the logic in the check_guess function, I ran the test again and it passed successfully, which showed me that the hints were now working correctly.
- Did AI help you design or understand any tests? How?
  Yes, AI helped me understand how to design tests for the game logic. While writing the tests for the check_guess function, I wasn't sure how to structure the tests or what cases to cover. I asked the AI for suggestions on writing effective tests for this function. It gave me a clear structure for testing different scenarios, such as a winning guess, a guess that is too high, and a guess that is too low. It also helped me see the importance of testing edge cases and covering all possible outcomes in the tests. This guidance from the AI helped me write better and more effective tests for the game logic.

---

## 4. What did you learn about Streamlit and state?

- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?

---

## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects?
  - This could be a testing habit, a prompting strategy, or a way you used Git.
- What is one thing you would do differently next time you work with AI on a coding task?
- In one or two sentences, describe how this project changed the way you think about AI generated code.
