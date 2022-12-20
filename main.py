def main():
  kolvo_krit = int(input("Введите колличество критериев: "))
  mas = [[0 for j in range(kolvo_krit)] for i in range(kolvo_krit)]
  for i in range(kolvo_krit):
    for j in range(kolvo_krit):
      if i == j:
        mas[i][j] = 1
      elif i < j:
        while True:
          mas[i][j] = float(input(f"Введите коэфициент сравнения {i+1} к {j+1}(от 0 до 9): "))
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
  print("Итоговая матрица:")
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