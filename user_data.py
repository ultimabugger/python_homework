user_name = input("Укажите имя: ")
user_surname = input("Укажите фамилию: ")
user_city = input("Укажите город, в котором вы проживаете: ")
user_email: str = input("Укажите ваш email: ")
user_num_phone = int(input("Укажите номер вашего телефона: "))
user_date_birth = input("Укажите дату вашего рождения: ")


def user_data(**kwargs):
    user_email = "@mail"
    if user_email == "@mail":
        suffix = "@"
        print(user_email.endswith(suffix))
    else:
        print("Некорректно введен адрес электронной почты")
    return kwargs


print(user_data(user_name=user_name, user_surname=user_surname,
                user_city=user_city, user_email=user_email,
                user_num_phone=user_num_phone, user_date_birth=user_date_birth))
