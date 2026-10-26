class Hero:
    def __init__(self, name, hp, attack):
        self.name = name
        self.hp = hp
        self.attack = attack  # Виправили помилку (тут не вистачало = attack)

    def say_hello(self):
        print(f"Привіт! Я {self.name}")

    def info(self):  # Нова проста функція — показати старти героя
        print(f"Герой: {self.name} | Здоров'я: {self.hp} | Атака: {self.attack}")


# Створюємо героїв
hulk = Hero("Галк", 400, 350)
spider_man = Hero("Людина-Павук", 250, 200)
batman = Hero("Бетмен", 200, 180)
black_widow = Hero("Чорна Вдова", 220, 230)

# Викликаємо функції
hulk.say_hello()
hulk.info()

print()

spider_man.say_hello()
spider_man.info()

print()

batman.say_hello()
batman.info()

print()

black_widow.say_hello()
black_widow.info()