num = input("Введіть чотирицифрове число: ")
digits = [int(digit) for digit in num]
max_digit = max(digits)
min_digit = min(digits)
print(f"Найбільша цифра: {max_digit}")
print(f"Найменша цифра: {min_digit}")