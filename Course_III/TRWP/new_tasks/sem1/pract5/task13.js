/*
13)	Every и some
У массивов есть ещё стандартные методы every и some.
Они принимают как аргумент некую функцию, которая,
будучи вызванной с элементом массива в качестве аргумента, возвращает true или false.
Так же, как && возвращает true, только если выражения с обеих сторон оператора возвращают true,
метод every возвращает true, когда функция возвращает true для всех элементов массива.
Соответственно, some возвращает true,
когда заданная функция возвращает true при работе хотя бы с одним из элементов массива.
Они не обрабатывают больше элементов, чем необходимо – например, если some получает true для первогоэлемента,
он не обрабатывает оставшиеся.

Напишите функции every и some, которые работают так же, как эти методы,
только принимают массив в качестве аргумента.
 */

function some(array) {
    for (let i = 0; i < array.length; i++) {
        if (isNaN(array[i]))
            return true;
    }
    return false;
}

function every(array) {
    for (let i = 0; i < array.length; i++) {
        if (!isNaN(array[i]))
            return false;
    }
    return true;
}

console.log(every([NaN, NaN, NaN]));
console.log(every([NaN, 1, NaN]));

console.log("---")

console.log(some([NaN, 3, 4]));
console.log(some([2, 3, 4]));