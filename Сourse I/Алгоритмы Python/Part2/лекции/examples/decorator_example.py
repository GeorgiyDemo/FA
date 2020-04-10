def positive_result(function):  # декоратор
    def wrapper(*args, **kwargs):  # обертка
        result = function(*args, **kwargs)  #
        assert result >= 0, function.__name__ + "() result isn't >= 0"
        return result

    wrapper.__name__ = function.__name__
    wrapper.__doc__ = function.__doc__
    return wrapper


@positive_result
def discriminant(a, b, c):
    return (b ** 2) - (4 * a * c)


def bounded(minimum, maximum):  # внешний генератор декоратора
    def decorator(function):  # вунтренний генератор декоратора
        @functools.wraps(function)
        def wrapper(*args, **kwargs):  # декоратор
            result = function(*args, **kwargs)  # вызов декарируемой функции
            if result < minimum:
                return minimum
            elif result > maximum:
                return maximum
            return result

        return wrapper

    return decorator


@bounded(0, 100)  # обрезает возвращения по нижней и верхней границе
def percent(amount, total):
    return (amount / total) * 100


if __name__ == "__main__":
    r1 = discriminant(1, 1, -1)
    r2 = discriminant(1, 1, 1)
    print(r1, r2)

    percent(180, 100)
    percent(15, 100)
