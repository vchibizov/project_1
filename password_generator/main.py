import random
import string


def generate_password(length=12):
    if length < 6:
        raise ValueError("Длина пароля должна быть не менее 6 символов.")

    # Определяем набор символов для пароля
    lowercase = string.ascii_lowercase
    uppercase = string.ascii_uppercase
    digits = string.digits
    punctuation = string.punctuation

    # Объединяем все символы
    all_characters = lowercase + uppercase + digits + punctuation

    # Генерируем пароль
    password = [
        random.choice(lowercase),
        random.choice(uppercase),
        random.choice(digits),
        random.choice(punctuation)
    ]

    # Заполняем оставшуюся длину пароля случайными символами
    password += random.choices(all_characters, k=length - 4)

    # Перемешиваем пароль для обеспечения "рандомности"
    random.shuffle(password)

    return ''.join(password)


if __name__ == "__main__":
    password_length = int(input("Введите желаемую длину пароля (не менее 6): "))
    try:
        password = generate_password(password_length)
        print(f"Сгенерированный пароль: {password}")
    except ValueError as e:
        print(e)
