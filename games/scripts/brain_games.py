from games import cli


def greet():
    """greeting user"""
    print("Welcome to the Brain Games!")


def main():
    greet()
    cli.welcome_user()

if __name__ == "__main__":
    main()
