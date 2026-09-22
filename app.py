def calculate_discount(price: float, discount: float) -> float:
    """
    Вычисляет итоговую цену со скидкой.
    :param price: Исходная цена товара (должна быть > 0)
    :param discount: Размер скидки в процентах (0 до 100)
    :return: Итоговая стоимость
    """
    if price <= 0:
        raise ValueError("Цена должна быть положительной")
    if not (0 <= discount <= 100):
        raise ValueError("Скидка должна быть в диапазоне от 0 до 100")
    
    return price * (1 - discount / 100)


def calculate_tax(income, tax_rate):
    return income * tax_rate / 100  # Ошибка PEP8: нет пробелов вокруг операторов


if __name__ == "__main__":
    print("Цена 1000 руб со скидкой 20%:", calculate_discount(1000, 20))
