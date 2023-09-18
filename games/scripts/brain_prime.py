import random
from games import cli


def game():
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    divisors = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31]
    for i in range(3):
        question = random.randint(1, 30)
        print(f"Question: {question}")
        answer_user = input("Your answer: ")
        for i in divisors:
            if question == i:
                answer_game = "yes"
                break
            elif question % i == 0:
                answer_game = "no"
                break
            else:
                answer_game = "yes"
        if answer_game == answer_user:
            print("Correct!")
            continue
        else:
            return False, answer_game, answer_user
    else:
        return True, answer_game, answer_user


def main():
    name = cli.greeting()
    answer, answer_game, answer_user = game()
    cli.ending_game(name, answer, answer_game, answer_user)


if __name__ == "__main__":
    main()
