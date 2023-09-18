import random
import prompt


def greeting():
    """greeting user"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May i have your name? ")
    print(f"Hello, {name}!")
    return name


def game():
    print('Answer "yes" if the number is even, otherwise answer "no"')
    for i in range(3):
        number = random.randint(1, 100)
        print(f"Question: {number}")
        user_answer = prompt.string("Your answer: ")
        if number % 2 == 0:
            answer_game = "yes"
        elif number % 2 == 1:
            answer_game = "no"
        if answer_game == user_answer:
            print("Correct!")
            continue
        elif answer_game != user_answer:
            return False, answer_game, user_answer
    else:
        return True, answer_game, user_answer


def ending_game(name, answer, answer_game, user_answer):
    if answer:
        print(f"Congratulation, {name}!")
    else:
        print(f"{user_answer} is wrong answer ;(. ", end="")
        print(f"Correct answer was {answer_game}")
        print(f"Let't try again, {name}.")


def main():
    name = greeting()
    answer, answer_game, user_answer = game()
    ending_game(name, answer, answer_game, user_answer)


if __name__ == "__main__":
    main()
