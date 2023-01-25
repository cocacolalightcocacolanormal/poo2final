import random


def lancer_de():
    throw1 = random.randit(1, 6)
    throw2 = random.randit(1, 6)
    throw3 = random.randit(1, 6)
    throw4 = random.randit(1, 6)

    if throw1 < throw2 and throw1 < throw3 and throw1 < throw4:
        return (throw2 + throw3 + throw4)

    elif throw2 < throw1 and throw2 < throw3 and throw2 < throw4:
        return (throw1 + throw3 + throw4)

    elif throw3 < throw2 and throw1 < throw3 and throw1 < throw4:
        return (throw2 + throw3 + throw4)

    elif throw4 < throw2 and throw4 < throw3 and throw4 < throw1:
        return (throw2 + throw3 + throw1)


class NPC:
    def __init__(self):
        self.force = lancer_de()
        self.agilite = lancer_de()
        self.constitution = lancer_de()
        self.intelligence = lancer_de()
        self.sagesse = lancer_de()
        self.charisme = lancer_de()


    def attributs(self/):
        print('force:', self.force, "agilité:", self.agilite, "constitution:", self.constitution, "intelligence:", self.intelligence, "sagesse:", self.sagesse, "charisme:", self.charisme)