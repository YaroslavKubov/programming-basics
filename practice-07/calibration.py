
def calibrate(raw_value, gain, offset):
    return raw_value * gain + offset


def is_in_range(value, minimum, maximum):
    return minimum <= value <= maximum


raw_value = 510
gain = 0.02
offset = -0.2
minimum = 0.0
maximum = 12.0

calibrated_value = calibrate(raw_value, gain, offset)
in_range = is_in_range(calibrated_value, minimum, maximum)

print("Каліброване значення:", calibrated_value)

if in_range:
    print("Статус: у допустимому діапазоні")
else:
    print("Статус: поза допустимим діапазоном")
