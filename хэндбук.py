class Point: #A 5.1
    def __init__(self, x, y):
        self.x = x
        self.y = y



class Point: #B 5.1
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, x, y):
        self.x += x
        self.y += y

    def length(self, point):
        d = ((self.x - point.x)**2 + (self.y - point.y)**2)**0.5
        return round(d, 2)


class RedButton: #C 5.1
    def __init__(self):
        self.counter = 0

    def click(self):
        print("Тревога!")
        self.counter += 1

    def count(self):
        return self.counter



class Programmer: #D 5.1
    def __init__(self, name, position):
        self.name = name
        self.position = position
        self.hours_worked = 0
        if position == "Junior":
            self.hourly_rate = 10
        elif position == "Middle":
            self.hourly_rate = 15
        elif position == "Senior":
            self.hourly_rate = 20
        self.salary = 0

    def work(self, time):
        self.hours_worked += time
        self.salary += time * self.hourly_rate

    def rise(self):
        if self.position == "Junior":
            self.position = "Middle"
            self.hourly_rate = 15
        elif self.position == "Middle":
            self.position = "Senior"
            self.hourly_rate = 20
        elif self.position == "Senior":
            self.hourly_rate += 1

    def info(self):
        return f"{self.name} {self.hours_worked}ч. {self.salary}тгр."


class Rectangle: #E 5.1
    def __init__(self, point1, point2):
        self.x1, self.y1 = point1
        self.x2, self.y2 = point2

    def perimeter(self):
        a = abs(self.x1 - self.x2)
        b = abs(self.y1 - self.y2)
        return round(2 * (a + b), 2)

    def area(self):
        a = abs(self.x1 - self.x2)
        b = abs(self.y1 - self.y2)
        return round(a * b, 2)

class Queue: #I 5.1
    def __init__(self):
        self.__queue = []

    def push(self, item):
        self.__queue.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('Queue is empty')
        return self.__queue.pop(0)

    def is_empty(self):
        return len(self.__queue) == 0


class Stack: #J 5.1
    def __init__(self):
        self.__stack = []

    def push(self, item):
        self.__stack.append(item)

    def pop(self):
        if self.is_empty():
            raise ValueError('Stack is empty')
        return self.__stack.pop()

    def is_empty(self):
        return len(self.__stack) == 0


class Point: #A 5.2
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)


class Point: #B 5.2
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def length(self, point):
        distance = ((self.x - point.x) ** 2 + (self.y - point.y) ** 2) ** 0.5
        return round(distance, 2)


class PatchedPoint(Point):
    def __init__(self, *args):
        if len(args) == 0:
            super().__init__(0, 0)
        elif len(args) == 1:
            super().__init__(args[0][0], args[0][1])
        elif len(args) == 2:
            super().__init__(*args)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def __repr__(self):
        return f'PatchedPoint({self.x}, {self.y})'


class Fraction: #D 5.2
    def __init__(self, numerator, denominator=1):
        if type(numerator) == str:
            numerator, denominator = map(int, numerator.split('/'))
        gcd = self._gcd(numerator, denominator)
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def numerator(self, number=None):
        if number is None:
            return self._numerator
        gcd = self._gcd(number, self._denominator)
        self._numerator = number // gcd
        self._denominator = self._denominator // gcd
        return self._numerator

    def denominator(self, number=None):
        if number is None:
            return self._denominator
        gcd = self._gcd(self._numerator, number)
        self._numerator = self._numerator // gcd
        self._denominator = number // gcd
        return self._denominator

    def __str__(self):
        return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"


class Fraction: #F 5.2
    def __init__(self, numerator, denominator=1):
        if type(numerator) == str:
            numerator, denominator = map(int, numerator.split('/'))
        if denominator < 0:
            numerator = -numerator
            denominator = -denominator
        gcd = self._gcd(abs(numerator), abs(denominator))
        self._numerator = numerator // gcd
        self._denominator = denominator // gcd

    def _gcd(self, a, b):
        if b == 0:
            return a
        return self._gcd(b, a % b)

    def numerator(self, number=None):
        if number is None:
            return self._numerator
        if number < 0:
            self._numerator = -abs(number)
        else:
            self._numerator = abs(number)
        gcd = self._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // gcd
        self._denominator = self._denominator // gcd
        return self._numerator

    def denominator(self, number=None):
        if number is None:
            return self._denominator
        if number == 0:
            raise ValueError("Denominator can't be equal to zero.")
        if number < 0:
            self._denominator = -abs(number)
        else:
            self._denominator = abs(number)
        gcd = self._gcd(self._numerator, self._denominator)
        self._numerator = self._numerator // gcd
        self._denominator = self._denominator // gcd
        return self._denominator

    def __str__(self):
        if self._denominator == 1:
            return f"{self._numerator}"
        else:
            return f"{self._numerator}/{self._denominator}"

    def __repr__(self):
        return f"Fraction({self._numerator}, {self._denominator})"

    def __neg__(self):
        return Fraction(-self._numerator, self._denominator)

    def __add__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for +: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __sub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for -: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        return Fraction(new_numerator, new_denominator)

    def __iadd__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for +=: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator + self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        gcd = self._gcd(abs(new_numerator), abs(new_denominator))
        self._numerator = new_numerator // gcd
        self._denominator = new_denominator // gcd
        return self

    def __isub__(self, other):
        if isinstance(other, int):
            other = Fraction(other)
        elif not isinstance(other, Fraction):
            raise TypeError("Unsupported operand type(s) for -=: 'Fraction' and '{}'".format(type(other).__name__))
        new_numerator = self._numerator * other._denominator - self._denominator * other._numerator
        new_denominator = self._denominator * other._denominator
        gcd = self._gcd(abs(new_numerator), abs(new_denominator))
        self._numerator = new_numerator // gcd
        self._denominator = new_denominator // gcd
        return self
