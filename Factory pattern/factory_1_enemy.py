from abc import ABC, abstractmethod

class Enemy(ABC):

    @abstractmethod
    def attack(self):
        pass

class Zombie(Enemy):
    def attack(self):
        print("Зомби медленно бредет и кусает... 'Грррр'")
    
class Skeleton(Enemy):
    def attack(self):
        print("Скелет стреляет из лука! *Щелк*")

class Dragon(Enemy):
    def attack(self):
        print("Скелет стреляет из лука! *Щелк*")

class EnemyFactory:

    def create_enemy(self, enemy_type):
        mapping = {
            'zombie': Zombie(),
            'skeleton': Skeleton(),
            'dragon': Dragon()
        }

        if enemy_type not in mapping:
            raise ValueError("Undefined type of enemy: ", enemy_type)

        return mapping[enemy_type]
    
efactory = EnemyFactory()
enemy_list = ['zombie', 'dragon', 'skeleton', 'zombie']
enemies = []

for enemy_type in enemy_list:
    enemy = efactory.create_enemy(enemy_type)
    enemies.append(enemy)
for enemy in enemies:
    enemy.attack()