import math

class MathTaskError(Exception):
    pass


################################ TASK A ########################################
print('Task A Testing')


def task_a_gen_2(x):
    k = 1
    while True:
        yield (x ** k) / k
        k += 1


gen = task_a_gen_2(2)
for _ in range(5):
    print(f'xk = {next(gen)}')
print()

################################ TASK B ########################################
print('Task B Testing')


def calculate_product(n):
    if n < 1:
        return 0

    p = 1.0
    for i in range(1, n + 1):
        term = 1 / math.factorial(i+1)
        p *= term
    return p

try:
    n = int(input("Введіть значення n: "))
    result = calculate_product(n)
    print(f"Результат Pn = {result}")
except ValueError:
    print("Будь ласка, введіть ціле число.")
print()

################################ TASK C ########################################
print('Task C Testing')


def task_c_calc_determinant(n):
    if n < 1:
        raise MathTaskError

    if n == 1:
        return 2

    if n == 2:
        return 1

    return 2 * task_c_calc_determinant(n - 1) - 3 * task_c_calc_determinant(n - 2)

try:
    n = int(input("Введіть значення n: "))
    result = task_c_calc_determinant(n)
    print(f"Результат D(n) = {result}")
except ValueError:
    print("Будь ласка, введіть ціле число.")
print()

################################ TASK D ########################################
print('Task D Testing')


def task_d_gen(n):
    if n < 1:
        raise MathTaskError

    if n >= 1:
        yield 0

    if n >= 2:
        yield 1

    a_k_1 = 0
    a_k_2 = 1

    for k in range(3, n + 1):

        a_k = a_k_1 + k*a_k_2
        yield a_k

        a_k_2, a_k_1 = a_k_1, a_k


print(f'ak = {list(task_d_gen(5))}')


def task_d_sum_sn(n):
    total = 0

    for k, a_k in enumerate(task_d_gen(n), start=1):
        total += (2 ** k) * a_k

    return total


print(f'Sn(1) = {task_d_sum_sn(1)}')
print(f'Sn(2) = {task_d_sum_sn(2)}')
print(f'Sn(5) = {task_d_sum_sn(5)}')
print()


################################ TASK E ########################################
print('Task E Testing')

import math
class AccuracyError(MathTaskError):
    def __init__(self, eps):
        self.eps = eps
        super().__init__(f"Accuracy eps must be positive, got {eps}")

def task_e_sin_terms(x):
    term = x
    k = 1

    while True:
        yield term

        term *=  -x ** 2 / ((2 * k) * (2 * k + 1))
        k += 1

def task_e_sin_taylor(x, eps):
    if eps <= 0:
        raise AccuracyError(eps)

    total = 0

    for term in task_e_sin_terms(x):
        total += term

        if abs(term) < eps:
            break

    return total


x = 1.5
eps = 0.000001

approx = task_e_sin_taylor(x, eps)
real = math.sin(x)

print("Taylor:", approx)
print("math.cosh:", real)
print("Difference:", abs(approx - real))