from abc import ABCMeta, abstractclassmethod
class Animal(metaclass=ABCMeta):
    @abstractclassmethod
    def __init__(self, kind, shape, character):
        #类型：eatmeat/eatgress
        self.kind = kind
        #体型：big/medinum/small
        self.shape = shape
        #性格：凶残ferocious
        self.character = character
        self.isferocious = 'None'

    def is_ferocious(self):
        if self.kind == 'eatmeat' \
        and (self.shape == 'medium' or self.shape == 'big') \
        and self.character =='ferocious':
            self.isferocious = True
        else:
            self.isferocious = False

class Cat(Animal):
    voice = 'miao'
    
    def __init__(self, kind, shape, character, name):
        self.name = name
        super().__init__(kind,shape,character)
        if super().is_ferocious:
            self.ispet = False
        else:
            self.ispet = True

class Zoo(object):
    def __init__(self, name):
        self.name = name
        self.isduplicate = {}

    def addAnimal(self,animal):
        animal_id = id(animal)
        if animal_id in list(self.isduplicate.keys()):
            raise Exception('animal is exists')
        self.isduplicate[animal_id] = animal

if __name__=='__main__':
    zoo = Zoo('first_zoo')
    cat1 = Cat('eatmeat', 'small', 'noferocious', 'blue_cat')
    cat2 = Cat('eatmeat', 'medium', 'noferocious', 'yellow_cat')
    print(cat1.isferocious)
    print(cat2.ispet)
    zoo.addAnimal(cat1)
    zoo.addAnimal(cat2)
    print(zoo.isduplicate)
    zoo.addAnimal(cat1)
    