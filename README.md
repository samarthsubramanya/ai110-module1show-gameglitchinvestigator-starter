# 🎮 Game Glitch Investigator: The Impossible Guesser

## 🚨 The Situation

You asked an AI to build a simple "Number Guessing Game" using Streamlit.
It wrote the code, ran away, and now the game is unplayable. 

- You can't win.
- The hints lie to you.
- The secret number seems to have commitment issues.

## 🛠️ Setup

1. Install dependencies: `pip install -r requirements.txt`
2. Run the broken app: `python -m streamlit run app.py`

## 🕵️‍♂️ Your Mission

1. **Play the game.** Open the "Developer Debug Info" tab in the app to see the secret number. Try to win.
2. **Find the State Bug.** Why does the secret number change every time you click "Submit"? Ask ChatGPT: *"How do I keep a variable from resetting in Streamlit when I click a button?"*
3. **Fix the Logic.** The hints ("Higher/Lower") are wrong. Fix them.
4. **Refactor & Test.** - Move the logic into `logic_utils.py`.
   - Run `pytest` in your terminal.
   - Keep fixing until all tests pass!

## 📝 Document Your Experience

- [x] Describe the game's purpose. <br/>
   The main purpose of the game is guessing. A random number is picked by the system with preset attempts based on difficulty and the player has to guess the number correctly within the said attempts. To assist the player, the game will provide hints on each guess indicating whether the secret chose number is higher than or lower than the player's current guess. The game terminates when player correctly guesses the number of all attempts are exhausted. <br/>
   
- [x] Detail which bugs you found.
    The main bugs observed in the game which hampered the gameplay were:
    - The hints were inverted. If the chose secret number was 50 and user guessed 40, the hint would say "go Lower" instead of "go Higher". Similary, if player guess was 60, the hint would say "go Higher" instead of "go Lower". This made it impossible for the player to win the game as they were misled by the hints.
    - The New Game button did not perform any action. As the on click of the button did not reset the state to default, the game did not clear previous state and it was stuck in the same Completed screen. Hence the game could not be reset/restarted unless the page was reloaded.
    - When the page was loaded freshly after starting from the command line, the attempts was 1 already. This consumed one attempt from the precious limited attempts available to the user. This was due to the fact that attempts was set to 1 on state load. 
    - More bugs have been mentioned in reflections.md.
- [x] Explain what fixes you applied.
   For the above bugs, I applied the following fixes:
   - For the inverted hint, The guess was parsed as int . Then the comparison logic was fixed so that accurate guess would happen. The tests file was also updated accordingly as the function was returning a tuple of values and test was comparing only a single value.
   - For the New Game button, the session state, attempts and secret number were reset to default values to indicate that the session is restarted, i.e game is reseta and all state be initialized freshly. This allowed the game to be restarted without having to reload the page.
   - For the attempts issue, I set the attempts to 0 on state load instead of 1. This ensured that the user starts with 0 attempts and the first guess would consume the first attempt, which is the expected behavior.

## 📸 Demo

- [x] [Insert a screenshot of your fixed, winning game here]
   I have attached screenshots of 3 different scenarios.

|Scenario   | Image  |
|-----------|--------|
| Guess > Secret | ![Go Low](/images/ss_go_low.png)  |
| Guess < Secret | ![Go High](/images/ss_go_high.png)  |
| Guess = Secret(Win) | ![ Win ](/images/ss_win.png)  |

   

## 🚀 Stretch Features

- [x] [Advanced test Case]

![Advanced test case](/images/ss_a_t_1.png)
