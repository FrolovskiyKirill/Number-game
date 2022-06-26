import random
from art import logo

print(logo)

random_number = random.randint(1, 100)
level = input("Выберите уровень игры - 'easy' или 'hard': ")

if level == "easy":
  health_points = 10
  print(health_points)
elif level == "hard":
  health_points = 5
  print(health_points)

while health_points != 0:
  health_points -= 1
  user_number = int(input("Введите число: "))    
  if random_number < user_number and health_points != 0:    
    print("Ваше число больше, попробуйте еще раз!")    
    print(f"У вас осталось {health_points} попыток.")
  elif random_number > user_number and health_points != 0:    
    print("Ваше число меньше, попробуйте еще раз!")    
    print(f"У вас осталось {health_points} попыток.")
  elif random_number == user_number: 
    print("Вы победили!")
    health_points = 0
  else:
    print(f"Вы проиграли! Загаданное число: {random_number}")
