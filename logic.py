import random
from  decouple import config


def play_round(money):
  print(f"У вас есть ${money}.")

  while True:
    bet = int(input("Сколько долларов вы хотите поставить: "))
    if 1 <= bet <= money:
      break
    else:
      print("Недопустимая ставка. Введите корректное значение.")

  selected_slot = random.randint(1, 30)
  print(f"Вы выбрали слот {selected_slot}.")

  winning_slot = random.randint(1, 30)
  print(f"Выигрышный слот: {winning_slot}")

  if selected_slot == winning_slot:
    money += bet
    print(f"Поздравляем! Вы выиграли ${bet}.")
  else:
    money -= bet
    print(f"Увы, вы проиграли ${bet}.")

  return money


def main():
  initial_money = config('MY_MONEY', cast=int)
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


if __name__ == "__main__":
  main()
