class Pet:
    def __init__(self, energyMax, hungryMax, cleanMax):
        self.energyMax = energyMax
        self.hungryMax = hungryMax
        self.cleanMax = cleanMax
        self.energy = energyMax
        self.hungry = hungryMax
        self.clean = cleanMax
        self.diamonds = 0
        self.age = 0
        self.alive = True

    def setEnergy(self, value):
        if value <= 0:
            self.energy = 0
            print("fail: pet morreu de fraqueza")
            self.alive = False
            return
        if value > self.energyMax:
            self.energy = self.energyMax
            return
        self.energy = value

    def setHungry(self, value):
        if value <= 0:
            self.hungry = 0
            print("fail: pet morreu de fome")
            self.alive = False
            return
        if value > self.hungryMax:
            self.hungry = self.hungryMax
            return
        self.hungry = value

    def setClean(self, value):
        if value < 0:
            self.clean = 0
            print("fail: pet morreu de sujeira")
            self.alive = False
            return
        if value > self.cleanMax:
            self.clean = self.cleanMax
            return
        self.clean = value

    def testAlive(self):
        if not self.alive:
            print("fail: pet esta morto")
            return False
        return True

    def __str__(self):
        return f"E:{self.energy}/{self.energyMax}, S:{self.hungry}/{self.hungryMax}, L:{self.clean}/{self.cleanMax}, D:{self.diamonds}, I:{self.age}"

    def play(self):
        if not self.testAlive():
            return
        self.setEnergy(self.energy - 2)
        self.setHungry(self.hungry - 1)
        self.setClean(self.clean - 3)
        self.diamonds += 1
        self.age += 1

    def shower(self):
        if not self.testAlive():
            return
        self.setEnergy(self.energy - 3)
        self.setHungry(self.hungry - 1)
        self.setClean(self.cleanMax)
        self.age += 2

    def eat(self):
        if not self.testAlive():
            return
        self.setEnergy(self.energy - 1)
        self.setHungry(self.hungry + 4)
        self.setClean(self.clean - 2)
        self.age += 1

    def sleep(self):
        if not self.testAlive():
            return
        self.setEnergy(self.energyMax)
        self.setHungry(self.hungry - 1)
        self.age += 5

    def cleanPet(self):
        if not self.testAlive():
            return
        if self.clean <= 0:
            print("fail: pet morreu de sujeira")
            self.alive = False
            return
        self.setEnergy(self.energy - 1)
        self.setHungry(self.hungry - 1)
        self.setClean(self.cleanMax)
        self.age += 1
        class Solver:
    @staticmethod
    def main():
        pet = Pet(0, 0, 0)

        while True:
            line = input()
            print("$" + line)
            args = line.split()

            if args[0] == "end":
                break
            elif args[0] == "show":
                print(pet)
            elif args[0] == "init":
                pet = Pet(int(args[1]), int(args[2]), int(args[3]))
            elif args[0] == "play":
                pet.play()
            elif args[0] == "eat":
                pet.eat()
            elif args[0] == "sleep":
                if pet.energy >= pet.energyMax - 4:
                    print("fail: nao esta com sono")
                else:
                    pet.sleep()
            elif args[0] == "shower":
                pet.shower()
            elif args[0] == "clean":
                pet.cleanPet()
            else:
                print("fail: comando invalido")

if __name__ == "__main__":
    Tamagotchi.main()
