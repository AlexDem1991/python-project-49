from games import cli
import random


def game():
    print("What is the result of the expression?")
    for i in range(3):
        symbol = random.choice(['*', '-', '+'])
        num_1 = str(random.randint(1, 100))
        num_2 = str(random.randint(1, 100))
        print(f"Question: {num_1} {symbol} {num_2}")
        result_str = num_1+symbol+num_2
        result_int = eval(result_str)
        answer_user = input("Your answer: ")
        try:
            if result_int == int(answer_user):
                print("Correct!")
                continue
            else:
                return False, result_int, answer_user
        except ValueError:
            return False, result_int, answer_user
    else:
        return True, result_int, answer_user


def main():
    name = cli.greeting()
    answer, result_int, answer_user = game()
    cli.ending_game(name, answer, result_int, answer_user)


if __name__ == "__main__":
    main()
