import sys
sys.path.append("/home/alexdem122/python-project-49/brain_games")
sys.path.append("/home/vboxuser/python-project-49/brain_games")
from cli import greeting, ending_game
import random


def devided(num):
    i = 2
    result = [1]
    while num != 1:
        if num % i == 0:
            result.append(i)
            num = num / i
        else:
            i += 1
    return result


def game():
    print("Find the greatest common divisir of given numbers.")
    for i in range(3):
        first_num = random.randint(1,100)
        second_num = random.randint(1, 100)
        if max(first_num, second_num) % min(first_num,second_num) == 0:
            game_answer = min(first_num,second_num)
        else:
            first = devided(first_num)
            second = devided(second_num)
            game_answer = max(list(set(first) & set(second)))
        print(f"Question: {first_num} {second_num}")
        user_answer = input("Your answer: ")
        try:
            if game_answer == int(user_answer):
                print("Correct!")
                continue
            else:
                return False, game_answer, user_answer
        except ValueError:
            return False, game_answer, user_answer
    else:
        return True, game_answer, user_answer
    
def main():
    name = greeting()
    answer, game_answer, user_answer = game()
    ending_game(name, answer, game_answer, user_answer)


if __name__ == "__main__":
    main()

