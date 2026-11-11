import math

radius_mm = float(input("Введіть радіус лінзи в мм: "))
area_mm2 = math.pi * radius_mm ** 2

print(f"Радіус: {radius_mm:.2f} мм")
print(f"Площа: {area_mm2:.2f} мм²")