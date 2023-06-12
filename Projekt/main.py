import random

from lib.menu import *
from lib.newQuestion import *
from lib.progressBar import *
from lib.validate import *
from lib.getColor import *
from lib.multipleChoice import *
from lib.trueFalse import *
from lib.podium import *
from lib.colored import *
from lib.format import *

from random import shuffle
import os
from urllib.request import urlopen
import math
import lib.database as db

db.create_if_not_exists()

# Check if all dependencies are installed
try:
    test = [
        random.random(),
        os.name,
        urlopen('https://www.google.com/'),
        math.floor(9.3)
    ]
except ModuleNotFoundError:
    print(colored(
        'Please make sure that every module is installed.\nRequired modules: \n - random\n - os\n - urllib\n - json\n '
        '- math\n  Disconnected to avoid redundancies in the JSON file.',
        'red'))
    quit()
except FileNotFoundError:
    print(colored('Please make sure that the scores.json file is in the same directory as the main.py file.', 'red'))
    quit()

print(colored(
    'Please note that you always have to type out the given numbers, not the full words! You can also write "skip" as '
    'an answer if you dont know it.',
    'red'))

# Welcome
name = input(colored('What do you want to be called? ▶ ', 'blue'))

while True:
    menu(50, ['full', 'Game mode Menu:', 'full', '(1) Play true / false', '(2) Play Multiple Choice', 'full'])
    game_mode = validate('Choose a game mode', ['1', '2'])

    menu(50, ['full', 'Difficulty Menu:', 'full', '(1) Easy', '(2) Medium', '(3) Hard', 'full'])
    difficulty = validate('Choose a difficulty', ['1', '2', '3'])

    # Topic-chooser menu
    menu_items = ['full', 'Topic Menu:', 'full', '(0) Any Category', '(1) General Knowledge', '(2) Books', '(3) Films',
                  '(4) Music',
                  '(5) Musicals & Theatres', '(6) Television', '(7) Video Games', '(8) Board Games',
                  '(9) Science & Nature',
                  '(10) Computers', '(11) Mathematics', '(12) Mythology', '(13) Sports', '(14) Geography',
                  '(15) History',
                  '(16) Politics', '(17) Art', '(18) Celebrities', '(19) Animals', '(20) Vehicles', '(21) Comics',
                  '(22) Science Gadgets', '(23) Anime & Manga', '(24) Cartoon & Animations', 'full']
    menu(50, menu_items)
    valids = []
    for i in range(0, len(menu_items)):
        valids.append(str(i))
    topic = '&category=' + str(int(validate('Choose a topic', valids)) + 8)

    # Configure game
    if topic == '&category=8':
        topic = ''

    match difficulty:
        case '1':
            difficulty = '&difficulty=easy'
            limit = 15
            multiplier = 0.5
        case '2':
            difficulty = '&difficulty=medium'
            limit = 30
            multiplier = 1
        case _:
            difficulty = '&difficulty=hard'
            limit = 45
            multiplier = 1.5

    if game_mode == '1':
        game_mode = '&type=boolean'
    else:
        game_mode = '&type=multiple'

    # Example api link: https://opentdb.com/api.php?amount=1&category=22&difficulty=medium&type=multiple

    game_iterations = 0
    first_try = 0
    incorrect = 0
    correct = 0
    mode = ''

    # game loop:
    while game_iterations < limit:
        data = new_question(topic, difficulty, game_mode)

        question = format_string(data['results'][0]['question'])
        answer = data['results'][0]['correct_answer']

        # there is slightly different logic depending on the game mode
        if game_mode == '&type=multiple':

            possible_answers = [
                data['results'][0]['correct_answer'],
                data['results'][0]['incorrect_answers'][0],
                data['results'][0]['incorrect_answers'][1],
                data['results'][0]['incorrect_answers'][2],
            ]

            shuffle(possible_answers)
            options = 'a: ' + possible_answers[0] + ' b: ' + possible_answers[1] + ' c: ' \
                      + possible_answers[2] + ' d: ' + possible_answers[3]

            chosen_answer_index = possible_answers.index(answer)
            if chosen_answer_index == 0:
                answer = 'a'
            elif chosen_answer_index == 1:
                answer = 'b'
            elif chosen_answer_index == 2:
                answer = 'c'
            elif chosen_answer_index == 3:
                answer = 'd'

            question_stats = (multiple_choice(format_string(question), answer, format_string(options)))
            correct += question_stats[2]
            incorrect += question_stats[1]
            if incorrect == 0:
                first_try += 1

            if question_stats[3]:
                break

        elif game_mode == '&type=boolean':
            data = new_question(topic, difficulty, game_mode)

            question = format_string(data['results'][0]['question'])
            answer = data['results'][0]['correct_answer']

            question_stats = (true_false(format_string(question), answer))
            correct += question_stats[2]
            incorrect += question_stats[1]

            first_try = 'N/A'

            if question_stats[3]:
                break

        game_iterations += 1

    # score calculations
    max_score = 0
    if first_try != 'N/A':
        max_score = limit * 5 * multiplier
    else:
        max_score = limit * multiplier
    score = 0
    if first_try != 'N/A':
        score = (first_try * 5 - incorrect + correct) * multiplier
    else:
        score = (correct - incorrect) * multiplier
    if score < 0:
        new_score = 0
    else:
        new_score = score

    stat_object = {
        "user": name,
        "correct": correct,
        "incorrect": incorrect,
        "firsttry": first_try,
        "score": score,
        "multiplechoice": game_mode == '&type=multiple',
    }

    db.write(stat_object)

    # User feedback
    first_try_text = ' '
    correctOnes = str(correct)
    correctPercentage = 100 / (incorrect + correct) * correct

    if first_try != 'N/A':
        correctOnes = str(correct + first_try)
    if first_try != 'N/A':
        first_try_text = colored('You got it first try ' + str(first_try) + ' times.', get_color(first_try))

    podium(name, score, game_mode)

    incorrect_s = 's'
    if incorrect != 1:
        incorrect_s = ''

    try:
        menu(50, [
            'full',
            [('Your score is: ' + str(new_score) + '/' + str(max_score)), get_color(100 / max_score * new_score)],
            [progressBar(100 / math.ceil(max_score) * int(score), 20), get_color(100 / max_score * score)],
            [('You made ' + str(incorrect) + ' mistake' + incorrect_s), get_color(correctPercentage)],
            first_try_text,
            [('You answered correctly ' + correctOnes + ' times!'), get_color(correctPercentage)],
            'empty',
            'full'

        ])
    except ZeroDivisionError:
        print("Most lost player ever !!!")

    print(colored('Do you want to play again?\n   (1) Play again\n   (2) Quit', 'blue'))

    play_again = validate('With what action do you want to continue?', ['1', '2'])

    if play_again != '1':
        break
