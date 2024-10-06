import random

def generate_progression(length, first_term, step):
    return [first_term * (step ** index) for index in range(length)]

def conceal_element(sequence):
    idx = random.randint(0, len(sequence) - 1)
    missing_value = sequence[idx]
    sequence[idx] = '..'
    return sequence, missing_value

def play_progression_game(player):
    attempts = 3  
    for _ in range(attempts):
        length = random.randint(5, 10)
        start = random.randint(1, 10)
        step = random.randint(2, 5)
        
        progression = generate_progression(length, start, step)
        masked_progression, correct_value = conceal_element(progression)
        
        print("Прогрессия:")
        print(' '.join(map(str, masked_progression)))

        while True:  
            try:
                guess = float(input("Какое число скрыто? "))
            except ValueError:
                print("Введите число.")
                continue  
            
            if guess == correct_value:
                print("Отлично! Вы угадали!")
                break  
            else:
                print(f"Неправильно. Правильное число: {correct_value}. Пробуйте снова.")

    print(f"Молодец, {player}! Вы победили в игре!")

if __name__ == "__main__":
    play_progression_game("Игрок")
