from logic import Game


def main():
    game = Game()
    for _ in range(game.attempts):
        bet = int(input("Введите вашу ставку: "))
        number = int(input(f"Введите число между {game.range_start} и {game.range_end}: "))
        if game.guess(bet, number):
            print("Вы угадали!")
        else:
            print("Вы не угадали.")
        print(f"Ваш текущий капитал: {game.capital}")


if __name__ == "__main__":
    main()
