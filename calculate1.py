import numpy as np

def f(x):
    return (2**x / (abs(x**2 + 1))) + np.log2(abs(x) + 1)

a = float(input("Введіть початок інтервалу (a): "))
b = float(input("Введіть кінець інтервалу (b): "))
h = float(input("Введіть крок (h): "))

x = np.arange(a, b, h)
y = f(x)

print("Значення функції:")
for i in range(len(x)):
    print(f"f({x[i]}) = {y[i]}")
