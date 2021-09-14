#!/usr/bin/env python3
# coding=utf-8


def main():
    a = int(input('Введите A: '))
    b = int(input('Введите B: '))
    x = int(input('Введите X: '))
    if x > 5:
        y = (5 * a * b) / (x ** 2 + a ** 2)
    else:
        y = 4 * ((a + b - x) ** 2)
    print("y = %.1f" % y)


if __name__ == '__main__':
    main()
