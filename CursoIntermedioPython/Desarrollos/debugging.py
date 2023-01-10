def divisors(num):
    divisors = []
    try:
        if num < 0:
            raise ValueError("Debes ingresar un número positivo")
        for i in range(1, num + 1):
            if (num % i == 0):
                divisors.append(i)
    except ValueError as ve:
        return ve

    return divisors


def run():
    try:
        num = int(input("Ingresa un número: "))
        print(divisors(num))
        print("Terminó mi programa")
    except ValueError:
        print("Debes ingresar un número")


if __name__ == '__main__':
    run()
