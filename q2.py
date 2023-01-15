import random
i = 0
peoples = []
orcs = []

class NPC:                                              ## узагальнюючий клас NPC
    def __init__(self, numb, command, name):
        self.numb = numb
        self.command = command
        self.name = name

class Soldait(NPC):                                     ## клас "воїни", який наслідує параметри із батьківського класу
    def __init__(self, numb, command, name, hero):
        super().__init__(numb, command, name)
        self.hero = hero
    def follow_the_people(self):                        ## метод "слідую за героєм людей"
        self.hero = King_of_peoples
    def follow_the_orcs(self):                          ## метод "слідую за героєм орків"
        self.hero = King_of_orcs

class Hero(NPC):                                        ## клас "герої", який наслідує параметри із батьківського класу
    def __init__(self, numb, command, name, lvl):
        super().__init__(numb, command, name)
        self.lvl = lvl
    def level_up (self):                                ## метод підвищення рівня героя
        self.lvl = self.lvl + 1
    def print_info(self):                               ## метод "вивід рівня героя в консоль"
        print(f'Рівень героя {self.name} тепер {self.lvl}')
    def print_numb(self):                               ## метод "вивід номера героя у консоль"
        print(f'Номер героя: {self.numb}')

King_of_peoples = Hero('432', 'peoples', 'Король Робар ІІ', 1)          ## об'єкти класу "Герої"
King_of_orcs = Hero('543', 'orcs', 'Кан Завойовник', 1)

while i < 5:                                                            ## цикл, який генерує 5 воїнів
    s = random.choice(['люди', 'орки'])
    i = i + 1
    if s == 'люди':
        soldait = Soldait(int(i), str(s), f'Найомник {i}', King_of_peoples)
        peoples.append(soldait)
    else:
        soldait = Soldait(int(i), str(s), f'Найомник {i}', King_of_orcs)
        orcs.append(soldait)

print(f'Кількість солдатів в команді Люди:  {len(peoples)}')
print(f'Кількість солдатів в команді Орки:  {len(orcs)}')

if len(peoples) > len(orcs):                        ## якщо до людей примкнуло більше воїнів ніж до орків, то:
    King_of_peoples.level_up()                      ## підняти рівень героя класу "люди"
    King_of_peoples.print_info()                    ## вивести ріень героя в консоль
    orcs[0].follow_the_people()                     ## перекинути одного із солдатів класу "орки" до класу "люди"
    print(f'Солдат під номером {orcs[0].numb} перейшов до Короля Робара ІІ')
    King_of_peoples.print_numb()                    ## вивести в конмоль номер героя, який преміг
else:
    King_of_orcs.level_up()                         ## в протилежному випадку все те ж саме, тільки навпаки
    King_of_orcs.print_info()
    peoples[0].follow_the_orcs()
    print(f'Солдат під номером {peoples[0].numb} перейшов до Кана Завойовника')
    King_of_orcs.print_numb()



