from abc import ABC, abstractmethod

class change_money_mixin:
    def change_money(self, money):
        self.current_money = self.current_money + money


class StudentError(Exception):
    def __init__(self, message="Студент не зміг отримати диплом через нестачу балів, або в нього закінчились гроші"):
        self.message = message
        super().__init__(self.message)


class student(ABC, change_money_mixin):
    def __init__(self, credits_needed, current_money):
        self.credits_needed = credits_needed
        self.current_money = current_money
        self.current_credits = 0

    @abstractmethod
    def get_credits(self):
        pass

    def check_if_eligible_to_continue(self):
        if self.current_money < 0:
            raise StudentError("В студента закінчилися гроші")


class humanitarian(student):

    def get_credits(self, subject, credits):
        if subject == "humanitarian":
            self.current_credits += credits


class natural(student):

    def get_credits(self, subject, credits):
        if subject == "natural":
            self.current_credits += credits


class natural_humanitarian(student):

    def get_credits(self, subject, credits):
        if subject in ["natural", "humanitarian"]:
            self.current_credits += credits



def create_student(filename):
    with open(filename, "r") as file:

        speciality = file.readline().strip()
        credits_needed = int(file.readline())
        current_money = int(file.readline())

        if speciality == "humanitarian":
            current_student = humanitarian(credits_needed, current_money)
        elif speciality == "natural":
            current_student = natural(credits_needed, current_money)
        elif speciality == "natural-humanitarian":
            current_student = natural_humanitarian(credits_needed, current_money)

        try:
            for line in file:
                line = line.split()
                if "obtain" == line[0]:
                    current_student.change_money(int(line[-1]))
                elif "pay" == line[0]:
                    current_student.change_money(-int(line[-1]))
                elif "teach" == line[0]:
                    current_student.get_credits(line[1], int(line[-1]))

                current_student.check_if_eligible_to_continue()
            if current_student.current_credits < current_student.credits_needed:
                raise StudentError(f"У студента з файлу {filename} не вистачило кредитів на диплом після навчання")
            else:
                print(f"У студента з файлу {filename} вийшло набрати кредити на диплом")

        except StudentError as e:
            print(e)
            return None

for i in range(1,10):
    create_student(f"input0{i}.txt")

for i in range(10,15):
    create_student(f"input{i}.txt")




