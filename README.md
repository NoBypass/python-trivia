# Python Trivia
## 1.1 Purpose
The Purpose of this Project is to provide a way to kill some time whenever someone is sitting in from of their computer and does not know what to do. Most of the questions are general knowledge questions, which means that one can even learn from being bored.

## 1.2 Goals
1. Specific Goal: Increase Correct Answers
    - Objective: Improve the user's knowledge and accuracy in answering quiz questions.
    - Example: Increase the number of correct answers by 10% compared to the previous game session.

2. Measurable Goal: Track User Progress
    - Objective: Monitor the user's progress and provide feedback on their performance.
    - Example: Implement a scoring system to calculate and display the user's score based on the number of correct answers.

3. Achievable Goal: Offer Different Difficulty Levels
    - Objective: Provide a challenging yet achievable experience for users of varying knowledge levels.
    - Example: Implement multiple difficulty levels (easy, medium, hard) that adapt the complexity of the questions based on the user's selection.

## 1.3 Requirements
**Python Modules:**
- `random` Used for generating random values and shuffling options.
- `os`  Used to rerun the game if the user wants to.
- `urllib` Used for making HTTP requests to retrieve the questions from external sources.
- `json` Used to save the games in a JSON file.
- `math` Used for various mathematical operations.

**Custom Libraries:**
   - `menu`: Provides functions for displaying menus. For example, it is used in the `menu` function calls to display the game mode menu and difficulty menu.
   - `newQuestion`: Provides a function for retrieving new quiz questions from an API based on the selected topic, difficulty level, and game mode. For example, it is used in the `data = newQuestion(topic, difficulty, game_mode)` line to fetch a new question.
   - `progressBar`: Provides a function for generating a progress bar visualization. For example, it is used in the `progressBar(100 / int(max_score) * int(score), 20)` line to display the user's progress.
   - `toScores`: Provides a function for storing user scores in the "scores.json" file. For example, it is used in the `to_scores(statObject, game_mode)` line to save the user's statistics.
   - `validate`: Provides a function for validating user input. For example, it is used in the `game_mode = validate('Choose a game mode', ['1', '2'])` line to validate the user's selection.
   - `getColor`: Provides a function for retrieving color codes based on a given input. For example, it is used in the `get_color(firstTry)` line to get the color for displaying the "first try" text.
   - `multipleChoice`: Provides a function for handling multiple-choice questions and user answers. For example, it is used in the `questionStats = (multipleChoice(format_string(question), answer, format_string(options)))` line to process the user's answer.
   - `trueFalse`: Provides a function for handling true/false questions and user answers. For example, it is used in the `questionStats = (true_false(format_string(question), answer))` line to process the user's answer.
   - `podium`: Provides a function for displaying a podium with the user's name, score, and game mode. For example, it is used in the `podium(name, score, game_mode)` line to show the user's performance.
   - `colored`: Provides a function for coloring text in the console. For example, it is used in the `print(colored('Please make sure that every module is installed.\nRequired modules: \n - random\n - os\n - urllib\n - json\n ' '- math\n  Disconnected to avoid redundancies in the JSON file.', 'red'))` line to display an error message in red color.
   - `format`: Provides functions for formatting strings. For example, it is used in the `question = format_string(data['results'][0]['question'])` line to format the question text.


## 1.4 Inputs
The script accepts the following inputs from the user:

1. **User Name:** The user is prompted to enter their preferred name to be used throughout the game.
2. **Game Mode:** The user selects the game mode (either true/false or multiple-choice) they want to play.
3. **Difficulty** Level: The user chooses the difficulty level (easy, medium, or hard) for the quiz questions.
4. **Topic Selection:** The user selects a specific topic or chooses to play with questions from any category.

## 1.5 Outputs
The script provided outputs are:

1. **Quiz Questions:** The script retrieves questions from an API based on the selected topic, difficulty level, and game mode. The questions are then presented to the user.
2. **Answer Options:** For multiple-choice questions, the script shuffles the answer options and displays them to the user.
2. **User Interaction:** The script prompts the user to answer the questions by selecting the correct option or providing a true/false response.
3. **Game Statistics:** The script keeps track of the user's performance, including the number of correct and incorrect answers, first try successes, and overall score.
4. **Score Calculation:** The script calculates the user's score based on their performance, taking into account factors such as correct answers, incorrect answers, and difficulty level.
5. **Progress Bar:** The script displays a visual representation of the user's progress through a progress bar.
6. **Game Results:** After completing the game, the script presents the user with their final score, performance statistics, and an option to play again or quit the game.

## 5.1 Usecases
### (T1) |15 questions get asked of true-false is selected on easy mode
**Prerequisites:**
- The script is started
- The dependency error handling did not trigger
- A name was given

**Test:**
1. In the gamemode menu, select (1)
2. In the difficulty menu, select (1)
3. Choose any number (0..24)
4. Type `skip` on every question or answer it

**Expected results:**
One was able to skip or answer the questions exactly 15 times. The program did not end early and after answering for the 15th time, the podium displayed.

### (T2) The multiple choice questions are different in every category/fit the category
**Prerequisites:**
- The script is started
- The dependency error handling did not trigger
- A name was given

**Test:**
1. In the gamemode menu, select (2)
2. In the difficulty menu, select any mode (1..3)
3. Choose any number (1..24) except 1
4. Play quiz and note the questions
5. Choose (1) in the play again menu
6. In the gamemode menu, select (2)
7. In the difficulty menu, select any mode (1..3)
8. Choose any number (1..24) except 1. Make sure not to select the same as last time
9. Note questions

**Expected results:**
The questions fit the category and are not about any other topic than what the category is titled. Also a question from the first category should never appear in the second category.

## 5.2 Test results
| Test ID | Successful |
| ------- | ---------- |
| T1 | yes |
| T2 | no |