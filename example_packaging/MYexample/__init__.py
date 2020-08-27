# A example module
from datetime import *
import random

__version__ = '0.1'
def smallest(a, b, c, d, e):
    minst = min(a, b, c, d, e)
    print('smallest number: ' + str(minst))

def biggest(a, b, c, d, e):
    störst = max(a, b, c, d, e)
    print('biggest number: ' + str(störst))


def seconds_day(a):
    hours = a * 24
    minute = hours * 60
    second = minute * 60
    print(second)

    
def hello():
    print('Hi this world')
    name = input('What\'s your name? write it here:')
    print('Hi ' + name)


def fib(n):    # write Fibonacci series up to n
    a, b = 0, 1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
def fib2(n):  # return Fibonacci series up to n
    result = []
    a, b = 0, 1
    while a < n:
        result.append(a)    # see below
        a, b = b, a+b
    return result




def cheeseshop(kind, *arguments, **keywords):
    print("-- Do you have any", kind, "?")
    kind1 = "-- I'm sorry, we're all out of " + kind
    kind2 = "-- Here you are your " + kind
    both = [kind1, kind2]
    ct = random.choice(both)
    print(ct)
    for arg in arguments:
        print(arg)
    print("-" * 40)
    for kw in keywords:
        print(kw, ":", keywords[kw])

def number(a, b, c):
    lista = [a, b, c]
    num = random.choice(lista)
    print(num)
#Y.cheeseshop("Limburger", "It's very runny, sir.",
#           "It's really very, VERY runny, sir.",
#           shopkeeper="Mandi Yang",
#           client="John Cleese",
#           sketch="Mac Donald")

def wekday(year, month, day):
    print(date(year, month, day).weekday())       
    if date(year, month, day).weekday() == 0:
        print('Monday')
    elif date(year, month, day).weekday() == 1:   #weekday on de date#
        print('Tuesday')
    elif date(year, month, day).weekday() == 2:
        print('Wednesday')
    elif date(year, month, day).weekday() == 3:
        print('Thursday')
    elif date(year, month, day).weekday() == 4:
        print('Friday')
    elif date(year, month, day).weekday() == 5:
        print('Saturday')
    elif date(year, month, day).weekday() == 6:
        print('Sunday')
    else:
        exit()
def prime(a, b):
    for n in range(a, b):
        for x in range(2, n):
            if n % x == 0:
                print(n, 'equals', x, '*', n//x)
                break
        else:
            # loop fell through without finding a factor
            print(n, 'is a prime number')       

PI = 3.141592653589793   # global constant -- only place the value of PI is set

def circleArea(radius):
    print('PI = ' + str(PI))
    return PI*radius*radius    # use value of global constant PI

def circleCircumference(radius):
    print('PI = ' + str(PI))
    return 2*PI*radius

class Card:
    def __init__(self, color, value):
        self._color = color
        self._value = value

    def get_color(self):
        return self._color

    def get_value(self):
        return self._value

    ftab = '\N{BLACK CLUB SUIT}\N{WHITE DIAMOND SUIT}'\
               '\N{WHITE HEART SUIT}\N{BLACK SPADE SUIT}'

    vtab = ('E', '2', '3', '4', '5', '6', '7',
                '8', '9', '10', 'Kn', 'D', 'K')

    def __str__(self):
        return Card.ftab[self._color-1] + ' ' +\
               Card.vtab[self._value-1]

class Cardgame:
    def __init__(self):
        self._game = []
        for i in range(1, 5):
            for j in range(1, 14):
                self._game.append(Card(i, j))
        random.shuffle(self._game)

    def give(self):
        if len(self._game) > 0:
            return self._game.pop()
        else:
            return None

