/*
7) Обращаем массив вспять.
Напишите две функции, reverseArray и reverseArrayInPlace.
Первая получает массив как аргумент и выдаёт новый массив, с обратным порядком элементов.

Вторая работает как оригинальный метод reverse – она меняет порядок элементов на обратный в том массиве,
который был ей передан в качестве аргумента. Не используйте стандартный метод reverse.
 */

function reverseArray(array) {
    let result = [];
    for (let i = array.length - 1; i >= 0; i--)
        result.push(array[i]);
    return result;
}

function reverseArrayInPlace(array) {

    for (let i = 0; i < Math.floor(array.length / 2); i++) {
        let old = array[i];
        let len = array.length - 1 - i;
        array[i] = array[len];
        array[len] = old;
    }
    return array;
}


let arr = [10, 20, 30, 35, 40]
console.log(arr);
console.log(reverseArrayInPlace(arr));
console.log(arr);
console.log(reverseArray(arr));