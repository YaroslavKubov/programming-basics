signal_intensity = int(input("Введіть інтенсивність сигналу: "))

if signal_intensity >= 95:
    level = "Насичення фотоприймача"
elif signal_intensity >= 60:
    level = "Сильний сигнал"
elif signal_intensity >= 20:
    level = "Робочий діапазон"
else:
    level = "Слабкий сигнал"

mode = "Потрібна увага" if signal_intensity < 20 or signal_intensity >= 95 else "Звичайний режим"

print("Рівень:", level)
print("Режим:", mode)