import random


class Wishes:
    def __init__(self):
        self.otcricheno_do_legi = 0
        self.otcricheno_do_chetvirki = 0


class Crutki(Wishes):
    def __init__(self):
        super().__init__()
        self.shans = 0

    def do_it_1(self):
        self.otcricheno_do_legi += 1
        self.otcricheno_do_chetvirki += 1
        Fiolka = False
        udacha = random.randint(1, 100)

        # рассматриваем для 4*
        if self.otcricheno_do_legi < 50:
            if self.otcricheno_do_chetvirki < 7:
                if udacha % 30 == 0:
                    print("У вас фиолетка")
                    self.otcricheno_do_chetvirki = 0
                    Fiolka = True
                else:
                    print("Нечего")
            elif self.otcricheno_do_chetvirki < 10:
                if udacha % 5 == 0:
                    print("у вас фиолка почти до гаранта")
                    self.otcricheno_do_chetvirki = 0
                    Fiolka = True
                else:
                    print("нечего")
            else:
                print("Четверка по гаранту")
                Fiolka = True
                self.otcricheno_do_chetvirki = 0

        # рассматриваем для 5*
        if not Fiolka:
            if self.otcricheno_do_legi < 35:
                if udacha % 33 == 0:
                    print("ЛЕГААААА БЕЗ ГАРАНТАА")
                    self.otcricheno_do_legi = 0
                else:
                    print("Нечего")
            elif self.otcricheno_do_legi < 45:
                if udacha % 20:
                    print("лега почти по гаранту")
                    self.otcricheno_do_legi = 0
                else:
                    print("Нечего")
            elif self.otcricheno_do_legi < 50:
                if udacha % 3:
                    print("Лега до гаранта")
                    self.otcricheno_do_legi = 0
                else:
                    print("Нечего")
            else:
                print("На 50ой крутке")
                self.otcricheno_do_legi = 0
            print(self.otcricheno_do_chetvirki)
            print(self.otcricheno_do_legi)
    def do_it_10(self):
        for i in range(10):
            self.do_it_1()



