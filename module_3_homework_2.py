'''
Завдання №2
Щоб виграти головний приз лотереї, необхідний збіг кількох номерів на лотерейному квитку з числами, 
що випали випадковим чином і в певному діапазоні під час чергового тиражу. 

Наприклад, необхідно вгадати шість чисел від 1 до 49 чи п'ять чисел від 1 до 36 тощо.

Вам необхідно написати функцію get_numbers_ticket(min, max, quantity), яка допоможе генерувати набір унікальних випадкових чисел для таких лотерей.

Вона буде повертати випадковий набір чисел у межах заданих параметрів, причому всі випадкові числа в наборі повинні бути унікальні.
'''
from random import randint
def get_numbers_ticket(min, max, quantity):
    if min > max or quantity > (max - min + 1) or quantity <= 0: # Додаємо перевірку вхідних значень
        return []
    elif min < 0:
        return []
    elif max > 1000:
        return []

    num_list = [] # Створюємо список, де будемо зберігати наші значення
    while len(num_list) < quantity:
        num = randint(min, max)

        if num not in num_list: # Перевірка на дублікат чисел у списку, щоб він приймав тільки унікальні значення
            num_list.append(num)

    return sorted(num_list)

# Перевіряємо функцію
print(get_numbers_ticket(1, 49, 6))
# Перевіряємо справність нашої перевірки вхідних значень
print(get_numbers_ticket(-10, 10, 5))
print(get_numbers_ticket(1000, 1200, 10))
print(get_numbers_ticket(10, 4, 5))
print(get_numbers_ticket(10, 14, 6))
'''
Потім прочитав і згадав, що також можна це було зробити за допомогою random.sample(range(min, max + 1), quantity). Це набагато практичніше
'''

