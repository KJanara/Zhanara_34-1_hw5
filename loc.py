import random

# def play_slot(money):
#   print(f'You have money: {money}')
#
#   while True:
#     bet = int(input('How many dollar do you want to bet'))
#     if

def main():
  initial_money = 1000  # Начальный капитал
  money = initial_money

  while money > 0:
    money = play_round(money)
    if money <= 0:
      print("Ваш капитал исчерпан.")
      break

    play_again = input("Хотите сыграть еще раз (да/нет)? ").lower()
    if play_again != "да":
      break

  if money > initial_money:
    print(f"Поздравляем, вы в выигрыше! Ваш капитал: ${money}")
  else:
    print(f"Вы в проигрыше. Ваш капитал: ${money}")

def play_round(money):
  print(f"У вас есть ${money}.")

  # Запрос ставки
  while True:
    bet = int(input("Сколько долларов вы хотите поставить (минимум $1): "))
    if 1 <= bet <= money:
      break
    else:
      print("Недопустимая ставка. Введите корректное значение.")

