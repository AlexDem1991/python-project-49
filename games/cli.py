import prompt


def welcome_user():
    name = prompt.string("May i have your name? ")
    return f"Hello, {name}!"


def greeting():
    """greeting user"""
    print("Welcome to the Brain Games!")
    name = prompt.string("May i have your name? ")
    print(f"Hello, {name}!")
    return name


def ending_game(name, answer, answer_game, user_answer):
    if answer:
        print(f"Congratulation, {name}!")
    else:
        print(f"{user_answer} is wrong answer ;(. ", end="")
        print(f"Correct answer was {answer_game}")
        print(f"Let't try again, {name}.")


def main():
    welcome_user()


if __name__ == "__main__":
    main()
