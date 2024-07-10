class Fraction:

    @staticmethod
    def _gcd(x, y):
        while y:
            x, y = y, x % y
        return abs(x)

    def _reduction(self):
        s = self._gcd(self._x, self._y)
        self._x //= s
        self._y //= s
        if self._y < 0:
            self._x = -self._x
            self._y = abs(self._y)
        return self

    def __init__(self, *args):
        match len(args):
            case 1:

                if isinstance(args[0], int):
                    self._x = args[0]
                    self._y = 1

                elif isinstance(args[0], str) and '/' in args[0]:
                    dr = list(map(int, args[0].split('/')))
                    self._x = dr[0]
                    self._y = dr[1]

                else:
                    self._x = int(args[0])
                    self._y = 1

            case 2:
                self._x = args[0]
                self._y = args[1]

        self._reduction()

    def numerator(self, *args):
        match len(args):
            case 0:
                return abs(self._x)
            case 1:
                if self._x < 0:
                    self._x = args[0] * (-1)
                else:
                    self._x = args[0]
                self._reduction()

    def denominator(self, *args):
        match len(args):
            case 0:
                return self._y
            case 1:
                self._y = args[0]
                self._reduction()

    def __str__(self):
        return f'{self._x}/{self._y}'

    def __repr__(self):
        return f"Fraction('{self._x}/{self._y}')"

    def __neg__(self):
        return Fraction(-self._x, self._y)

    def __add__(self, other):
        other = self._rec(other)
        return Fraction(self._x * other._y + other._x * self._y, self._y * other._y)._reduction()

    def __sub__(self, other):
        other = self._rec(other)
        return Fraction(self._x * other._y - other._x * self._y, self._y * other._y)._reduction()

    def __iadd__(self, other):
        other = self._rec(other)
        self._x = self._x * other._y + other._x * self._y
        self._y = other._y * self._y
        self._reduction()
        return self

    def __isub__(self, other):
        other = self._rec(other)
        self._x = self._x * other._y - other._x * self._y
        self._y = other._y * self._y
        self._reduction()
        return self

    def __mul__(self, other):
        other = self._rec(other)
        return Fraction(self._x * other._x, self._y * other._y)._reduction()

    def __truediv__(self, other):
        other = self._rec(other)
        return Fraction(self._x * other._y, self._y * other._x)._reduction()

    def __imul__(self, other):
        other = self._rec(other)
        self._x = self._x * other._x
        self._y = self._y * other._y
        self._reduction()
        return self

    def __itruediv__(self, other):
        other = self._rec(other)
        self._x = self._x * other._y
        self._y = self._y * other._x
        self._reduction()
        return self

    def reverse(self):
        return Fraction(self._y, self._x)

    def _compare(self, tfrac):
        a = self._x * tfrac._y
        b = tfrac._x * self._y
        return a, b

    def _rec(self, frac):
        if isinstance(frac, int) or isinstance(frac, str):
            frac = Fraction(frac)
        return frac

    def __lt__(self, other):
        other = self._rec(other)
        return self._compare(other)[0] < self._compare(other)[1]

    def __le__(self, other):
        other = self._rec(other)
        return self._compare(other)[0] <= self._compare(other)[1]

    def __eq__(self, other):
        other = self._rec(other)
        return self._x == other._x and self._y == other._y

    def __ne__(self, other):
        other = self._rec(other)
        return self._x != other._x and self._y != other._y

    def __gt__(self, other):
        other = self._rec(other)
        return self._compare(other)[0] > self._compare(other)[1]

    def __ge__(self, other):
        other = self._rec(other)
        return self._compare(other)[0] >= self._compare(other)[1]

    def __radd__(self, other):
        other = self._rec(other)
        return Fraction(self._x * other._y + other._x * self._y, self._y * other._y)._reduction()

    def __rsub__(self, other):
        other = self._rec(other)
        return Fraction(other._x * self._y - self._x * other._y, self._y * other._y)._reduction()

    def __rmul__(self, other):
        other = self._rec(other)
        return Fraction(self._x * other._x, self._y * other._y)._reduction()

    def __rtruediv__(self, other):
        other = self._rec(other)
        return Fraction(other._x * self._y, self._x * other._y)._reduction()


