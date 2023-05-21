class Avto:
    def __init__(self, madel, rang, karobka, narh):
        self.model = madel
        self.rang = rang
        self.karobka = karobka
        self.narh = narh
        self.km = 0

    def get_info(self):
        return (f"Madel-{self.model}\n"
                f"Rangi-{self.rang}\n"
                f"Karobka-{self.karobka}\n"
                f"Narhi-{self.narh}$\n"
                f"Km-{self.km}")

    def set_km(self, km):
        self.km = km


car = Avto("cobalt", "qizil", "mehanika", 11000)
car.set_km(1000)
print(car.get_info())




