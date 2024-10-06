import progression_game
import lcm_game
import engine

def main():
    print("Добро пожаловать в Игры для ума!")
    player_name = input("Как вас зовут? ")
    print(f"Приветствую, {player_name}!")
    
    game_options = {
        '1': lambda: engine.run_game(lambda: progression_game.play_progression_game(player_name)),
        '2': lambda: engine.run_game(lambda: lcm_game.play_lcm_game(player_name)),
    }
    
    while True:
        print("\nВыберите игру:")
        print("1. Прогрессия")
        print("2. НОК")
        print("3. Выйти")

        user_choice = input("Введите номер (1-3): ")

        if user_choice in game_options:
            game_options[user_choice]()
        elif user_choice == '3':
            print("Спасибо за игру, до встречи!")
            break
        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
