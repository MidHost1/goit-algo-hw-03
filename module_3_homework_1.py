'''
Завдання №1

Створіть функцію get_days_from_today(date), яка розраховує кількість днів між заданою датою і поточною датою.
'''
from datetime import datetime, timedelta, date 

def get_days_from_today(date):
    try:
            cur_date = datetime.today() # Зберігаємо в змінну нашу сьогоднішню дату ("07.02.2025")
            converted_date = datetime.strptime(date, "%Y-%m-%d").date() # Конвертуємо аргумент "date"('2020-10-09') в об'єкт "date"
            date_diff = converted_date - cur_date.date() # Формула для визначення кількості днів між заданою та поточною датами
            return date_diff.days
    except ValueError:
        print("Неправильний формат вхідних даних. Будь ласка, використовуйте формат 'РРРР-ММ-ДД' ")
        return None # Повертаємо None, якщо сталася помилка
# Перевірка
print(get_days_from_today('2020-10-09'))

