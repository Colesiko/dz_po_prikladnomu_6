def main():
  kolvo_krit = input("Введите колличество критериев: ")

  bukv = kolvo_krit.isdigit()
  if bukv == False:  # проверка на буквы
    while bukv == False:
      print("Введите число большее или равное 1(цифрами): ")
      kolvo_krit = input()
      bukv = str.isnumeric(kolvo_krit)
  kolvo_krit = int(kolvo_krit)

  while kolvo_krit == 0:
    kolvo_krit = input("Введите число большее или равное 1(цифрами): ")
    bukv = kolvo_krit.isdigit()
    if bukv == False:  # проверка на буквы
      while bukv == False:
        print("Введите число большее или равное 1(цифрами): ")
        kolvo_krit = input()
        bukv = str.isnumeric(kolvo_krit)
    kolvo_krit = int(kolvo_krit)

  mas = [[0 for j in range(kolvo_krit)] for i in range(kolvo_krit)]
  for i in range(kolvo_krit):         #метод анализа иерархий Томаса Саати для одного уровня
    for j in range(kolvo_krit):
      if i == j:
        mas[i][j] = 1
      elif i < j:
        while True:
          mas[i][j] = input(f"Введите коэфициент сравнения {i+1} к {j+1}(от 0 до 9): ")

          bukv = mas[i][j].isdigit()
          if bukv == False:  # проверка на буквы
            while bukv == False:
              print("Введите число от 1 до 9(цифрами): ")
              mas[i][j] = input()
              bukv = str.isnumeric(mas[i][j])
          mas[i][j] = int(mas[i][j])

          if mas[i][j] > 9 or mas[i][j] <= 0:
            print("Недопустимое значение, попробуйте ещё раз\n")
          else:
            break
  for i in range(kolvo_krit):
    for j in range(kolvo_krit):
      if i > j:
        mas[i][j] = 1 / mas[j][i]

  ves = []
  sum = 0
  print("Итоговая матрица:")      #вывод матрицы
  for i in range(kolvo_krit):
    for j in range(kolvo_krit):
      print(f"{mas[i][j]:.2f}  ", end="")
      sum += mas[i][j]
    ves.append(sum)
    sum = 0
    print()
  for i in range(kolvo_krit):
    sum += ves[i]
  print("Весовые коэфициенты: ", end="")
  for i in range(kolvo_krit):
    print(f"{i+1} - {ves[i]/sum:.2f}, ", end="")

if __name__ == "__main__":
  main()
