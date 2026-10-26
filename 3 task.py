try:
    age = int(input("Введите ваш возраст: "))
    days = age * 365

    print(f"Ваш возраст {age}, это {days} дней.")

except ValueError:
    print("Ошибка, введите целое число (цифрами), а не текст")