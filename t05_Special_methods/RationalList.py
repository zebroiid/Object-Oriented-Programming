import math


class Rational:

    def __init__(self, n, d=1):
        if d == 0:
            raise ValueError("Знаменник не може бути нулем.")

        common = math.gcd(n, d)
        self.n = n // common
        self.d = d // common

        if self.d < 0:
            self.n *= -1
            self.d *= -1

    def __add__(self, other):
        if isinstance(other, int):
            other = Rational(other)
        if isinstance(other, Rational):
            new_n = self.n * other.d + other.n * self.d
            new_d = self.d * other.d
            return Rational(new_n, new_d)
        return NotImplemented

    def __radd__(self, other):
        return self.__add__(other)

    def __repr__(self):
        return f"{self.n}/{self.d}" if self.d != 1 else f"{self.n}"


class RationalList:

    def __init__(self, items=None):
        self._data = []
        if items:
            for item in items:
                self._add_to_internal(item)

    def _add_to_internal(self, item):
        if isinstance(item, int):
            self._data.append(Rational(item))
        elif isinstance(item, Rational):
            self._data.append(item)
        else:
            raise TypeError("Елементом списку може бути лише Rational або int")

    def __getitem__(self, index):
        return self._data[index]

    def __setitem__(self, index, value):
        if isinstance(value, int):
            value = Rational(value)
        if not isinstance(value, Rational):
            raise TypeError("Значення має бути типу Rational або int")
        self._data[index] = value

    def __len__(self):
        return len(self._data)

    # +
    def __add__(self, other):
        new_list = RationalList(self._data)
        if isinstance(other, RationalList):
            new_list._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            new_list._add_to_internal(other)
        else:
            return NotImplemented
        return new_list

    #  +=
    def __iadd__(self, other):
        if isinstance(other, RationalList):
            self._data.extend(other._data)
        elif isinstance(other, (Rational, int)):
            self._add_to_internal(other)
        else:
            return NotImplemented
        return self

    def sum_all(self):
        res = Rational(0)
        for x in self._data:
            res = res + x
        return res


def len_and_sum(filenames):
    for filename in filenames:
        r_list = RationalList()
        try:
            with open(filename, 'r') as f:
                for line in f:
                    parts = line.split()
                    for part in parts:
                        if '/' in part:
                            n, d = map(int, part.split('/'))
                            r_list += Rational(n, d)
                        else:
                            r_list += int(part)

            total_sum = r_list.sum_all()
            print(f"Файл: {filename}")
            print(f"Кількість елементів: {len(r_list)}")
            print(f"Сума послідовності: {total_sum}\n")

        except FileNotFoundError:
            print(f"Файл {filename} не знайдено.")


files = ['input01.txt', 'input02.txt', 'input03.txt']
len_and_sum(files)