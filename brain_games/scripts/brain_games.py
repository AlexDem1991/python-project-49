import sys
sys.path.append("/home/alexdem122/python-project-49/brain_games")
sys.path.append("/home/vboxuser/python-project-49/brain_games")
from cli import welcome_user


def greet():
    """greeting user"""
    print("Welcome to the Brain Games!")


def main():
    greet()
    print(welcome_user())


if __name__ == "__main__":
    main()
