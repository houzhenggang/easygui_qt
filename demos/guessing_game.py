import os
import sys
sys.path.insert(0, os.path.join(os.getcwd(), "../"))
import easygui_qt as eg
from random import randint

def guessing_game():
    name = eg.get_string(message="What is your name?",
                            title="Mine is Reeborg.")
    if not name:
        name = "Unknown person"

    message = """<p>The following language selection will only affect the
        default GUI elements like the text on the buttons.
        Note that <b>Default</b> is reverting back to the
        local PyQt default (likely English).</p>"""

    eg.show_message(message=message, title="For information")
    eg.select_language()

    eg.show_message(message="If the text is too small or too large," +
                      " you can fix that",
                      title="For information")
    eg.set_default_font()
    eg.show_message(message="Hello {}. Let's play a game".format(name),
                      title="Guessing game!")

    guess = min_ = 1
    max_ = 50
    answer = randint(min_, max_)
    title = "Guessing game"
    while guess != answer:
        message = "Guess a number between {} and {}".format(min_, max_)
        prev_guess = guess
        guess = eg.get_int(message=message, title=title,
                              default_value=guess, min_=min_ ,max_=max_)
        if guess is None:
            quitting = eg.yes_no_question("Do you want to quit?")
            guess = prev_guess
            if quitting:
                break
        elif guess < answer:
            title = "Too low"
            min_ = guess
        elif guess > answer:
            title = "Too high"
            max_ = guess
    else:
        message="Congratulations {}! {} was the answer.".format(name, guess)
        eg.show_message(message, title="You win!")


if __name__ == '__main__':
    eg.show_message("Temporarily setting the locale to Spanish")
    eg.set_locale('es')
    guessing_game()

