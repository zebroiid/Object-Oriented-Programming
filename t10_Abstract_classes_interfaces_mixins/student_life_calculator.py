from abc import ABC, abstractmethod

class StudentError(Exception):
    def __init__(self, message="Студент не зміг отримати диплом"):
        self.message = message
        super().__init__(self.message)


class Visitor(ABC):
    @abstractmethod
    def visit_humanitarian(self, student): pass

    @abstractmethod
    def visit_natural(self, student): pass

    @abstractmethod
    def visit_natural_humanitarian(self, student): pass


class Teacher(Visitor):
    def __init__(self, profile, credits):
        self.profile = profile
        self.credits = credits

    def visit_humanitarian(self, student):
        if self.profile == "humanitarian":
            student.current_credits += self.credits

    def visit_natural(self, student):
        if self.profile == "natural":
            student.current_credits += self.credits

    def visit_natural_humanitarian(self, student):
        student.current_credits += self.credits


class Accounting(Visitor):
    def __init__(self, amount):
        self.amount = amount

    def visit_humanitarian(self, student): student.current_money += self.amount

    def visit_natural(self, student): student.current_money += self.amount

    def visit_natural_humanitarian(self, student): student.current_money += self.amount


class CampusDirection(Visitor):
    def __init__(self, cost):
        self.cost = cost

    def visit_humanitarian(self, student): student.current_money -= self.cost

    def visit_natural(self, student): student.current_money -= self.cost

    def visit_natural_humanitarian(self, student): student.current_money -= self.cost


class Canteen(Visitor):
    def __init__(self, cost):
        self.cost = cost

    def visit_humanitarian(self, student): student.current_money -= self.cost

    def visit_natural(self, student): student.current_money -= self.cost

    def visit_natural_humanitarian(self, student): student.current_money -= self.cost



class Student(ABC):
    def __init__(self, credits_needed, current_money):
        self.credits_needed = credits_needed
        self.current_money = current_money
        self.current_credits = 0

    @abstractmethod
    def accept(self, visitor: Visitor):
        pass

    def check_if_eligible_to_continue(self):
        if self.current_money < 0:
            raise StudentError("Студент відрахований: закінчилися гроші для існування.")


class Humanitarian(Student):
    def accept(self, visitor: Visitor):
        visitor.visit_humanitarian(self)


class Natural(Student):
    def accept(self, visitor: Visitor):
        visitor.visit_natural(self)


class NaturalHumanitarian(Student):
    def accept(self, visitor: Visitor):
        visitor.visit_natural_humanitarian(self)


def create_student(filename):
    with open(filename, "r") as file:


        speciality = file.readline().strip()
        credits_needed = int(file.readline())
        current_money = int(file.readline())

        if speciality == "humanitarian":
            current_student = Humanitarian(credits_needed, current_money)
        elif speciality == "natural":
            current_student = Natural(credits_needed, current_money)
        elif speciality == "natural-humanitarian":
            current_student = NaturalHumanitarian(credits_needed, current_money)
        else:
            print(f"Невідомий тип спеціальності: {speciality}")
            return None

        try:
            for line in file:
                line = line.split()
                if not line:
                    continue

                visitor = None

                if "teach" == line[0]:
                    profile = line[1]
                    credits_val = int(line[-1])
                    visitor = Teacher(profile, credits_val)

                elif "obtain" == line[0]:
                    amount = int(line[-1])
                    visitor = Accounting(amount)

                elif "pay" == line[0]:
                    service = line[1]
                    cost = int(line[-1])
                    if service == "hostel":
                        visitor = CampusDirection(cost)
                    elif service == "canteen":
                        visitor = Canteen(cost)

                if visitor is not None:
                    current_student.accept(visitor)

                current_student.check_if_eligible_to_continue()

            if current_student.current_credits < current_student.credits_needed:
                raise StudentError(
                    f"У студента з файлу {filename} не вистачило кредитів на диплом після навчання (Має {current_student.current_credits} з {current_student.credits_needed})")
            else:
                print(
                    f"Студент з файлу {filename} отримав диплом. Залишок грошей: {current_student.current_money}, Кредити: {current_student.current_credits}")
                return current_student

        except StudentError as e:
            print(f"Помилка для {filename}: {e}")
            return None


if __name__ == "__main__":
    for i in range(1, 15):
        filename = f"input{i:02d}.txt"
        try:
            create_student(filename)
        except FileNotFoundError:
            continue