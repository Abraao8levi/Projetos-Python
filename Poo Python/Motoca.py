class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def get_name(self):
        return self.name

    def get_age(self):
        return self.age

    def __str__(self):
        return f"{self.name}:{self.age}"


class Motorcycle:
    def __init__(self, power):
        self.power = power
        self.time = 0
        self.person = None

    def get_power(self):
        return self.power

    def get_time(self):
        return self.time

    def get_person(self):
        return self.person

    def enter(self, person):
        if self.person is None:
            self.person = person
            return True
        else:
            print("fail: busy motorcycle")
            return False

    def leave(self):
        if self.person is not None:
            person_leaving = self.person
            self.person = None
            return person_leaving
        else:
            print("fail: empty motorcycle")
            return None

    def honk(self):
        pot = 1
        while pot < self.power:
            pot += 1
        return "P" + "e" * pot + "m"

    def buy_time(self, time):
        self.time += time

    def drive(self, time):
        if self.time == 0:
            print("fail: buy time first")
            return
        if self.person is None:
            print("fail: empty motorcycle")
            return
        if self.person.get_age() > 10:
            print("fail: too old to drive")
            return
        if self.time >= time:
            self.time -= time
        else:
            print(f"fail: time finished after {self.time} minutes")
            self.time = 0

    def __str__(self):
        person_str = "empty" if self.person is None else str(self.person)
        return f"power:{self.power}, time:{self.time}, person:({person_str})"


motoca = Motorcycle(1)

while True:
    line = input()
    args = line.split(" ")

    if args[0] == "show":
        print(motoca)
    elif args[0] == "init":
        motoca = Motorcycle(int(args[1]))
    elif args[0] == "enter":
        motoca.enter(Person(args[1], int(args[2])))
    elif args[0] == "end":
        break
    elif args[0] == "leave":
        person = motoca.leave()
        if person is not None:
            print(person)
    elif args[0] == "honk":
        print(motoca.honk())
    elif args[0] == "buy":
        motoca.buy_time(int(args[1]))
    elif args[0] == "drive":
        motoca.drive(int(args[1]))
    else:
        print("fail: comando invalido")
