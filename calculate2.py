import numpy as np
def f(x):
    return (2**x / (abs(x**2 + 1))) + np.log2(abs(x) + 1)
a = float(input("Введіть початок інтервалу (a): "))
b = float(input("Введіть кінець інтервалу (b): "))
h = float(input("Введіть крок (h): "))
x = a
values = []
while x <= b:
    y = f(x)
    values.append((x, y))
    x += h
print("\nЗначення функції:")
for val in values:
    print(f"f({val[0]}) = {val[1]}")
max_val = max(values, key=lambda item: item[1])
min_val = min(values, key=lambda item: item[1])
print(f"\nМаксимальне значення функції: f({max_val[0]}) = {max_val[1]}")
print(f"Мінімальне значення функції: f({min_val[0]}) = {min_val[1]}")

