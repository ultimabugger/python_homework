def div(*args):
    try:
        arg_1 = float(input("Укажите число x: "))
        arg_2 = float(input("Укажите число y: "))
        res = arg_1 / arg_2
    except ValueError:
        return "Что-то пошло не так :) Попробуйте еще раз"
    except ZeroDivisionError:
        return "На ноль делить нельзя!"

    return res


print(f"Результат деления: {div()}")
