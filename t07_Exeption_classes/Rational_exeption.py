import math

class RationalError(ZeroDivisionError):

    def __init__(self, message="Знаменник раціонального числа не може дорівнювати нулю"):
        self.message = message
        super().__init__(self.message)


class Rational:
    def __init__(self, n, d=1):
        if d == 0:
            raise RationalError(f"Спроба створення дробу {n}/{d}. Знаменник не може бути 0.")

        common = math.gcd(n, d)
        self.n = n // common
        self.d = d // common

        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __repr__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"



try:
    bad_number = Rational(5, 0)
except RationalError as e:
    print(f"Перехоплено специфічну помилку: {e}")