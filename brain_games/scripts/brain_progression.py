import random
import prompt
from brain_games.scripts.brain_games import get_welcome
from brain_games.cli import welcome_user


def get_progression():
    name =  welcome_user()
    print('What number is missing in the progression?')
    i = 0
    while i <= 2:
        a = []
        num1 = random.randint(25, 60)
        num2 = random.randint(1, 5)
        step = random.randint(2, 5)
        for n in range(num2, num1, step):
            a.append(n)
        s = str(random.choice(a))
        p = " ".join(str(x) for x in a)
        new_p = p.replace(s, '..', 1)
        print(f'Question: {new_p}')
        answer = prompt.string('Your answer: ')
        if answer == s:
            print('Correct!')
            i += 1
        else:
            print(f"'{answer}' is wrong answer ;(. "
                  f"Correct answer was '{s}'.")
            print("Let's try again, " + name + "!")
            break
        if i == 3:
            print('Congratulations, ' + name + '!')


def main():
    get_welcome()
    get_progression()


if __name__ == '__main__':
    main()
