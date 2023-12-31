from games import cli
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


def sorted(num1, num2):
    if max(num1, num2) % min(num1, num2) == 0:
        game_answer = min(num1, num2)
    else:
        first = devided(num1)
        second = devided(num2)
        game_answer = max(list(set(first) & set(second)))
    return game_answer


def game():
    print("Find the greatest common divisir of given numbers.")
    for i in range(3):
        first_num = random.randint(1, 100)
        second_num = random.randint(1, 100)
        game_answer = sorted(first_num, second_num)
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
    name = cli.greeting()
    answer, game_answer, user_answer = game()
    cli.ending_game(name, answer, game_answer, user_answer)


if __name__ == "__main__":
    main()
