"""
Выполнить собственную программную реализацию MD5.
Референс: https://ru.wikipedia.org/wiki/MD5
"""

import struct
from enum import Enum
from math import floor, sin
from bitarray import bitarray


class MD5Buffer(Enum):
    """
    Буфер начальных значений MD5, используется на 3 шаге

    Для вычислений инициализируются 4 переменных размером по 32 бита
    задаются начальные значения шестнадцатеричными числами
    (порядок байтов little-endian, сначала младший байт):
    """
    A = 0x67452301
    B = 0xEFCDAB89
    C = 0x98BADCFE
    D = 0x10325476


class MD5:
    """Класс MD5"""

    string = None
    buffers = {
        MD5Buffer.A: None,
        MD5Buffer.B: None,
        MD5Buffer.C: None,
        MD5Buffer.D: None,
    }

    @classmethod
    def hash(cls, string):
        """
        Основной метод для вызова и получения данных
        """
        cls.string = string

        preprocessed_bit_array = cls.step_2(cls.step_1())
        cls.step_3()
        cls.step_4(preprocessed_bit_array)
        return cls.step_5()

    @classmethod
    def step_1(cls):
        """
        Шаг 1. Выравнивание потока
        (конвертация строки в bit array)
        """
        bit_array = bitarray(endian="big")
        bit_array.frombytes(cls.string.encode("utf-8"))

        # Сначала к концу потока дописывают единичный бит.
        bit_array.append(1)

        # Затем добавляют некоторое число нулевых бит такое, чтобы новая длина потока стала сравнима с 448 по модулю 512
        while bit_array.length() % 512 != 448:
            bit_array.append(0)

        return bitarray(bit_array, endian="little")

    @classmethod
    def step_2(cls, step_1_result):
        """
        Шаг 2. Добавление длины сообщения
        """

        # В конец сообщения дописывают 64-битное представление длины данных (количество бит в сообщении) до выравнивания
        length = (len(cls.string) * 8) % pow(2, 64)
        length_bit_array = bitarray(endian="little")
        length_bit_array.frombytes(struct.pack("<Q", length))

        result = step_1_result.copy()
        result.extend(length_bit_array)
        return result

    @classmethod
    def step_3(cls):
        """
        Шаг 3. Инициализация буфера
        (буферы со значениями по-умолчанию)
        """
        for buffer_type in cls.buffers.keys():
            cls.buffers[buffer_type] = buffer_type.value

    @classmethod
    def step_4(cls, step_2_result):
        """
        Шаг 4. Вычисление в цикле
        """

        # 1-й раунд
        def F(x, y, z): return (x & y) | (~x & z)
        # 2-й раунд
        def G(x, y, z): return (x & z) | (y & ~z)
        # 3-й раунд
        def H(x, y, z): return x ^ y ^ z
        # 4-й раунд
        def I(x, y, z): return y ^ (x | ~z)

        def rotate_left(x, n): return (x << n) | (x >> (32 - n))
        def modular_add(a, b): return (a + b) % pow(2, 32)

        # Определение таблицы констант T
        T = [floor(pow(2, 32) * abs(sin(i + 1))) for i in range(64)]

        N = len(step_2_result) // 32

        for chunk_index in range(N // 16):

            start = chunk_index * 512
            # Каждый 512-битный блок проходит 4 этапа вычислений по 16 раундов. Для этого блок представляется в виде массива X из 16 слов по 32 бита.
            X = [step_2_result[start + (x * 32): start + (x * 32) + 32]
                 for x in range(16)]
            # Переводим все в int из байтов
            X = [int.from_bytes(word.tobytes(), byteorder="little")
                 for word in X]

            # Получаем значение из буферов
            A = cls.buffers[MD5Buffer.A]
            B = cls.buffers[MD5Buffer.B]
            C = cls.buffers[MD5Buffer.C]
            D = cls.buffers[MD5Buffer.D]

            for i in range(4 * 16):

                # 1-й раунд
                if 0 <= i <= 15:
                    k = i
                    s = [7, 12, 17, 22]
                    buff = F(B, C, D)

                 # 2-й раунд
                elif 16 <= i <= 31:
                    k = ((5 * i) + 1) % 16
                    s = [5, 9, 14, 20]
                    buff = G(B, C, D)

                # 3-й раунд
                elif 32 <= i <= 47:
                    k = ((3 * i) + 5) % 16
                    s = [4, 11, 16, 23]
                    buff = H(B, C, D)

                # 4-й раунд
                elif 48 <= i <= 63:
                    k = (7 * i) % 16
                    s = [6, 10, 15, 21]
                    buff = I(B, C, D)

                # Тут происходит добавление модульного значения
                buff = modular_add(buff, X[k])
                buff = modular_add(buff, T[i])
                buff = modular_add(buff, A)
                buff = rotate_left(buff, s[i % 4])
                buff = modular_add(buff, B)

                # Замена регистров
                A = D
                D = C
                C = B
                B = buff

            # Обновление буферов
            cls.buffers[MD5Buffer.A] = modular_add(cls.buffers[MD5Buffer.A], A)
            cls.buffers[MD5Buffer.B] = modular_add(cls.buffers[MD5Buffer.B], B)
            cls.buffers[MD5Buffer.C] = modular_add(cls.buffers[MD5Buffer.C], C)
            cls.buffers[MD5Buffer.D] = modular_add(cls.buffers[MD5Buffer.D], D)

    @classmethod
    def step_5(cls):
        """
        Шаг 5. Результат вычислений
        Результат вычислений находится в буфере ABCD, это и есть хеш.
        Если выводить побайтово, начиная с младшего байта A и закончив старшим байтом D, то мы получим MD5-хеш.
        """
        # Конвертация в прямой порядок байтов
        A = struct.unpack("<I", struct.pack(">I", cls.buffers[MD5Buffer.A]))[0]
        B = struct.unpack("<I", struct.pack(">I", cls.buffers[MD5Buffer.B]))[0]
        C = struct.unpack("<I", struct.pack(">I", cls.buffers[MD5Buffer.C]))[0]
        D = struct.unpack("<I", struct.pack(">I", cls.buffers[MD5Buffer.D]))[0]

        # Форматирование на выходе
        return f"{format(A, '08x')}{format(B, '08x')}{format(C, '08x')}{format(D, '08x')}"
