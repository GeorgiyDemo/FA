/*
5)	Считаем бобы.
Символ номер N строки можно получить, добавив к ней .charAt(N)
( “строчка”.charAt(5) ) – схожим образом с получением длины строки при помощи .length.
Возвращаемое значение будет строковым,
состоящим из одного символа (к примеру, “к”).
У первого символа строки позиция 0, что означает,
что у последнего символа позиция будет string.length – 1.

Другими словами, у строки из двух символов длина 2,
а позиции её символов будут 0 и 1.
Напишите функцию countBs, которая принимает строку в качестве аргумента,
и возвращает количество символов “B”, содержащихся в строке.
Затем напишите функцию countChar, которая работает примерно как countBs,
только принимает второй параметр — символ, который мы будем искать в
строке (вместо того, чтобы просто считать количество символов “B”).

Для этого переделайте функцию countBs.
 */

function countBs(justString) {
    let counter = 0;
    for (let i = 0; i < justString.length; i++) {
        counter++;
    }
    console.log(counter)
}

function countChar(justString, char) {
    let counter = 0;
    for (let i = 0; i < justString.length; i++) {
        if (justString.charAt(i) === char) {
            counter++;
        }
    }
    console.log(counter)
}

const text = "countBs";
console.log(text)
countBs(text)
countChar(text, "B")
