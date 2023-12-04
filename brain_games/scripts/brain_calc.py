import random
import prompt
from brain_games.scripts.brain_games import get_welcome
from brain_games.cli import welcome_user


def get_calc():
    name =  welcome_user()
    print('What is the result of the expression?')
    i = 0
    m_oper = ['+', '-', '*']
    while i <= 2:
        num1 = random.randint(10, 25)
        num2 = random.randint(1, 10)
        oper = random.choice(m_oper)
        print(f'Question: {num1} {oper} {num2}')
        answer = prompt.integer('Your answer: ')
        if oper == '+':
            if answer == num1 + num2:
                print('Correct!')
                i += 1
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{num1 + num2}'.")
                print("Let's try again, " + name + "!")
                break
        elif oper == '-':
            if answer == num1 - num2:
                print('Correct!')
                i += 1
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{num1 - num2}'.")
                print("Let's try again, " + name + "!")
                break
        elif oper == '*':
            if answer == num1 * num2:
                print('Correct!')
                i += 1
            else:
                print(f"'{answer}' is wrong answer ;(. "
                      f"Correct answer was '{num1 * num2}'.")
                print("Let's try again, " + name + "!")
                break
        if i == 3:
            print('Congratulations, ' + name + '!')


def main():
    get_welcome()
    get_calc()


if __name__ == '__main__':
    main()
