'''
Завдання №3
У вашій компанії ведеться активна маркетингова кампанія за допомогою SMS-розсилок. 
Для цього ви збираєте телефонні номери клієнтів із бази даних, але часто стикаєтеся з тим, що номери записані у різних форматах. 
Розробіть функцію normalize_phone(phone_number), що нормалізує телефонні номери до стандартного формату, залишаючи тільки цифри та символ '+' на початку.
'''
import re

def normalize_phone(phone_number):
    
    
    updated_number = re.sub(r"[^0-9]", "", phone_number)# Видаляємо все, крім цифр
        
    #Тут ми додаємо код країни, якщо його немає, за допомогою умовного оператора "if"
    if updated_number.startswith("380"):
        updated_number = '+' + updated_number # Тут - додали "+"
            
    elif updated_number.startswith("0"):
        updated_number = '+38' + updated_number # Тут перевіряється випадок, коли номер не починається з "380", а з "0", як деякі номери зі списку

    else:
        return "Номер не відповідає укр. формату" # Якщо номер не відповідає українському формату, виводимо ось таке повідомлення
    



    return updated_number
# Перевіряємо перевірку, чи вказаний номер відповідає українському формату:
print(normalize_phone("+49 161 71777965")) # Виводить - "Номер не відповідає укр. формату."
# Перевіряємо функцію
print(normalize_phone("067\\t123 4567"))
print(normalize_phone("(095) 234-5678\\n"))
print(normalize_phone("+380 44 123 4567"))
print(normalize_phone("380501234567"))
print(normalize_phone("    +38(050)123-32-34"))
print(normalize_phone("     0503451234"))
print(normalize_phone("(050)8889900"))
print(normalize_phone("38050-111-22-22"))
print(normalize_phone("38050 111 22 11   "))