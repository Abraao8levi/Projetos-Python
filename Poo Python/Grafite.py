class Lead:
    def __init__(self, thickness, hardness, size):
        self.thickness = thickness
        self.hardness = hardness
        self.size = size

    def get_thickness(self):
        return self.thickness

    def get_hardness(self):
        return self.hardness

    def get_size(self):
        return self.size

    def set_size(self, size):
        self.size = size

    def usage_per_sheet(self):
        if self.hardness == "HB":
            return 1
        elif self.hardness == "2B":
            return 2
        elif self.hardness == "4B":
            return 4
        else:
            return 6

    def __str__(self):
        return f"{self.thickness:.1f}:{self.hardness}:{self.size}"


class Pencil:
    def __init__(self, thickness):
        self.thickness = thickness
        self.tip = None

    def get_thickness(self):
        return self.thickness

    def set_thickness(self, value):
        self.thickness = value

    def has_grafite(self):
        return self.tip is not None

    def insert(self, grafite):
        if self.thickness != grafite.get_thickness():
            print("fail: calibre incompativel")
            return False
        if self.has_grafite():
            print("fail: ja existe grafite")
            return False
        self.tip = grafite
        return True

    def remove(self):
        removed_tip = self.tip
        self.tip = None
        return removed_tip

    def write_page(self):
        if self.tip is None:
            print("fail: nao existe grafite")
            return
        if self.tip.get_size() == 10:
            print("fail: tamanho insuficiente")
            return
        final_size = self.tip.get_size() - self.tip.usage_per_sheet()
        if final_size >= 10:
            self.tip.set_size(final_size)
        else:
            self.tip.set_size(10)
            print("fail: folha incompleta")

    def __str__(self):
        return f"calibre: {self.thickness}, grafite: [{'None' if self.tip is None else str(self.tip)}]"


def main():
    lap = Pencil(0.5)

    while True:
        line = input()
        argsL = line.split(" ")

        if argsL[0] == "end":
            break
        elif argsL[0] == "init":
            lap = Pencil(float(argsL[1]))
        elif argsL[0] == "insert":
            lap.insert(Lead(float(argsL[1]), argsL[2], int(argsL[3])))
        elif argsL[0] == "remove":
            lap.remove()
        elif argsL[0] == "write":
            lap.write_page()
        elif argsL[0] == "show":
            print(lap)


if __name__ == "__main__":
    main()
