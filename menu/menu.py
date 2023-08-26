from menu.controllers import *


def start_menu():
    create_table_for_start()
    while True:
        print(
            "\nВведите команду:\n"
            "    Создать пользователя: 1\n"
            "    Проверить пользователя: 2\n"
            "    Удалить пользователя: 3\n"
            "    Покинуть программу: 0\n"
        )

        inp = int(input())

        if inp == 1:
            print(
                "Хотите создать фейкового пользователя или настоящего?\n"
                "Фейк: 1\n"
                "Настоящий: 2\n"
            )

            inp2 = int(input())

            if inp2 == 1:
                create_user(fake=True)
                print("Пользователь создан\n")

            else:
                create_user(
                    username=input("Введите имя пользователя\n"),
                    hashedpassword=input("Введите пароль\n"),
                    email=input("Введите адрес почты\n"),
                )
                print("Пользователь создан\n")

        elif inp == 2:
            print(
                check_user(
                    username=input("Введите имя пользователя\n"),
                    password=input("Введите пароль\n"),
                )
            )

        elif inp == 3:
            print(
                delete_user(
                    username=input("Введите имя пользователя\n"),
                    password=input("Введите пароль\n"),
                )
            )

        elif inp == 0:
            print("Хорошего дня!\n")
            break

        else:
            print("Введите корректное значение!\n")
