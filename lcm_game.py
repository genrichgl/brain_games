import random
import math
from functools import reduce

def compute_lcm(x, y):
    return abs(x * y) // math.gcd(x, y)

def find_lcm_for_list(num_list):
    return reduce(compute_lcm, num_list)

def play_lcm_game(player):
    rounds = 3  
    for _ in range(rounds):
        num_set = [random.randint(1, 20) for _ in range(3)]
        
        print(f"Найдите НОК для чисел: {num_set}")
        
        correct_lcm = find_lcm_for_list(num_set)
        
        while True: 
            try:
                guess = int(input("Ваш ответ: "))
            except ValueError:
                print("Введите целое число.")
                continue  
            
            if guess == correct_lcm:
                print("Вы правы! Молодцы!")
                break  
            else:
                print(f"Неверно. Ответ был: {correct_lcm}. Попробуйте ещё раз.")

    print(f"Отлично, {player}! Вы победили в игре!")

if __name__ == "__main__":
    play_lcm_game("Игрок")
