/*
6)	Сумма диапазона.  Напишите функцию
range, принимающую два аргумента, начало и конец диапазона, и возвращающую массив,
 который содержит все числа из него, включая начальное и конечное.
 Затем напишите функцию sum, принимающую массив чисел и возвращающую их сумму.
 Запустите указанную выше инструкцию и убедитесь, что она возвращает 55.
 В качестве бонуса дополните функцию range, чтобы она могла принимать необязательный третий аргумент
 – шаг для построения массива.

 Если он не задан, шаг равен единице.
 Вызов функции range(1, 10, 2) должен будет вернуть [1, 3, 5, 7, 9].
 Убедитесь, что она работает с отрицательным шагом так, что вызов range(5, 2, -1)
 возвращает [5, 4, 3, 2].
 */

function myrange(start, end, step) {
    const array = [];
    const typeofStart = typeof start;
    const typeofEnd = typeof end;

    if (step === 0) {
        throw TypeError("Step cannot be zero.");
    }
    if (typeofStart === "undefined" || typeofEnd === "undefined") {
        throw TypeError("Must pass start and end arguments.");
    } else if (typeofStart !== typeofEnd) {
        throw TypeError("Start and end arguments must be of same type.");
    }

    typeof step == "undefined" && (step = 1);
    while (step > 0 ? end >= start : end <= start) {
        array.push(start);
        start += step;
    }

    return array;
}

function sum(array) {
    let summ = 0;
    for (let i = 0; i < array.length; i++)
        summ += array[i];
    return summ
}

result = myrange(1, 10, 1);
console.log(result);
console.log(sum(result));