import random
import prompt
from brain_games.scripts.brain_games import get_welcome
from brain_games.cli import welcome_user


def is_even():
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    i = 0
    while i <= 2:
        num = random.randint(1, 100)
        print(f'Question: {num}')
        answer = prompt.string('Your answer: ')
        if num % 2 == 0:
            correct_answer = 'yes'
            if answer == correct_answer:
                print('Correct!')
                i += 1
            else:
                print(f"{answer} is wrong answer ;(. "
                      f"Correct answer was {correct_answer}")
                print("Let's try again, " + name + "!")
                break
        elif num % 2 != 0:
            correct_answer = 'no'
            if answer == correct_answer:
                print('Correct!')
                i += 1
            else:
                print(f"{answer} is wrong answer ;(. "
                      f"Correct answer was {correct_answer}")
                print("Let's try again, " + name + "!")
                break
        if i == 3:
            print('Congratulations, ' + name + '!')


def main():
    get_welcome()
    is_even()


if __name__ == '__main__':
    main()
