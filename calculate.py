import numpy as np
import matplotlib.pyplot as plt

def f(x):
    return (2**x / (abs(x**2 + 1))) + np.log2(abs(x) + 1)
a = float(input("Введіть початок інтервалу (a): "))
b = float(input("Введіть кінець інтервалу (b): "))
h = float(input("Введіть розмір кроку (h): "))
x = np.arange(a, b, h)
y = f(x)
values = list(y)
print("Значення функції:")
for val in values:
    print(val)
print(f"Максимальне значення: {max(values)}")
print(f"Мінімальне значення: {min(values)}")