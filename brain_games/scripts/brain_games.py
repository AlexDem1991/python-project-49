from brain_games import cli

def greet():
    print("Welcome to the Brain Games!")

def main():
    greet()
    print(cli.welcome_user())

if __name__=="__main__":
    main()
