import random
import prompt
from brain_games.scripts.brain_games import get_welcome
from brain_games.cli import welcome_user


def is_prime():
    name =  welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    i = 0
    while i <= 2:
        num = random.randint(1, 100)
        count = 0
        print(f'Question: {num}')
        for n in range(1, num + 1):
            if num % n == 0:
                count += 1
        if count == 2:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        if answer == correct_answer:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{correct_answer}'.")
            print("Let's try again, " + name + "!")
            break
        if i == 3:
            print('Congratulations, ' + name + '!')


def main():
    get_welcome()
    is_prime()


if __name__ == '__main__':
    main()
