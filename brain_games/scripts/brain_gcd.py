import random
import prompt
from brain_games.scripts.brain_games import get_welcome
from brain_games.cli import welcome_user


def get_gcd():
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')
    i = 0
    a = 0
    while i <= 2:
        num1 = random.randint(20, 100)
        num2 = random.randint(1, 20)
        print(f'Question: {num1} {num2}')
        answer = prompt.integer('Your answer: ')
        for n in range(1, num2 + 1):
            if num1 % n == 0 and num2 % n == 0:
                a = n
        if answer == a:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{a}'.")
            print("Let's try again, " + name + "!")
            break
        if i == 3:
            print('Congratulations, ' + name + '!')


def main():
    get_welcome()
    get_gcd()


if __name__ == '__main__':
    main()
