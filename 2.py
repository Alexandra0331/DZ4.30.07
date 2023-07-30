# 2. Напишите функцию, принимающую на вход только ключевые параметры и возвращающую словарь,
# где ключ — значение переданного аргумента, а значение — имя аргумента. Если ключ не хешируем,
# используйте его строковое представление.
# Пример: rev_kwargs(res=1, reverse=[1, 2, 3]) -> {1: 'res', '[1, 2, 3]': 'reverse'}

GLOBAL_VALUE = 23


def my_func(**kwargs) -> dict:
    result = dict()
    for k, v in kwargs.items():
        try:
            _ = hash(v)
            result[v] = k
        except TypeError:
            result[str(v)] = k

    return result


def main():
    print("Исх. параметры: res=1, revers=[1,2,3]")
    print(my_func(res=1, revers=[1, 2, 3]))


if __name__ == "__main__":
    main()