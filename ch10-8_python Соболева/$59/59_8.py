# Напишите процедуру, которая принимает параметр – натуральное число N – и выводит на
# экран квадрат из звездочек со стороной N.

def show_square(number):
    i = 0
    while i < number:
        print('*' * number)
        i += 1

show_square(int(input('print number --> ')))