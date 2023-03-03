def calculate_EKUB(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def calculate_EKUK(a, b):
    return (a * b) // calculate_EKUB(a, b)


print(f'EKUK {calculate_EKUK(4, 6)}, EKUB {calculate_EKUB(4,6)}')
