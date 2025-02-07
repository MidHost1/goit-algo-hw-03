'''
Завдання №3
У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. 
Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах. 
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку.
'''
import re
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

def normalize_phone(phone_number):
    cleared_numbers = []
    for phone in phone_number:
        updated_number = re.sub(r"[^0-9]", "", phone)# Видаляємо все, крім цифр
        
        #Тут ми додаємо код країни, якщо його немає, за допомогою умовного оператора "if"
        if updated_number.startswith('380'):
            updated_number = '+' + updated_number # Тут - додали "+"
            
        else:
            updated_number = '+38' + updated_number # Тут перевіряється випадок, коли номер не починається з "380", а з "0", як деякі номери зі списку
        
        cleared_numbers.append(updated_number)



    return cleared_numbers
    
sanitized_numbers = normalize_phone(raw_numbers)
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)

