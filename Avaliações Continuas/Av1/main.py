import math

x1 = math.factorial(30)
x2 = math.factorial(40)
x3 = math.factorial(50)

# --
def celsiusToFahrenheit(c):
    return (c*9)/5 + 32

grausCelsius = float(input())  # não alterar esta linha
grausFahrenheit = celsiusToFahrenheit(grausCelsius)

# --
a = float(input())   # terei de fazer alguma conversão de valores?
b = float(input())
c = float(input())

cosA = (-a**2 + b**2 + c**2) / (2*b * c)
print('{0:.3f}'.format(cosA))

# --
def volCilindro(r, h):
    return math.pi * r**2 * h

h = float(input())
r = float(input())

volumeCilindro = volCilindro(r, h)
volumeCone = volumeCilindro / 3
ratio = volumeCilindro / volumeCone
print('{0:.4f}\n{1:.4f}\n{2:.4f}'.format(volumeCilindro, volumeCone, ratio))