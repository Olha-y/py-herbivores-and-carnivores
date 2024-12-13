class Animal:
    alive = []

    def __init__(self, name: str, health: int = 100) -> None:
        self.name = name
        self.health = health
        self.hidden = False
        # add animal to the alive list when it's created

        Animal.alive.append(self)

    def die(self):
        if self.health <= 0:
            Animal.alive.remove(self)

    def __repr__(self):
        return (f""
                f"{{Name: {self.name}, "
                f"Health: {self.health}, "
                f"Hidden: {self.hidden}}}"
                )


class Herbivore(Animal):
    def hide(self):
        self.hidden = not self.hidden


class Carnivore(Animal):
    @staticmethod
    def bite(herbivore):
        if isinstance(herbivore, Herbivore) and not herbivore.hidden:
            herbivore.health -= 50
            if herbivore.health <= 0:
                herbivore.die()

    @staticmethod
    def remove_dead_animal():
        Animal.alive = [animal for animal in Animal.alive if animal.health > 0]
