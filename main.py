class Student:
    def __init__(self, name, age, money=0):
        self.name = name
        self.age = age
        self.money = money
        self.knowledge = 0  # рівень знань
        self.energy = 100  # рівень енергії

    def greeting(self):
        print(f"Hello, I am {self.name}!")

    def grow_up(self):
        self.age += 1

    def print_age(self):
        print(f"Age: {self.age}")

    def work(self):
        if self.energy >= 20:
            print(f"{self.name} is working...")
            self.money += 50
            self.energy -= 20
        else:
            print(f"{self.name} is too tired to work. Needs rest.")

    def rest(self):
        print(f"{self.name} is resting...")
        self.energy += 30
        if self.energy > 100:
            self.energy = 100

    def study(self):
        if self.energy >= 15:
            print(f"{self.name} is studying...")
            self.knowledge += 10
            self.energy -= 15
        else:
            print(f"{self.name} is too tired to study. Needs rest.")

    def spend_money(self, amount):
        if self.money >= amount:
            print(f"{self.name} spent {amount} money.")
            self.money -= amount
        else:
            print(f"{self.name} doesn't have enough money. Needs to work.")

    def live_a_year(self):
        print(f"{self.name} is living a year...")
        for month in range(1, 13):
            print(f"\nMonth {month}:")
            # Витрати кожного місяця
            self.spend_money(20)

            # Поведінка залежить від стану студента
            if self.money < 20:
                print(f"{self.name} needs to work to cover expenses.")
                self.work()
            elif self.knowledge < 50:
                print(f"{self.name} needs to study more.")
                self.study()
            elif self.energy < 50:
                print(f"{self.name} is feeling exhausted.")
                self.rest()
            else:
                print(f"{self.name} is maintaining a balanced routine.")

        # Після року студент дорослішає
        self.grow_up()
        print(f"\nEnd of the year: {self.name}'s age is now {self.age}.")
        print(f"Final status: Money: {self.money}, Knowledge: {self.knowledge}, Energy: {self.energy}")

# Приклад використання
maxym_student = Student(name="Maxym", age=12, money=100)
maxym_student.greeting()
maxym_student.live_a_year()
