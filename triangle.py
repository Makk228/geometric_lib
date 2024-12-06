import math
def area(a, b, c):
    p=(a+b+c)/2
    '''Функция принимает 2  аргумента a, b, c (все int) и возвращает
        площадь тркугольника по формуле Герона
        math.sqrt(p * (p-a) * (p-b) * (p-c))  (float)
    '''
    return  math.sqrt(p * (p-a) * (p-b) * (p-c))


def perimeter(a, b, c):
    ''' Функция принимает 3  аргумента a b c (все int) и возвращает
        периметр треугольника по формуле a + b + c (int).
    '''
    return a + b + c
    
