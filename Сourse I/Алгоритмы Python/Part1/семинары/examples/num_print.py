import sys

d = {
    "0": "000000000\n00     00\n00     00\n00     00\n00     00\n000000000\n",
    "1": "     111\n     111\n     111\n     111\n     111\n     111\n     111\n     111\n",
    "2": "2222222\n     22\n     22\n2222222\n22     \n22     \n2222222\n",
}


def main():
    try:
        input_n = sys.argv[1]
    except IndexError:
        print("Не введен аргумент в виде числа!")
        return

    for n in input_n:
        print(d[n])


if __name__ == "__main__":
    main()
