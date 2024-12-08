def slope_of_cubic(coefficients, x):
    slope = 3 * coefficients[0] * x * x + 2 * coefficients[1] * x + coefficients[2]
    return slope

if __name__ == '__main__':
    coeff_1 = int(input('Enter coefficient 1: '))
    coeff_2 = int(input('Enter coefficient 2: '))
    coeff_3 = int(input('Enter coefficient 3: '))
    coeff_4 = int(input('Enter coefficient 4: '))
    x = int(input('Enter x: '))

    slope = slope_of_cubic((coeff_1, coeff_2, coeff_3, coeff_4), x)
    print(slope)
