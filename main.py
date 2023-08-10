import random

class Fighter():
    def __init__(self, name='Bot'):
        self.name = name
        self.head = 'Head'
        self.body = 'Body'
        self.legs = 'Legs'
        self.health = random.randint(75, 150)
        self.damage = random.randint(10, 25)
 
    def __str__(self):
        return f'Боец: {self.name}, Здоровье: {self.health}, Урон: {self.damage}'
 
    def fight(self, p2):
        print(f'Здоровье бойца {self.name}: {self.health}')
        print(f'Здоровье бойца {p2.name}: {p2.health}')

        while p2.health > 0 and self.health > 0:  # Исправлено or на and
            bot_attack = random.choice((self.head, self.legs, self.body))
            bot_block = random.choice((self.head, self.legs, self.body))
            
            print(f'{self.name}, куда бьем? (Head/Legs/Body)')
            player_attack = input().strip().capitalize()  # Нормализация ввода
            print(f'{self.name}, на что ставим блок? (Head/Legs/Body)')
            player_block = input().strip().capitalize()   # Нормализация ввода
            
            print(f'Атакуем {player_attack}, блокируем {player_block}')
            
            PP = {
                'Head': self.damage * 3,
                'Body': self.damage * 2,
                'Legs': self.damage
            }
            
            if player_attack == bot_block:
                print(f'{self.name} наносит удар в {bot_block}, но {p2.name} блокирует удар!')
            if bot_attack == player_block:
                print(f'{p2.name} наносит удар в {player_block}, но {self.name} блокирует удар!')
            
            if player_attack != bot_block:
                p2.health -= PP.get(player_attack, 0)
                print(f'{self.name} попадает в {player_attack} и наносит {PP.get(player_attack, 0)} урона')
                print(f'Здоровье {p2.name} теперь {p2.health}')
            if bot_attack != player_block:
                self.health -= PP.get(bot_attack, 0)
                print(f'{p2.name} попадает в {bot_attack} и наносит {PP.get(bot_attack, 0)} урона')
                print(f'Здоровье {self.name} теперь {self.health}')
            
            if self.health <= 0:
                return 'Вы проиграли'
            if p2.health <= 0:
                return 'Вы победили'
# Пример реализации
player1 = Fighter('Player 1')
player2 = Fighter('Player 2')

print(player1)
print(player2)

result = player1.fight(player2)
print(result)
