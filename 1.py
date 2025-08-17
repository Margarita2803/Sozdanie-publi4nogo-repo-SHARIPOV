n = int(input("Введите число: "))
even_numbers = list(filter(lambda x: x % 2 == 0, range(n + 1)))
print(even_numbers)
