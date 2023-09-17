import random
import sys
sys.path.append("/home/alexdem122/python-project-49/brain_games")
sys.path.append("/home/vboxuser/python-project-49/brain_games")
from cli import greeting, ending_game


def maked_sequence():
    finish = random.randint(5, 11)
    step = random.randint(1, 10)
    start = random.randint(1, 50)
    i = 0
    result = []
    while i != finish:
        result.append(str(start))
        start += step
        i += 1
    return result


def switch_num(sequence):
    element = random.choice(sequence)
    for i in range(len(sequence)):
        if sequence[i] == element:
            sequence[i] = ".."
    return sequence, element


def game():
    print("What number is missing in the progression?")
    for i in range(3):
        full_list = maked_sequence()
        secret_list, secret_element = switch_num(full_list)
        print(f"Question: {secret_list}")
        answer_user = input("Yior_answer: ")
        if secret_element == answer_user:
            print("Correct!")
            continue
        else:
            return False, secret_element, answer_user
    else:
        return True, secret_element, answer_user


def main():
    name = greeting()
    answer, secret_element, answer_user = game()
    ending_game(name, answer, secret_element, answer_user)


if __name__ == "__main__":
    main()
