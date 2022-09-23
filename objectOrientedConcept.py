import time


class Rectangle:
    width = 0
    height = 0

    def __init__(self, width, length):
        self.width = width
        self.length = length

    def __perimeter(self):
        w = self.width
        l = self.length
        return (w + l) * 2

    def __area(self):
        return self.width * self.length

    def display(self):
        print("Width of the rectangle is: ", self.width)
        print("Height of the rectangle is: ", self.length)
        print("Perimeter of the rectangle is: ", self.__perimeter())
        print("Area of the rectangle is: ", self.__area())


square = Rectangle(5, 7)
square.display()


class Parallelepipede(Rectangle):
    def __init__(self, width, length, height):
        Rectangle.__init__(self, width, length)
        self.height = height

    # define Volume method
    def __volume(self):
        return self.length * self.width * self.height

    def display_volume(self):
        print("Width of the Parallelepipede is: ", self.width)
        print("Length of the Parallelepipede is: ", self.length)
        print("Height of the Parallelepipede is: ", self.height)
        print("Volume of the Parallelepipede is: ", self.__volume())


print("------------------------------------------------------------------------\n")
parallel = Parallelepipede(5, 7, 10)
parallel.display_volume()

print("------------------------------------------------------------------------\n")
print("Outputting Person class: ")
time.sleep(3)


class Person:
    name = ""
    age = 0

    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        print("The Person you created is named: ", self.name, "and", self.age, "years old")


p1 = Person("Judy", 28)
p1.display()


class Student(Person):

    def __init__(self, name, age, section):
        Person.__init__(self, name, age)
        self.section = section

    def display_student(self):
        print("The Student you created is named: ", self.name, ",", self.age, "years old and is in section:",
              self.section)


s1 = Student("Peter", 22, "3-B")
s1.display_student()

print("------------------------------------------------------------------------\n")
print("Outputting Bank Account class: ")
time.sleep(3)


class BankAccount:

    def __init__(self, account_number, person_name, balance):
        self.account_number = account_number
        self.person_name = person_name
        self.balance = balance

    def deposit(self, deposit_amount):
        self.balance = self.balance + deposit_amount
        print("Deposited:$", deposit_amount, "current balance is now: $", self.balance)

    def withdraw(self, withdraw_amount):
        if self.balance > withdraw_amount:
            self.balance -= withdraw_amount
            print("Withdraw:$", withdraw_amount, "current balance is now: $", self.balance)
        else:
            print("We cannot allow you to withdraw more than your current balance")

    def bank_fees(self):
        fees = self.balance * .05
        print("Bank charges you: $", fees, "fees")

    def display(self):
        print("Member: ", self.person_name, "\nAccount Number:", self.account_number, "\nBalance: $", self.balance)


bank_owner = BankAccount("38520000023237", "Justin", 3000)
bank_owner.display()
bank_owner.deposit(300)
bank_owner.withdraw(700)
bank_owner.withdraw(7000)
bank_owner.bank_fees()


